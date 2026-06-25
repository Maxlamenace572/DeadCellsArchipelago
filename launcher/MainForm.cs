using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.IO.Compression;
using System.Net.Http;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json.Linq;

namespace DeadCellsInstaller
{
    public class MainForm : Form
    {
        // ─── GitHub URLs ────────────────────────────────────────────────
        private const string CORE_API = "https://api.github.com/repos/dead-cells-core-modding/core/releases/latest";
        private const string MOD_API  = "https://api.github.com/repos/Maxlamenace572/DeadCellsArchipelago/releases/latest";

        private const string DEFAULT_PATH =
            @"C:\Program Files (x86)\Steam\steamapps\common\Dead Cells\deadcells.exe";

        // ─── Controls ───────────────────────────────────────────────────
        private Label       lblTitle;
        private Label       lblPath;
        private TextBox     txtPath;
        private Button      btnBrowse;
        private Label       lblWarning;
        private Label       lblWarningDccm;
        private CheckBox    chkNonSteam;
        private CheckBox    chkGog;
        private Button      btnInstall;
        private Button      btnUpdateDccm;
        private Button      btnLaunch;
        private ProgressBar progressBar;
        private Label       lblStatus;
        private RichTextBox rtbLog;

        // ─── State ──────────────────────────────────────────────────────
        private string deadCellsDir;

        private static readonly string ConfigPath = Path.Combine(
            AppDomain.CurrentDomain.BaseDirectory, "installer.cfg");

        // ════════════════════════════════════════════════════════════════
        //  CONSTRUCTEUR
        // ════════════════════════════════════════════════════════════════
        public MainForm()
        {
            InitializeComponent();
            using (var stream = System.Reflection.Assembly.GetExecutingAssembly()
                .GetManifestResourceStream("DeadCellsInstaller.logo.ico"))
            {
                if (stream != null) this.Icon = new Icon(stream);
            }
            LoadSavedPath();
            _ = RefreshWarningsAsync();
        }

        // ════════════════════════════════════════════════════════════════
        //  CONFIG PERSISTANTE (format "key=value" par ligne)
        // ════════════════════════════════════════════════════════════════
        private string ReadConfig(string key)
        {
            try
            {
                if (!File.Exists(ConfigPath)) return null;
                foreach (var line in File.ReadAllLines(ConfigPath))
                {
                    int idx = line.IndexOf('=');
                    if (idx > 0 && line.Substring(0, idx).Trim() == key)
                        return line.Substring(idx + 1).Trim();
                }
            }
            catch { }
            return null;
        }

        private void WriteConfig(string key, string value)
        {
            try
            {
                var lines = new System.Collections.Generic.List<string>();
                if (File.Exists(ConfigPath))
                    lines.AddRange(File.ReadAllLines(ConfigPath));

                bool found = false;
                for (int i = 0; i < lines.Count; i++)
                {
                    int idx = lines[i].IndexOf('=');
                    if (idx > 0 && lines[i].Substring(0, idx).Trim() == key)
                    {
                        lines[i] = key + "=" + value;
                        found = true;
                        break;
                    }
                }
                if (!found) lines.Add(key + "=" + value);
                File.WriteAllLines(ConfigPath, lines);
            }
            catch { }
        }

        private void LoadSavedPath()
        {
            try
            {
                string saved = ReadConfig("path");
                txtPath.Text = !string.IsNullOrEmpty(saved) ? saved : DEFAULT_PATH;
            }
            catch { txtPath.Text = DEFAULT_PATH; }
        }

        private void SavePath(string path)       => WriteConfig("path", path);
        private bool LoadFallbackMode()           => ReadConfig("fallback") == "true";
        private void SaveFallbackMode(bool value) => WriteConfig("fallback", value ? "true" : "false");

