using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.IO.Compression;
using System.Net;
using System.Net.Http;
using System.Runtime.InteropServices;
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

        // ─── Controls ───────────────────────────────────────────────────
        private Label       lblTitle;
        private Label       lblPath;
        private TextBox     txtPath;
        private Button      btnBrowse;
        private Button      btnInstall;
        private ProgressBar progressBar;
        private Label       lblStatus;
        private RichTextBox rtbLog;

        // ─── State ──────────────────────────────────────────────────────
        private string deadCellsDir;

        private static readonly string ConfigPath = Path.Combine(
            AppDomain.CurrentDomain.BaseDirectory, "installer.cfg");

        public MainForm()
        {
            InitializeComponent();
            LoadSavedPath();
        }

        private void LoadSavedPath()
        {
            try
            {
                if (File.Exists(ConfigPath))
                {
                    string saved = File.ReadAllText(ConfigPath).Trim();
                    if (!string.IsNullOrEmpty(saved))
                        txtPath.Text = saved;
                }
            }
            catch { /* silencieux */ }
        }

        private void SavePath(string path)
        {
            try { File.WriteAllText(ConfigPath, path); }
            catch { /* silencieux */ }
        }

        // ════════════════════════════════════════════════════════════════
        //  UI SETUP
        // ════════════════════════════════════════════════════════════════
        private void InitializeComponent()
        {
            this.Text            = "Dead Cells Archipelago Installer";
            this.Size            = new Size(620, 480);
            this.MinimumSize     = new Size(620, 480);
            this.StartPosition   = FormStartPosition.CenterScreen;
            this.BackColor       = Color.FromArgb(22, 22, 30);
            this.ForeColor       = Color.White;
            this.Font            = new Font("Segoe UI", 9.5f);

            // Title
            lblTitle = new Label
            {
                Text      = "Dead Cells · Archipelago Installer",
                Font      = new Font("Segoe UI", 14f, FontStyle.Bold),
                ForeColor = Color.FromArgb(220, 80, 60),
                AutoSize  = true,
                Location  = new Point(20, 18)
            };

            // Path label
            lblPath = new Label
            {
                Text      = "Path to deadcells.exe :",
                AutoSize  = true,
                Location  = new Point(20, 65),
                ForeColor = Color.FromArgb(180, 180, 190)
            };

            // Path text box
            txtPath = new TextBox
            {
                Location  = new Point(20, 85),
                Width     = 480,
                BackColor = Color.FromArgb(35, 35, 45),
                ForeColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Browse button
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

            // Install button
            btnInstall = new Button
            {
                Text      = "Install/Update and Launch",
                Location  = new Point(20, 120),
                Width     = 570,
                Height    = 36,
                BackColor = Color.FromArgb(180, 50, 40),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font      = new Font("Segoe UI", 10f, FontStyle.Bold),
                Cursor    = Cursors.Hand
            };
            btnInstall.FlatAppearance.BorderSize = 0;
            btnInstall.Click += BtnInstall_Click;

            // Progress bar
            progressBar = new ProgressBar
            {
                Location = new Point(20, 168),
                Width    = 570,
                Height   = 16,
                Minimum  = 0,
                Maximum  = 100,
                Value    = 0,
                Style    = ProgressBarStyle.Continuous
            };

            // Status label
            lblStatus = new Label
            {
                Text      = "Waiting…",
                AutoSize  = false,
                Location  = new Point(20, 190),
                Width     = 570,
                ForeColor = Color.FromArgb(150, 150, 160)
            };

            // Log box
            rtbLog = new RichTextBox
            {
                Location   = new Point(20, 215),
                Width      = 570,
                Height     = 210,
                BackColor  = Color.FromArgb(12, 12, 18),
                ForeColor  = Color.FromArgb(180, 220, 180),
                ReadOnly   = true,
                Font       = new Font("Consolas", 8.5f),
                BorderStyle = BorderStyle.FixedSingle,
                ScrollBars = RichTextBoxScrollBars.Vertical
            };

            this.Controls.AddRange(new Control[] {
                lblTitle, lblPath, txtPath, btnBrowse,
                btnInstall, progressBar, lblStatus, rtbLog
            });
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
                SetStatus("Failed the installation");
            }
            finally
            {
                SetUiEnabled(true);
            }
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

            string fileName = Path.GetFileName(raw);
            if (!fileName.Equals("deadcells.exe", StringComparison.OrdinalIgnoreCase))
            {
                Error("Path should point to deadcells.exe.");
                return false;
            }

            if (!File.Exists(raw))
            {
                Error("deadcells.exe not found with this path.");
                return false;
            }

            deadCellsDir = Path.GetDirectoryName(raw);
            SavePath(raw);
            return true;
        }

        // ════════════════════════════════════════════════════════════════
        //  INSTALLATION PIPELINE
        // ════════════════════════════════════════════════════════════════
        private async Task RunInstallation()
        {
            // ── STEP 1 : Check .NET 10 ──────────────────────────────────
            SetStatus("Check for .NET SDK 10…");
            Log("→ Check for .NET 10 SDK…");
            bool hasDotnet10 = CheckDotnet10();

            if (!hasDotnet10)
            {
                Log("  .NET 10 SDK not found. Downloading installer…");
                await InstallDotnet10();
                SetProgress(10);

                if (!CheckDotnet10())
                {
                    LogError("  Install of .NET 10 SDK failed. Cancelling.");
                    return;
                }
            }
            else
            {
                Log("  .NET 10 SDK already present. ✓");
            }
            SetProgress(10);

            // ── STEP 2 : Télécharger core (win-x64.zip) ─────────────────
            string coremodDir = Path.Combine(deadCellsDir, "coremod");
            string coreDir    = Path.Combine(coremodDir, "core");
            string corePs1    = Path.Combine(coreDir, "mdk", "install.ps1");

            bool coreAlreadyPresent = File.Exists(corePs1);

            if (coreAlreadyPresent)
            {
                Log("→ core already installed, step skipped. ✓");
                SetProgress(40);
            }
            else
            {
                SetStatus("Downloading core (win-x64.zip)…");
                Log("→ Recovering latest release of core on GitHub…");
                string coreZipUrl = await GetAssetUrl(CORE_API, "win-x64.zip");
                string coreZip    = Path.Combine(Path.GetTempPath(), "dc_core_win-x64.zip");

                await DownloadFile(coreZipUrl, coreZip, 10, 30,
                    "Downloading core…");

                SetStatus("Extract core…");
                Log("→ Extracted to " + coremodDir + "…");
                Directory.CreateDirectory(coremodDir);
                ExtractZip(coreZip, coremodDir);
                File.Delete(coreZip);
                Log("  Extraction ended. ✓");
                SetProgress(40);
            }

            // ── STEP 3 : Exécuter install.ps1 ───────────────────────────
            if (!File.Exists(corePs1))
            {
                LogError("  install.ps1 not found : " + corePs1);
                return;
            }

            string coremodDataDir = Path.Combine(coremodDir, "data");
            if (Directory.Exists(coremodDataDir))
            {
                Log("→ Folder coremod\\data already present, install.ps1 skipped. ✓");
                SetProgress(55);
            }
            else
            {
                SetStatus("Execute install.ps1…");
                Log("→ Run install.ps1…");
                await RunPowerShell(corePs1);
                Log("  install.ps1 ended. ✓");
                SetProgress(55);
            }

            // ── STEP 4 : Télécharger mods.zip si nécessaire ─────────────
            string modInfoPath = Path.Combine(
                coremodDir, "mods", "DeadCellsArchipelago", "modinfo.json");

            string localVersion  = ReadLocalModVersion(modInfoPath);
            string remoteVersion = await GetRemoteModVersion();
            Log($"→ Local version of Archipelago mod  : {(localVersion ?? "missing")}");
            Log($"  Latest version on GitHub : {remoteVersion}");

            if (localVersion == remoteVersion && localVersion != null)
            {
                Log("  Mod already up to date. ✓");
                SetProgress(90);
            }
            else
            {
                SetStatus("Dowloading mods.zip…");
                Log("→ Dowloading mods.zip…");
                string modZipUrl = await GetAssetUrl(MOD_API, "mods.zip");
                string modZip    = Path.Combine(Path.GetTempPath(), "dc_mods.zip");

                await DownloadFile(modZipUrl, modZip, 55, 85,
                    "Dowloading Archipelago mod…");

                SetStatus("Extraction of mods.zip…");
                Log("→ Extracting to " + coremodDir + "…");
                ExtractZip(modZip, coremodDir);
                File.Delete(modZip);
                Log("  Extraction ended. ✓");
                SetProgress(90);
            }

            // ── STEP 5 : Lancer le jeu ──────────────────────────────────
            string launcherExe = Path.Combine(
                coremodDir, "core", "host", "startup", "DeadCellsModding.exe");

            if (!File.Exists(launcherExe))
            {
                LogError("  Launcher not found : " + launcherExe);
                return;
            }

            SetStatus("Launching game…");
            Log("→ Starting DeadCellsModding.exe…");
            Process.Start(launcherExe);
            SetProgress(100);
            Log("  Installation ended and game lauched!");
            SetStatus("Installation ended!");
        }

        // ════════════════════════════════════════════════════════════════
        //  HELPERS – .NET 10
        // ════════════════════════════════════════════════════════════════
        // Chemins possibles de dotnet : PATH système + installation locale du user
        private System.Collections.Generic.IEnumerable<string> DotnetCandidates()
        {
            yield return "dotnet"; // via PATH
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
            // Télécharge le script officiel d'installation Microsoft
            string scriptUrl  = "https://dot.net/v1/dotnet-install.ps1";
            string scriptPath = Path.Combine(Path.GetTempPath(), "dotnet-install.ps1");

            Log("  Downloading installation script for .NET…");
            using (var client = NewHttpClient())
            {
                byte[] data = await client.GetByteArrayAsync(scriptUrl);
                File.WriteAllBytes(scriptPath, data);
            }

            string installDir = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
                "Microsoft", "dotnet");

            Log("  Installation Directory: " + installDir);
            Log("  Execute installer .NET 10 SDK…");
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
            throw new Exception($"Asset '{assetName}' not found in the GitHub release.");
        }

        private async Task<string> GetRemoteModVersion()
        {
            using (var client = NewHttpClient())
            {
                string json = await client.GetStringAsync(MOD_API);
                var obj = JObject.Parse(json);
                // tag_name est typiquement "v0.0.9" – on retire le "v" si présent
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
                    byte[] buf     = new byte[81920];
                    long   read    = 0;
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
                            string mb = (read / 1048576.0).ToString("0.0");
                            string mb2 = (total.Value / 1048576.0).ToString("0.0");
                            SetStatus($"{statusLabel} ({mb} / {mb2} Mo)");
                        }
                    }
                }
            }
            Log($"  File downloaded → {dest}");
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
                    string fullDest = Path.GetFullPath(
                        Path.Combine(destDir, entry.FullName));

                    // Sécurité : pas de path traversal
                    if (!fullDest.StartsWith(Path.GetFullPath(destDir),
                        StringComparison.OrdinalIgnoreCase))
                        continue;

                    if (string.IsNullOrEmpty(entry.Name)) // répertoire
                    {
                        Directory.CreateDirectory(fullDest);
                    }
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
                    throw new Exception("install.ps1 returned an error : "
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
                string json = File.ReadAllText(modInfoPath);
                var obj = JObject.Parse(json);
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
            btnInstall.Enabled = enabled;
            btnBrowse.Enabled  = enabled;
            txtPath.Enabled    = enabled;
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
            => MessageBox.Show(msg, "Erreur", MessageBoxButtons.OK, MessageBoxIcon.Warning);
    }
}
