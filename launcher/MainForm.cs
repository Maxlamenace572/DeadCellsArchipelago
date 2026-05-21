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
        private CheckBox    chkNonSteam;
        private Button      btnInstall;
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
            // Calcul du warning au lancement
            _ = RefreshWarningAsync();
        }

        // ════════════════════════════════════════════════════════════════
        //  CONFIG PERSISTANTE
        // ════════════════════════════════════════════════════════════════
        // ─── Config helpers (format "key=value" par ligne) ─────────────
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

        private void SavePath(string path)
        {
            WriteConfig("path", path);
        }

        private bool LoadFallbackMode()
        {
            return ReadConfig("fallback") == "true";
        }

        private void SaveFallbackMode(bool fallback)
        {
            WriteConfig("fallback", fallback ? "true" : "false");
        }

        // ════════════════════════════════════════════════════════════════
        //  UI SETUP
        // ════════════════════════════════════════════════════════════════
        private void InitializeComponent()
        {
            this.Text          = "Dead Cells Archipelago Installer";
            this.Size          = new Size(620, 540);
            this.MinimumSize   = new Size(620, 540);
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
            txtPath.TextChanged += async (s, e) => await RefreshWarningAsync();

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

            // ── Warning label ──
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

            // ── Non-Steam checkbox ──
            chkNonSteam = new CheckBox
            {
                Text      = "Non-Steam version  (writes coremod/config/modcore.json)",
                Location  = new Point(20, 142),
                Width     = 570,
                ForeColor = Color.FromArgb(180, 180, 190),
                BackColor = Color.Transparent
            };

            // ── Install/Update button ──
            btnInstall = new Button
            {
                Text      = "Install / Update",
                Location  = new Point(20, 170),
                Width     = 375,
                Height    = 36,
                BackColor = Color.FromArgb(180, 50, 40),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font      = new Font("Segoe UI", 10f, FontStyle.Bold),
                Cursor    = Cursors.Hand
            };
            btnInstall.FlatAppearance.BorderSize = 0;
            btnInstall.Click += BtnInstall_Click;

            // ── Launch button ──
            btnLaunch = new Button
            {
                Text      = "▶  Launch",
                Location  = new Point(405, 170),
                Width     = 185,
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
                Location = new Point(20, 218),
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
                Location  = new Point(20, 240),
                Width     = 570,
                ForeColor = Color.FromArgb(150, 150, 160)
            };

            // ── Log box ──
            rtbLog = new RichTextBox
            {
                Location    = new Point(20, 265),
                Width       = 570,
                Height      = 230,
                BackColor   = Color.FromArgb(12, 12, 18),
                ForeColor   = Color.FromArgb(180, 220, 180),
                ReadOnly    = true,
                Font        = new Font("Consolas", 8.5f),
                BorderStyle = BorderStyle.FixedSingle,
                ScrollBars  = RichTextBoxScrollBars.Vertical
            };

            this.Controls.AddRange(new Control[] {
                lblTitle, lblPath, txtPath, btnBrowse,
                lblWarning, chkNonSteam,
                btnInstall, btnLaunch,
                progressBar, lblStatus, rtbLog
            });
        }

        // ════════════════════════════════════════════════════════════════
        //  WARNING – calcul asynchrone
        // ════════════════════════════════════════════════════════════════
        private async Task RefreshWarningAsync()
        {
            string raw = txtPath.Text.Trim();

            // 1. Chemin invalide
            if (string.IsNullOrEmpty(raw)
                || !Path.GetFileName(raw).Equals("deadcells.exe", StringComparison.OrdinalIgnoreCase)
                || !File.Exists(raw))
            {
                SetWarning("⚠  Path is invalid or deadcells.exe not found.");
                return;
            }

            // 2. Chemin OK — vérifier si mise à jour disponible
            SetWarning("⚠  Checking for mod update…");
            try
            {
                string dir         = Path.GetDirectoryName(raw);
                string modInfoPath = Path.Combine(dir, "coremod", "mods",
                    "DeadCellsArchipelago", "modinfo.json");
                string local  = ReadLocalModVersion(modInfoPath);
                string remote = await GetRemoteModVersion();

                if (local == null)
                    SetWarning("⚠  Mod not installed yet — run Install / Update.");
                else if (local != remote)
                    SetWarning($"⚠  Update available : {local} → {remote}");
                else
                    SetWarning("");  // tout est OK
            }
            catch
            {
                SetWarning("");  // pas de réseau, pas de warning bloquant
            }
        }

        private void SetWarning(string text)
        {
            if (InvokeRequired) { Invoke(new Action(() => SetWarning(text))); return; }
            lblWarning.Text = text;
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

            try
            {
                await RunInstallation();
            }
            catch (Exception ex)
            {
                LogError("Fatal error : " + ex.Message);
                SetStatus("Installation failed.");
            }
            finally
            {
                SetUiEnabled(true);
                // Recalcul du warning après installation
                await RefreshWarningAsync();
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
            {
                Error("Enter a path to deadcells.exe.");
                return false;
            }

            if (!Path.GetFileName(raw).Equals("deadcells.exe", StringComparison.OrdinalIgnoreCase))
            {
                Error("Path should point to deadcells.exe.");
                return false;
            }

            if (!File.Exists(raw))
            {
                Error("deadcells.exe not found at this path.");
                return false;
            }

            deadCellsDir = Path.GetDirectoryName(raw);
            SavePath(raw);
            return true;
        }

        // ════════════════════════════════════════════════════════════════
        //  LAUNCH (partagé entre Install et bouton Launch)
        // ════════════════════════════════════════════════════════════════
        private void LaunchGame()
        {
            string coremodDir  = Path.Combine(deadCellsDir, "coremod");
            string launcherExe = Path.Combine(coremodDir, "core", "host", "startup", "DeadCellsModding.exe");
            string fallbackExe = Path.Combine(deadCellsDir, "DeadCellsModding.exe");

            string exeToLaunch;

            if (LoadFallbackMode())
            {
                // Installation via fallback (sans PS1) : on utilise Dead Cells\DeadCellsModding.exe
                exeToLaunch = File.Exists(fallbackExe) ? fallbackExe : null;
                if (exeToLaunch == null)
                    Log("  Warning: fallback exe not found, trying standard path…");
            }
            else
            {
                // Installation standard (avec PS1) : on utilise le launcher dans coremod
                exeToLaunch = File.Exists(launcherExe) ? launcherExe : null;
                if (exeToLaunch == null)
                    Log("  Warning: standard launcher not found, trying fallback path…");
            }

            // Filet de sécurité : si le chemin attendu est absent, on essaie l'autre
            if (exeToLaunch == null)
                exeToLaunch = File.Exists(launcherExe) ? launcherExe
                            : File.Exists(fallbackExe) ? fallbackExe
                            : null;

            if (exeToLaunch == null)
            {
                Error("DeadCellsModding.exe not found.\nPlease run Install / Update first.");
                return;
            }

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
            bool psEnabled = ArePowerShellScriptsEnabled();
            string coremodDir = Path.Combine(deadCellsDir, "coremod");

            // ── Incompatibilité non-Steam + PS désactivé ─────────────────
            if (nonSteam && !psEnabled)
            {
                LogError("⚠  Incompatible options: the no-PowerShell fallback method");
                LogError("   is not compatible with the Non-Steam version.");
                LogError("   Please enable PowerShell script execution, or uncheck Non-Steam.");
                SetStatus("Installation cancelled.");
                return;
            }

            // ── STEP 1 : Check .NET 10 ──────────────────────────────────
            SetStatus("Checking for .NET SDK 10…");
            Log("→ Checking for .NET 10 SDK…");
            bool hasDotnet10 = CheckDotnet10();

            if (!hasDotnet10)
            {
                Log("  .NET 10 SDK not found. Downloading installer…");
                await InstallDotnet10();
                SetProgress(10);

                if (!CheckDotnet10())
                {
                    LogError("  .NET 10 SDK installation failed. Cancelling.");
                    return;
                }
            }
            else
            {
                Log("  .NET 10 SDK already present. ✓");
            }
            SetProgress(10);

            // ── STEP 2 : Core ────────────────────────────────────────────
            if (psEnabled)
            {
                await InstallCoreWithPs1(coremodDir);
            }
            else
            {
                Log("→ PowerShell scripts disabled — using fallback method (direct exe).");
                await InstallCoreWithoutPs1();
            }

            // ── STEP 3 : Non-Steam config ────────────────────────────────
            if (nonSteam)
            {
                WriteNonSteamConfig(coremodDir);
            }

            // ── STEP 4 : Télécharger mods.zip si nécessaire ─────────────
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

            // ── STEP 5 : Lancer le jeu ──────────────────────────────────
            SetProgress(100);
            Log("  Installation complete! Launching…");
            SetStatus("Done — launching game…");
            LaunchGame();
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

                await DownloadFile(coreZipUrl, coreZip, 10, 35, "Downloading core…");

                SetStatus("Extracting core…");
                Log("→ Extracting to " + coremodDir + "…");
                Directory.CreateDirectory(coremodDir);
                ExtractZip(coreZip, coremodDir);
                File.Delete(coreZip);
                Log("  Extraction done. ✓");
                SaveFallbackMode(false);
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
        //  Télécharge deadcells.exe depuis le release core,
        //  le renomme DeadCellsModding.exe et le place dans Dead Cells\
        // ════════════════════════════════════════════════════════════════
        private async Task InstallCoreWithoutPs1()
        {
            string destExe = Path.Combine(deadCellsDir, "DeadCellsModding.exe");

            if (File.Exists(destExe))
            {
                Log("→ DeadCellsModding.exe already present (fallback), skipped. ✓");
                SetProgress(55);
                return;
            }

            SetStatus("Downloading DeadCellsModding.exe (fallback)…");
            Log("→ Fetching deadcells.exe from core release (no-PowerShell fallback)…");

            string exeUrl  = await GetAssetUrl(CORE_API, "deadcells.exe");
            string tempExe = Path.Combine(Path.GetTempPath(), "dc_modding_temp.exe");

            await DownloadFile(exeUrl, tempExe, 10, 55, "Downloading DeadCellsModding.exe…");

            Log($"→ Renaming and moving to Dead Cells\\DeadCellsModding.exe…");
            if (File.Exists(destExe)) File.Delete(destExe);
            File.Move(tempExe, destExe);
            Log("  DeadCellsModding.exe placed in Dead Cells\\. ✓");
            SaveFallbackMode(true);
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
                File.WriteAllText(configFile, "{\n  \"GeneratePseudocodeAssembly\": true,\n  \"AllowCloseConsole\": false,\n  \"AllowLockCursor\": true,\n  \"EnableGoldberg\": true,\n  \"SkipLogoSplash\": true\n}");
                Log("→ modcore.json written (non-Steam mode). ✓");
            }
            else
            {
                Log("→ modcore.json already present, not overwritten. ✓");
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – PowerShell scripts activés ?
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
        // ════════════════════════════════════════════════════════════════
        private System.Collections.Generic.IEnumerable<string> DotnetCandidates()
        {
            yield return "dotnet";
            string local = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                "Microsoft", "dotnet", "dotnet.exe");
            if (File.Exists(local)) yield return local;
        }

        private bool CheckDotnet10()
        {
            foreach (string dotnet in DotnetCandidates())
            {
                try
                {
                    var psi = new ProcessStartInfo(dotnet, "--list-sdks")
                    {
                        RedirectStandardOutput = true,
                        UseShellExecute        = false,
                        CreateNoWindow         = true
                    };
                    using (var p = Process.Start(psi))
                    {
                        string output = p.StandardOutput.ReadToEnd();
                        p.WaitForExit();
                        if (Regex.IsMatch(output, @"^10\.", RegexOptions.Multiline))
                            return true;
                    }
                }
                catch { }
            }
            return false;
        }

        private async Task InstallDotnet10()
        {
            string scriptUrl  = "https://dot.net/v1/dotnet-install.ps1";
            string scriptPath = Path.Combine(Path.GetTempPath(), "dotnet-install.ps1");

            Log("  Downloading .NET install script…");
            using (var client = NewHttpClient())
            {
                byte[] data = await client.GetByteArrayAsync(scriptUrl);
                File.WriteAllBytes(scriptPath, data);
            }

            string installDir = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                "Microsoft", "dotnet");

            Log("  Install directory : " + installDir);
            Log("  Running .NET 10 SDK installer…");

            var psi = new ProcessStartInfo("powershell.exe",
                $"-ExecutionPolicy Bypass -File \"{scriptPath}\" -Channel 10.0 -InstallDir \"{installDir}\"")
            {
                UseShellExecute        = false,
                CreateNoWindow         = true,
                RedirectStandardOutput = true,
                RedirectStandardError  = true
            };

            using (var p = Process.Start(psi))
            {
                p.OutputDataReceived += (s, e) => { if (e.Data != null) Log("  [dotnet] " + e.Data); };
                p.ErrorDataReceived  += (s, e) => { if (e.Data != null) LogError("  [dotnet] " + e.Data); };
                p.BeginOutputReadLine();
                p.BeginErrorReadLine();
                await Task.Run(() => p.WaitForExit());

                if (p.ExitCode != 0 && !CheckDotnet10())
                    throw new Exception($"dotnet-install.ps1 failed (code {p.ExitCode}).");
            }
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
                    string name = asset["name"].ToString();
                    if (name.Equals(assetName, StringComparison.OrdinalIgnoreCase))
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
                string tag = obj["tag_name"]?.ToString() ?? "";
                return tag.TrimStart('v');
            }
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
                            double pct = (double)read / total.Value;
                            int prog = progressFrom + (int)(pct * (progressTo - progressFrom));
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

                    if (!fullDest.StartsWith(Path.GetFullPath(destDir),
                        StringComparison.OrdinalIgnoreCase))
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
        //  HELPERS – PowerShell
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
                        if (!string.IsNullOrWhiteSpace(line))
                            Log("  [ps1] " + line.Trim());

                if (p.ExitCode != 0)
                    throw new Exception("install.ps1 returned an error: "
                        + p.ExitCode + "\n" + stderr);
            }
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – Mod version
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
            btnInstall.Enabled  = enabled;
            btnLaunch.Enabled   = enabled;
            btnBrowse.Enabled   = enabled;
            txtPath.Enabled     = enabled;
            chkNonSteam.Enabled = enabled;
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