        // ════════════════════════════════════════════════════════════════
        //  UI SETUP
        // ════════════════════════════════════════════════════════════════
        private void InitializeComponent()
        {
            this.Text          = "Dead Cells Archipelago Installer";
            this.Size          = new Size(620, 610);
            this.MinimumSize   = new Size(620, 610);
            this.StartPosition = FormStartPosition.CenterScreen;
            this.BackColor     = Color.FromArgb(22, 22, 30);
            this.ForeColor     = Color.White;
            this.Font          = new Font("Segoe UI", 9.5f);

            // ── Title ──
            lblTitle = new Label
            {
                Text      = "Dead Cells · Archipelago Installer",
                Font      = new Font("Segoe UI", 14f, FontStyle.Bold),
                ForeColor = Color.FromArgb(220, 80, 60),
                AutoSize  = true,
                Location  = new Point(20, 18)
            };

            // ── Path label ──
            lblPath = new Label
            {
                Text      = "Path to deadcells.exe :",
                AutoSize  = true,
                Location  = new Point(20, 65),
                ForeColor = Color.FromArgb(180, 180, 190)
            };

            // ── Path text box ──
            txtPath = new TextBox
            {
                Location    = new Point(20, 85),
                Width       = 480,
                BackColor   = Color.FromArgb(35, 35, 45),
                ForeColor   = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };
            txtPath.TextChanged += async (s, e) => await RefreshWarningsAsync();

            // ── Browse ──
            btnBrowse = new Button
            {
                Text      = "Browse…",
                Location  = new Point(510, 83),
                Width     = 80,
                Height    = 26,
                BackColor = Color.FromArgb(50, 50, 65),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Cursor    = Cursors.Hand
            };
            btnBrowse.FlatAppearance.BorderColor = Color.FromArgb(80, 80, 100);
            btnBrowse.Click += BtnBrowse_Click;

            // ── Warning : path / mod ──
            lblWarning = new Label
            {
                Text      = "",
                AutoSize  = false,
                Location  = new Point(20, 116),
                Width     = 570,
                Height    = 20,
                ForeColor = Color.FromArgb(255, 200, 60),
                Font      = new Font("Segoe UI", 9f)
            };

            // ── Warning : DCCM version ──
            lblWarningDccm = new Label
            {
                Text      = "",
                AutoSize  = false,
                Location  = new Point(20, 136),
                Width     = 570,
                Height    = 20,
                ForeColor = Color.FromArgb(255, 200, 60),
                Font      = new Font("Segoe UI", 9f)
            };

            // ── Checkboxes ──
            chkNonSteam = new CheckBox
            {
                Text      = "Non-Steam version  (writes coremod/config/modcore.json)",
                Location  = new Point(20, 162),
                Width     = 400,
                ForeColor = Color.FromArgb(180, 180, 190),
                BackColor = Color.Transparent
            };

            chkGog = new CheckBox
            {
                Text      = "GOG version  (uses deadcells-gog.exe for fallback install)",
                Location  = new Point(20, 184),
                Width     = 400,
                ForeColor = Color.FromArgb(180, 180, 190),
                BackColor = Color.Transparent
            };

            // ── Install / Update button ──
            btnInstall = new Button
            {
                Text      = "Install / Update mod",
                Location  = new Point(20, 214),
                Width     = 280,
                Height    = 36,
                BackColor = Color.FromArgb(180, 50, 40),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font      = new Font("Segoe UI", 10f, FontStyle.Bold),
                Cursor    = Cursors.Hand
            };
            btnInstall.FlatAppearance.BorderSize = 0;
            btnInstall.Click += BtnInstall_Click;

            // ── Update DCCM button ──
            btnUpdateDccm = new Button
            {
                Text      = "Update DCCM",
                Location  = new Point(310, 214),
                Width     = 115,
                Height    = 36,
                BackColor = Color.FromArgb(60, 90, 160),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font      = new Font("Segoe UI", 10f, FontStyle.Bold),
                Cursor    = Cursors.Hand
            };
            btnUpdateDccm.FlatAppearance.BorderSize = 0;
            btnUpdateDccm.Click += BtnUpdateDccm_Click;

            // ── Launch button ──
            btnLaunch = new Button
            {
                Text      = "▶  Launch",
                Location  = new Point(435, 214),
                Width     = 155,
                Height    = 36,
                BackColor = Color.FromArgb(40, 130, 80),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font      = new Font("Segoe UI", 10f, FontStyle.Bold),
                Cursor    = Cursors.Hand
            };
            btnLaunch.FlatAppearance.BorderSize = 0;
            btnLaunch.Click += BtnLaunch_Click;

            // ── Progress bar ──
            progressBar = new ProgressBar
            {
                Location = new Point(20, 262),
                Width    = 570,
                Height   = 16,
                Minimum  = 0,
                Maximum  = 100,
                Value    = 0,
                Style    = ProgressBarStyle.Continuous
            };

            // ── Status label ──
            lblStatus = new Label
            {
                Text      = "Waiting…",
                AutoSize  = false,
                Location  = new Point(20, 284),
                Width     = 570,
                ForeColor = Color.FromArgb(150, 150, 160)
            };

            // ── Log box ──
            rtbLog = new RichTextBox
            {
                Location    = new Point(20, 308),
                Width       = 570,
                Height      = 260,
                BackColor   = Color.FromArgb(12, 12, 18),
                ForeColor   = Color.FromArgb(180, 220, 180),
                ReadOnly    = true,
                Font        = new Font("Consolas", 8.5f),
                BorderStyle = BorderStyle.FixedSingle,
                ScrollBars  = RichTextBoxScrollBars.Vertical
            };

            this.Controls.AddRange(new Control[] {
                lblTitle, lblPath, txtPath, btnBrowse,
                lblWarning, lblWarningDccm,
                chkNonSteam, chkGog,
                btnInstall, btnUpdateDccm, btnLaunch,
                progressBar, lblStatus, rtbLog
            });
        }

        // ════════════════════════════════════════════════════════════════
        //  WARNINGS
        // ════════════════════════════════════════════════════════════════
        private async Task RefreshWarningsAsync()
        {
            string raw = txtPath.Text.Trim();

            // ── Warning 1 : chemin / mod ──
            if (string.IsNullOrEmpty(raw)
                || !Path.GetFileName(raw).Equals("deadcells.exe", StringComparison.OrdinalIgnoreCase)
                || !File.Exists(raw))
            {
                SetWarning("⚠  Path is invalid or deadcells.exe not found.");
                SetWarningDccm("");
                return;
            }

            // Chemin OK — vérifier mise à jour du mod
            SetWarning("⚠  Checking for mod update…");
            SetWarningDccm("⚠  Checking for DCCM update…");
            try
            {
                string dir         = Path.GetDirectoryName(raw);
                string modInfoPath = Path.Combine(dir, "coremod", "mods",
                    "DeadCellsArchipelago", "modinfo.json");
                string localMod  = ReadLocalModVersion(modInfoPath);
                string remoteMod = await GetRemoteModVersion();

                if (localMod == null)
                    SetWarning("⚠  Mod not installed yet — run Install / Update.");
                else if (localMod != remoteMod)
                    SetWarning($"⚠  Mod update available : {localMod} → {remoteMod}");
                else
                    SetWarning("");
            }
            catch { SetWarning(""); }

            // ── Warning 2 : DCCM ──
            try
            {
                string dir            = Path.GetDirectoryName(raw);
                string dccmVerPath    = Path.Combine(dir, "coremod", "ModCoreVersion.txt");
                string localDccm      = ReadLocalDccmVersion(dccmVerPath);
                string remoteDccm     = await GetRemoteDccmVersion();

                if (localDccm == null)
                    SetWarningDccm("");   // DCCM pas installé, pas pertinent ici
                else if (localDccm != remoteDccm)
                    SetWarningDccm($"⚠  DCCM update available : {localDccm} → {remoteDccm}");
                else
                    SetWarningDccm("");
            }
            catch { SetWarningDccm(""); }
        }

        private void SetWarning(string text)
        {
            if (InvokeRequired) { Invoke(new Action(() => SetWarning(text))); return; }
            lblWarning.Text = text;
        }

        private void SetWarningDccm(string text)
        {
            if (InvokeRequired) { Invoke(new Action(() => SetWarningDccm(text))); return; }
            lblWarningDccm.Text = text;
        }

        // ════════════════════════════════════════════════════════════════
        //  EVENTS
        // ════════════════════════════════════════════════════════════════
        private void BtnBrowse_Click(object sender, EventArgs e)
        {
            using (var dlg = new OpenFileDialog())
            {
                dlg.Title  = "Select deadcells.exe";
                dlg.Filter = "deadcells.exe|deadcells.exe";
                if (dlg.ShowDialog() == DialogResult.OK)
                    txtPath.Text = dlg.FileName;
            }
        }

        private async void BtnInstall_Click(object sender, EventArgs e)
        {
            if (!ValidatePath()) return;
            SetUiEnabled(false);
            rtbLog.Clear();
            progressBar.Value = 0;
            try   { await RunInstallation(); }
            catch (Exception ex) { LogError("Fatal error : " + ex.Message); SetStatus("Installation failed."); }
            finally
            {
                SetUiEnabled(true);
                await RefreshWarningsAsync();
            }
        }

        private async void BtnUpdateDccm_Click(object sender, EventArgs e)
        {
            if (!ValidatePath()) return;
            SetUiEnabled(false);
            rtbLog.Clear();
            progressBar.Value = 0;
            try   { await RunUpdateDccm(); }
            catch (Exception ex) { LogError("Fatal error : " + ex.Message); SetStatus("DCCM update failed."); }
            finally
            {
                SetUiEnabled(true);
                await RefreshWarningsAsync();
            }
        }

        private void BtnLaunch_Click(object sender, EventArgs e)
        {
            if (!ValidatePath()) return;
            LaunchGame();
        }

        // ════════════════════════════════════════════════════════════════
        //  VALIDATION
        // ════════════════════════════════════════════════════════════════
        private bool ValidatePath()
        {
            string raw = txtPath.Text.Trim();

            if (string.IsNullOrEmpty(raw))
            { Error("Enter a path to deadcells.exe."); return false; }

            if (!Path.GetFileName(raw).Equals("deadcells.exe", StringComparison.OrdinalIgnoreCase))
            { Error("Path should point to deadcells.exe."); return false; }

            if (!File.Exists(raw))
            { Error("deadcells.exe not found at this path."); return false; }

            deadCellsDir = Path.GetDirectoryName(raw);
            SavePath(raw);
            return true;
        }

        // ════════════════════════════════════════════════════════════════
        //  LAUNCH
        // ════════════════════════════════════════════════════════════════
        private void LaunchGame()
        {
            string coremodDir  = Path.Combine(deadCellsDir, "coremod");
            string launcherExe = Path.Combine(coremodDir, "core", "host", "startup", "DeadCellsModding.exe");
            string fallbackExe = Path.Combine(deadCellsDir, "DeadCellsModding.exe");

            string exeToLaunch;
            if (LoadFallbackMode())
            {
                exeToLaunch = File.Exists(fallbackExe) ? fallbackExe : null;
                if (exeToLaunch == null)
                    Log("  Warning: fallback exe not found, trying standard path…");
            }
            else
            {
                exeToLaunch = File.Exists(launcherExe) ? launcherExe : null;
                if (exeToLaunch == null)
                    Log("  Warning: standard launcher not found, trying fallback path…");
            }

            // Filet de sécurité
            if (exeToLaunch == null)
                exeToLaunch = File.Exists(launcherExe) ? launcherExe
                            : File.Exists(fallbackExe) ? fallbackExe
                            : null;

            if (exeToLaunch == null)
            { Error("DeadCellsModding.exe not found.\nPlease run Install / Update first."); return; }

            Log("→ Starting " + exeToLaunch + "…");
            Process.Start(exeToLaunch);
            SetStatus("Game launched!");
        }

        // ════════════════════════════════════════════════════════════════
        //  INSTALLATION PIPELINE
        // ════════════════════════════════════════════════════════════════
        private async Task RunInstallation()
        {
            bool nonSteam  = chkNonSteam.Checked;
            bool gog       = chkGog.Checked;
            bool psEnabled = ArePowerShellScriptsEnabled();
            string coremodDir = Path.Combine(deadCellsDir, "coremod");

            if (nonSteam && !psEnabled)
            {
                LogError("⚠  Incompatible options: the no-PowerShell fallback method");
                LogError("   is not compatible with the Non-Steam version.");
                LogError("   Please enable PowerShell script execution, or uncheck Non-Steam.");
                SetStatus("Installation cancelled.");
                return;
            }

            // ── STEP 1 : .NET 10 ────────────────────────────────────────
            SetStatus("Checking for .NET 10 Runtime…");
            Log("→ Checking for .NET 10 Runtime…");

            if (!CheckDotnet10Runtime())
            {
                Log("  .NET 10 Runtime not found. Downloading installer…");
                await InstallDotnet10();
                SetProgress(10);

                // On vérifie en ciblant aussi l'exe local (pas encore dans PATH)
                if (!CheckDotnet10Runtime())
                {
                    LogError("  .NET 10 Runtime installation failed. Cancelling.");
                    return;
                }
                Log("  .NET 10 Runtime installed successfully. ✓");
            }
            else
            {
                Log("  .NET 10 Runtime already present. ✓");
            }
            SetProgress(10);

            // ── STEP 2 : Core ────────────────────────────────────────────
            if (psEnabled)
                await InstallCoreWithPs1(coremodDir);
            else
            {
                Log($"→ PowerShell scripts disabled — using fallback method ({(gog ? "GOG" : "Steam")}).");
                await InstallCoreWithoutPs1(gog);
            }

            // ── STEP 3 : Non-Steam config ────────────────────────────────
            if (nonSteam) WriteNonSteamConfig(coremodDir);

            // ── STEP 4 : mods.zip ────────────────────────────────────────
            string modInfoPath = Path.Combine(
                coremodDir, "mods", "DeadCellsArchipelago", "modinfo.json");
            string localVersion  = ReadLocalModVersion(modInfoPath);
            string remoteVersion = await GetRemoteModVersion();

            Log($"→ Local mod version  : {(localVersion ?? "missing")}");
            Log($"  Latest on GitHub   : {remoteVersion}");

            if (localVersion == remoteVersion && localVersion != null)
            {
                Log("  Mod already up to date. ✓");
                SetProgress(90);
            }
            else
            {
                SetStatus("Downloading mods.zip…");
                Log("→ Downloading mods.zip…");
                string modZipUrl = await GetAssetUrl(MOD_API, "mods.zip");
                string modZip    = Path.Combine(Path.GetTempPath(), "dc_mods.zip");

                await DownloadFile(modZipUrl, modZip, 55, 85, "Downloading Archipelago mod…");

                SetStatus("Extracting mods.zip…");
                Log("→ Extracting to " + coremodDir + "…");
                ExtractZip(modZip, coremodDir);
                File.Delete(modZip);
                Log("  Extraction done. ✓");
                SetProgress(90);
            }

            SetProgress(100);
            Log("  Installation complete! Launching…");
            SetStatus("Done — launching game…");
            LaunchGame();
        }

        // ════════════════════════════════════════════════════════════════
        //  UPDATE DCCM PIPELINE
        // ════════════════════════════════════════════════════════════════
        private async Task RunUpdateDccm()
        {
            bool psEnabled = ArePowerShellScriptsEnabled();
            bool gog       = chkGog.Checked;
            string coremodDir = Path.Combine(deadCellsDir, "coremod");

            string localDccm  = ReadLocalDccmVersion(Path.Combine(coremodDir, "ModCoreVersion.txt"));
            string remoteDccm = await GetRemoteDccmVersion();

            Log($"→ Local DCCM version  : {(localDccm ?? "missing")}");
            Log($"  Latest on GitHub    : {remoteDccm}");

            if (localDccm == remoteDccm)
            {
                Log("  DCCM already up to date. ✓");
                SetProgress(100);
                SetStatus("DCCM is already up to date.");
                return;
            }

            if (psEnabled)
            {
                // Supprimer l'ancien core et réinstaller
                Log("→ Removing old coremod/core…");
                string coreDir = Path.Combine(coremodDir, "core");
                if (Directory.Exists(coreDir))
                    Directory.Delete(coreDir, recursive: true);

                await InstallCoreWithPs1(coremodDir);
            }
            else
            {
                Log($"→ PowerShell disabled — updating DeadCellsModding.exe ({(gog ? "GOG" : "Steam")})…");
                // Supprimer l'ancien exe fallback pour forcer le re-téléchargement
                string fallbackExe = Path.Combine(deadCellsDir, "DeadCellsModding.exe");
                if (File.Exists(fallbackExe)) File.Delete(fallbackExe);
                await InstallCoreWithoutPs1(gog);
            }

            SetProgress(100);
            SetStatus("DCCM updated!");
            Log("  DCCM update complete. ✓");
        }

        // ════════════════════════════════════════════════════════════════
        //  CORE – méthode normale (avec PS1)
        // ════════════════════════════════════════════════════════════════
        private async Task InstallCoreWithPs1(string coremodDir)
        {
            string coreDir = Path.Combine(coremodDir, "core");
            string corePs1 = Path.Combine(coreDir, "mdk", "install.ps1");

            if (File.Exists(corePs1))
            {
                Log("→ core already installed, download skipped. ✓");
                SaveFallbackMode(false);
                SetProgress(40);
            }
            else
            {
                SetStatus("Downloading core (win-x64.zip)…");
                Log("→ Fetching latest core release from GitHub…");
                string coreZipUrl = await GetAssetUrl(CORE_API, "win-x64.zip");
                string coreZip    = Path.Combine(Path.GetTempPath(), "dc_core_win-x64.zip");

                await DownloadFile(coreZipUrl, coreZip, 10, 35, "Downloading DCCM…");

                SetStatus("Extracting core…");
                Log("→ Extracting to " + coremodDir + "…");
                Directory.CreateDirectory(coremodDir);
                ExtractZip(coreZip, coremodDir);
                File.Delete(coreZip);
                SaveFallbackMode(false);
                Log("  Extraction done. ✓");
                SetProgress(40);
            }

            if (!File.Exists(corePs1))
                throw new Exception("install.ps1 not found after extraction: " + corePs1);

            string coremodDataDir = Path.Combine(coremodDir, "data");
            if (Directory.Exists(coremodDataDir))
            {
                Log("→ coremod\\data already present, install.ps1 skipped. ✓");
                SetProgress(55);
            }
            else
            {
                SetStatus("Running install.ps1…");
                Log("→ Running install.ps1…");
                await RunPowerShell(corePs1);
                Log("  install.ps1 done. ✓");
                SetProgress(55);
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  CORE – méthode fallback (sans PS1)
        //  gog=true  → télécharge deadcells-gog.exe
        //  gog=false → télécharge deadcells.exe
        //  Dans les deux cas, renommé en DeadCellsModding.exe dans Dead Cells\
        // ════════════════════════════════════════════════════════════════
        private async Task InstallCoreWithoutPs1(bool gog)
        {
            string destExe    = Path.Combine(deadCellsDir, "DeadCellsModding.exe");
            string assetName  = gog ? "deadcells-gog.exe" : "deadcells.exe";

            if (File.Exists(destExe))
            {
                Log("→ DeadCellsModding.exe already present (fallback), skipped. ✓");
                SetProgress(55);
                return;
            }

            SetStatus($"Downloading DeadCellsModding.exe (fallback, {(gog ? "GOG" : "Steam")})…");
            Log($"→ Fetching {assetName} from core release…");

            string exeUrl  = await GetAssetUrl(CORE_API, assetName);
            string tempExe = Path.Combine(Path.GetTempPath(), "dc_modding_temp.exe");

            await DownloadFile(exeUrl, tempExe, 10, 55, "Downloading DeadCellsModding.exe…");

            Log($"→ Renaming and moving to Dead Cells\\DeadCellsModding.exe…");
            if (File.Exists(destExe)) File.Delete(destExe);
            File.Move(tempExe, destExe);
            SaveFallbackMode(true);
            Log("  DeadCellsModding.exe placed in Dead Cells\\. ✓");
            SetProgress(55);
        }

        // ════════════════════════════════════════════════════════════════
        //  NON-STEAM CONFIG
        // ════════════════════════════════════════════════════════════════
        private void WriteNonSteamConfig(string coremodDir)
        {
            string configDir  = Path.Combine(coremodDir, "config");
            string configFile = Path.Combine(configDir, "modcore.json");
            Directory.CreateDirectory(configDir);
            if (!File.Exists(configFile))
            {
                File.WriteAllText(configFile, "{\n  \"steam\": false\n}\n");
                Log("→ modcore.json written (non-Steam mode). ✓");
            }
            else
            {
                Log("→ modcore.json already present, not overwritten. ✓");
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – PowerShell activé ?
        // ════════════════════════════════════════════════════════════════
        private bool ArePowerShellScriptsEnabled()
        {
            try
            {
                var psi = new ProcessStartInfo("powershell.exe",
                    "-NonInteractive -Command \"Get-ExecutionPolicy\"")
                {
                    RedirectStandardOutput = true,
                    UseShellExecute        = false,
                    CreateNoWindow         = true
                };
                using (var p = Process.Start(psi))
                {
                    string output = p.StandardOutput.ReadToEnd().Trim().ToLowerInvariant();
                    p.WaitForExit();
                    return output != "restricted";
                }
            }
            catch { return false; }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – .NET 10
        //
        //  PROBLÈME : dotnet-install.ps1 installe dans AppData\Local\Microsoft\dotnet
        //  mais DeadCellsModding.exe cherche le runtime dans C:\Program Files\dotnet\
        //  (installation système). Ces deux emplacements sont indépendants.
        //  Solution : télécharger l'installeur officiel .exe Microsoft qui installe
        //  dans Program Files, visible de tous les exes du système.
        // ════════════════════════════════════════════════════════════════
        private bool CheckDotnet10Runtime()
        {
            // Vérification directe dans C:\Program Files\dotnet\shared\Microsoft.NETCore.App\
            string systemRuntimeDir = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.ProgramFiles),
                "dotnet", "shared", "Microsoft.NETCore.App");

            if (Directory.Exists(systemRuntimeDir))
            {
                foreach (var dir in Directory.GetDirectories(systemRuntimeDir))
                {
                    if (Regex.IsMatch(Path.GetFileName(dir), @"^10\."))
                        return true;
                }
            }

            // Fallback : via dotnet --list-runtimes (PATH système ou AppData)
            foreach (string dotnet in new[] {
                "dotnet",
                Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                    "Microsoft", "dotnet", "dotnet.exe") })
            {
                try
                {
                    var psi = new ProcessStartInfo(dotnet, "--list-runtimes")
                    {
                        RedirectStandardOutput = true,
                        UseShellExecute        = false,
                        CreateNoWindow         = true
                    };
                    using (var p = Process.Start(psi))
                    {
                        string output = p.StandardOutput.ReadToEnd();
                        p.WaitForExit();
                        if (Regex.IsMatch(output, @"Microsoft\.NETCore\.App 10\.", RegexOptions.Multiline))
                            return true;
                    }
                }
                catch { }
            }
            return false;
        }

        private async Task InstallDotnet10()
        {
            // URL stable officielle Microsoft — installe dans C:\Program Files\dotnet\
            // contrairement à dotnet-install.ps1 qui installe dans AppData
            const string runtimeInstallerUrl =
                "https://aka.ms/dotnet/10.0/dotnet-runtime-win-x64.exe";

            string installerPath = Path.Combine(Path.GetTempPath(), "dotnet10-runtime-installer.exe");

            Log("  Downloading .NET 10 Runtime installer…");
            using (var client = NewHttpClient())
            using (var response = await client.GetAsync(runtimeInstallerUrl, HttpCompletionOption.ResponseHeadersRead))
            {
                response.EnsureSuccessStatusCode();
                long? total = response.Content.Headers.ContentLength;
                using (var src  = await response.Content.ReadAsStreamAsync())
                using (var file = File.Create(installerPath))
                {
                    byte[] buf = new byte[81920];
                    long read = 0; int bytesRead;
                    while ((bytesRead = await src.ReadAsync(buf, 0, buf.Length)) > 0)
                    {
                        await file.WriteAsync(buf, 0, bytesRead);
                        read += bytesRead;
                        if (total.HasValue)
                        {
                            string mb  = (read / 1048576.0).ToString("0.0");
                            string mb2 = (total.Value / 1048576.0).ToString("0.0");
                            SetStatus($"Downloading .NET 10 Runtime… ({mb} / {mb2} MB)");
                        }
                    }
                }
            }
            Log("  Running .NET 10 Runtime installer (a UAC prompt may appear)…");

            // /install /quiet /norestart — silencieux, installe dans Program Files
            var psi = new ProcessStartInfo(installerPath, "/install /quiet /norestart")
            {
                UseShellExecute = true,   // nécessaire pour l'élévation UAC
                Verb            = "runas"
            };
            using (var p = Process.Start(psi))
            {
                await Task.Run(() => p.WaitForExit());
                // Exit code 3010 = succès avec redémarrage requis (acceptable)
                if (p.ExitCode != 0 && p.ExitCode != 3010 && !CheckDotnet10Runtime())
                    throw new Exception($".NET 10 Runtime installer failed (code {p.ExitCode}).");
            }
            try { File.Delete(installerPath); } catch { }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – GitHub API
        // ════════════════════════════════════════════════════════════════
        private async Task<string> GetAssetUrl(string apiUrl, string assetName)
        {
            using (var client = NewHttpClient())
            {
                string json = await client.GetStringAsync(apiUrl);
                var obj = JObject.Parse(json);
                foreach (var asset in obj["assets"])
                {
                    if (asset["name"].ToString().Equals(assetName, StringComparison.OrdinalIgnoreCase))
                        return asset["browser_download_url"].ToString();
                }
            }
            throw new Exception($"Asset '{assetName}' not found in GitHub release.");
        }

        private async Task<string> GetRemoteModVersion()
        {
            using (var client = NewHttpClient())
            {
                string json = await client.GetStringAsync(MOD_API);
                var obj = JObject.Parse(json);
                return (obj["tag_name"]?.ToString() ?? "").TrimStart('v');
            }
        }

        private async Task<string> GetRemoteDccmVersion()
        {
            using (var client = NewHttpClient())
            {
                string json = await client.GetStringAsync(CORE_API);
                var obj = JObject.Parse(json);
                return (obj["tag_name"]?.ToString() ?? "").TrimStart('v');
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – versions locales
        // ════════════════════════════════════════════════════════════════
        private string ReadLocalModVersion(string modInfoPath)
        {
            if (!File.Exists(modInfoPath)) return null;
            try
            {
                var obj = JObject.Parse(File.ReadAllText(modInfoPath));
                return obj["version"]?.ToString();
            }
            catch { return null; }
        }

        private string ReadLocalDccmVersion(string versionFilePath)
        {
            if (!File.Exists(versionFilePath)) return null;
            try { return File.ReadAllText(versionFilePath).Trim(); }
            catch { return null; }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – Download
        // ════════════════════════════════════════════════════════════════
        private async Task DownloadFile(string url, string dest,
            int progressFrom, int progressTo, string statusLabel)
        {
            using (var client = NewHttpClient())
            using (var response = await client.GetAsync(url, HttpCompletionOption.ResponseHeadersRead))
            {
                response.EnsureSuccessStatusCode();
                long? total = response.Content.Headers.ContentLength;

                using (var src  = await response.Content.ReadAsStreamAsync())
                using (var file = File.Create(dest))
                {
                    byte[] buf = new byte[81920];
                    long   read = 0;
                    int    bytesRead;

                    while ((bytesRead = await src.ReadAsync(buf, 0, buf.Length)) > 0)
                    {
                        await file.WriteAsync(buf, 0, bytesRead);
                        read += bytesRead;
                        if (total.HasValue)
                        {
                            double pct  = (double)read / total.Value;
                            int    prog = progressFrom + (int)(pct * (progressTo - progressFrom));
                            SetProgress(prog);
                            string mb  = (read / 1048576.0).ToString("0.0");
                            string mb2 = (total.Value / 1048576.0).ToString("0.0");
                            SetStatus($"{statusLabel} ({mb} / {mb2} MB)");
                        }
                    }
                }
            }
            Log($"  Downloaded → {dest}");
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – Zip
        // ════════════════════════════════════════════════════════════════
        private void ExtractZip(string zipPath, string destDir)
        {
            using (var archive = ZipFile.OpenRead(zipPath))
            {
                foreach (var entry in archive.Entries)
                {
                    string fullDest = Path.GetFullPath(Path.Combine(destDir, entry.FullName));
                    if (!fullDest.StartsWith(Path.GetFullPath(destDir), StringComparison.OrdinalIgnoreCase))
                        continue;
                    if (string.IsNullOrEmpty(entry.Name))
                        Directory.CreateDirectory(fullDest);
                    else
                    {
                        Directory.CreateDirectory(Path.GetDirectoryName(fullDest));
                        entry.ExtractToFile(fullDest, overwrite: true);
                    }
                }
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – PowerShell runner
        // ════════════════════════════════════════════════════════════════
        private async Task RunPowerShell(string scriptPath)
        {
            var psi = new ProcessStartInfo("powershell.exe",
                $"-ExecutionPolicy Bypass -File \"{scriptPath}\"")
            {
                WorkingDirectory       = Path.GetDirectoryName(scriptPath),
                UseShellExecute        = false,
                RedirectStandardOutput = true,
                RedirectStandardError  = true,
                CreateNoWindow         = true
            };
            using (var p = Process.Start(psi))
            {
                string stdout = await p.StandardOutput.ReadToEndAsync();
                string stderr = await p.StandardError.ReadToEndAsync();
                p.WaitForExit();
                if (!string.IsNullOrWhiteSpace(stdout))
                    foreach (var line in stdout.Split('\n'))
                        if (!string.IsNullOrWhiteSpace(line)) Log("  [ps1] " + line.Trim());
                if (p.ExitCode != 0)
                    throw new Exception("install.ps1 returned an error: " + p.ExitCode + "\n" + stderr);
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – HTTP
        // ════════════════════════════════════════════════════════════════
        private HttpClient NewHttpClient()
        {
            var client = new HttpClient();
            client.DefaultRequestHeaders.Add("User-Agent", "DeadCellsInstaller/1.0");
            return client;
        }

        // ════════════════════════════════════════════════════════════════
        //  UI HELPERS
        // ════════════════════════════════════════════════════════════════
        private void SetProgress(int value)
        {
            if (InvokeRequired) { Invoke(new Action(() => SetProgress(value))); return; }
            progressBar.Value = Math.Max(0, Math.Min(100, value));
        }

        private void SetStatus(string text)
        {
            if (InvokeRequired) { Invoke(new Action(() => SetStatus(text))); return; }
            lblStatus.Text = text;
        }

        private void SetUiEnabled(bool enabled)
        {
            if (InvokeRequired) { Invoke(new Action(() => SetUiEnabled(enabled))); return; }
            btnInstall.Enabled    = enabled;
            btnUpdateDccm.Enabled = enabled;
            btnLaunch.Enabled     = enabled;
            btnBrowse.Enabled     = enabled;
            txtPath.Enabled       = enabled;
            chkNonSteam.Enabled   = enabled;
            chkGog.Enabled        = enabled;
        }

        private void Log(string msg)
        {
            if (InvokeRequired) { Invoke(new Action(() => Log(msg))); return; }
            rtbLog.AppendText(msg + "\n");
            rtbLog.ScrollToCaret();
        }

        private void LogError(string msg)
        {
            if (InvokeRequired) { Invoke(new Action(() => LogError(msg))); return; }
            int start = rtbLog.TextLength;
            rtbLog.AppendText(msg + "\n");
            rtbLog.Select(start, msg.Length);
            rtbLog.SelectionColor = Color.FromArgb(255, 100, 80);
            rtbLog.SelectionLength = 0;
            rtbLog.ScrollToCaret();
        }

        private void Error(string msg)
            => MessageBox.Show(msg, "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
    }
}
