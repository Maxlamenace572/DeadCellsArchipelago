using dc;
using dc.pr;
using dc.ui;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.HeroManager;
using static DeadCellsArchipelago.ModAssetManager;
using static DeadCellsArchipelago.RoomManager;
using Newtonsoft.Json;
using System.Text.Json;

namespace DeadCellsArchipelago {
    public static class MainMenuManager
    {
        public static dc.h2d.Object? apMenuContainer = null;
        public static Text? connectionStatus = null;
        public static dc.h2d.TextInput? serverIp = null;
        public static dc.h2d.TextInput? slotName = null;
        public static dc.h2d.TextInput? password = null;
        public static Text? connectButton = null;
        public static int loadDataInPlayMenu = 0;
        public static bool isOnMenu = false;
        public static Text? apVersion = null;
        public static string lastCompatibleApworld = "0.1.3";

        public static void OnMainMenu(Hook_TitleScreen.orig_mainMenu orig, TitleScreen self)
        {
            self.news.hidden = true;
            self.news.updateVisible();

            if (!isOnMenu)
            {
                ResetGameData();
                isOnMenu = true;
            }

            int menuScale = 3;
            if (apMenuContainer == null) {
                apMenuContainer = new dc.h2d.Object(self.root)
                {
                    x = dc.libs.Process.Class.CUSTOM_STAGE_WIDTH * 0.7,
                    y = dc.libs.Process.Class.CUSTOM_STAGE_HEIGHT * 0.05,
                };

                int frame = 0;
                double XY = 0;
                dc.h2d.Tile bgTileApMenu = Assets.Class.ui.getTile("walterWhite".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
                dc.h2d.Tile frameTileApMenu = Assets.Class.ui.getTile("boxLegendary".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
                dc.h2d.Tile logoTile = archipelagoLogoTile.clone();


                var bgApMenu = new dc.h2d.Bitmap(bgTileApMenu, apMenuContainer)
                {
                    scaleX = (113-4)*menuScale,
                    scaleY = (113-4)*menuScale,
                    x = 2*menuScale,
                    y = 2*menuScale,
                    color = ColorVectorRGBA(34, 34, 74, 1)
                };

                var apMenu = new dc.h2d.Bitmap(frameTileApMenu, apMenuContainer)
                {
                    scaleX = menuScale,
                    scaleY = menuScale
                };

                var logoBitmap = new dc.h2d.Bitmap(logoTile, apMenuContainer)
                {
                    x = -45,
                    y = -45,
                    scaleX = 0.08,
                    scaleY = 0.08,
                    alpha = 0.5
                };
            }


            int index = 0;
            if (connectionStatus == null) {
                double scale = 1;
                connectionStatus = new Text(apMenuContainer, false, false, new Ref<double>(ref scale), null, null)
                {
                    x = 10,
                    y = 10+40*index
                };
                index++;

                if (ARCHIPELAGO == null || ARCHIPELAGO.isConnected == false)
                {
                    connectionStatus.set_text("Not Connected".AsHaxeString());
                    connectionStatus.set_textColor(16711680);
                }
                else
                {
                    connectionStatus.set_text("Connected".AsHaxeString());
                    connectionStatus.set_textColor(2883371);
                    SetApworldVersion();
                }

            }


            if (serverIp == null) {
                double scale = 1;
                Text serverIpTag = new Text(apMenuContainer, false, false, new Ref<double>(ref scale), null, null)
                {
                    y = 10+40*index
                };
                index++;

                serverIpTag.set_text("Address:".AsHaxeString());
                serverIpTag.x = ((113-4)*menuScale - serverIpTag.textWidth) /2;

                serverIpTag.set_textColor(16777215);


                UIBox bgServerIp = UIBox.Class.drawBoxMain(270, 1, 4, 3, 0, null);
                bgServerIp.x = 18;
                bgServerIp.y = 40*index;
                bgServerIp.alpha = 0.85;
                bgServerIp.sg.color = ColorVectorRGBA(17*bgServerIp.alpha, 17*bgServerIp.alpha, 37*bgServerIp.alpha, 1);

                apMenuContainer.addChild(bgServerIp);

                serverIp = new dc.h2d.TextInput(connectionStatus.font, apMenuContainer)
                {
                    x = 18+6,
                    y = 2+40*index,
                    inputWidth = 284,
                    onMove = (e) =>
                    {
                        serverIp?.set_textColor(16776960);
                    },
                    onOut = (e) =>
                    {
                        serverIp?.set_textColor(16777215);
                    }
                };
                index++;
            }


            if (slotName == null) {
                double scale = 1;
                Text slotNameTag = new Text(apMenuContainer, false, false, new Ref<double>(ref scale), null, null)
                {
                    y = 10+40*index
                };
                index++;

                slotNameTag.set_text("Slot:".AsHaxeString());
                slotNameTag.x = ((113-4)*menuScale - slotNameTag.textWidth) /2;

                slotNameTag.set_textColor(16777215);


                UIBox bgSlotName = UIBox.Class.drawBoxMain(270, 1, 4, 3, 0, null);
                bgSlotName.x = 18;
                bgSlotName.y = 40*index;
                bgSlotName.alpha = 0.85;
                bgSlotName.sg.color = ColorVectorRGBA(17*bgSlotName.alpha, 17*bgSlotName.alpha, 37*bgSlotName.alpha, 1);

                apMenuContainer.addChild(bgSlotName);

                slotName = new dc.h2d.TextInput(connectionStatus.font, apMenuContainer)
                {
                    x = 18+6,
                    y = 2+40*index,
                    inputWidth = 284,
                    onMove = (e) =>
                    {
                        slotName?.set_textColor(16776960);
                    },
                    onOut = (e) =>
                    {
                        slotName?.set_textColor(16777215);
                    }
                };
                index++;
                slotName.set_text("test".AsHaxeString());
            }


            if (password == null) {
                double scale = 1;
                Text passwordTag = new Text(apMenuContainer, false, false, new Ref<double>(ref scale), null, null)
                {
                    y = 10+40*index
                };
                index++;

                passwordTag.set_text("Password:".AsHaxeString());
                passwordTag.x = ((113-4)*menuScale - passwordTag.textWidth) /2;

                passwordTag.set_textColor(16777215);


                UIBox bgPassword = UIBox.Class.drawBoxMain(270, 1, 4, 3, 0, null);
                bgPassword.x = 18;
                bgPassword.y = 40*index;
                bgPassword.alpha = 0.85;
                bgPassword.sg.color = ColorVectorRGBA(17*bgPassword.alpha, 17*bgPassword.alpha, 37*bgPassword.alpha, 1);

                apMenuContainer.addChild(bgPassword);

                password = new dc.h2d.TextInput(connectionStatus.font, apMenuContainer)
                {
                    x = 18+6,
                    y = 2+40*index,
                    inputWidth = 284,
                    onMove = (e) =>
                    {
                        password?.set_textColor(16776960);
                    },
                    onOut = (e) =>
                    {
                        password?.set_textColor(16777215);
                    }
                };
                index++;
            }

            if (connectButton == null) {
                double scale = 1;
                connectButton = new Text(apMenuContainer, false, true, new Ref<double>(ref scale), null, null)
                {
                    y = 40*index
                };
                index++;
                connectButton.set_text("Connect".AsHaxeString());
                connectButton.x = ((113-4)*menuScale - connectButton.textWidth) /2;
                connectButton.set_textColor(16777215);
                var inter = new dc.h2d.Interactive(
                    connectButton.get_textWidth(),
                    connectButton.get_textHeight(),
                    connectButton,
                    null
                )
                {
                    onClick = (e) =>
                    {
                        SaveFields();

                        if (ARCHIPELAGO != null)
                        {
                            ARCHIPELAGO.Disconnect();
                            ARCHIPELAGO = null;
                        }

                        var archipelago = new ArchipelagoManager();
                        archipelago.Connect(serverIp.text.ToString(), slotName.text.ToString(), password.text?.ToString());
                        if (archipelago.isConnected)
                        {
                            connectionStatus.set_text("Connected".AsHaxeString());
                            connectionStatus.set_textColor(2883371);
                            ARCHIPELAGO = archipelago;
                            SetApworldVersion();
                            
                            if (SAVED_DATA != null)
                            {
                                ARCHIPELAGO.SyncAll();
                            }
                        }
                        else
                        {
                            connectionStatus.set_text("Failed to Connect".AsHaxeString());
                            connectionStatus.set_textColor(16711680);
                            archipelago.Disconnect();
                        }
                    },
                    onMove = (e) =>
                    {
                        connectButton.set_textColor(16776960);
                    },
                    onOut = (e) =>
                    {
                        connectButton.set_textColor(16777215);
                    }
                };
            }

            SetValueFields();

            orig(self);
        }

        public static void OnOnResize(Hook_TitleScreen.orig_onResize orig, TitleScreen self)
        {
            orig(self);
            if (apMenuContainer != null)
            {
                apMenuContainer.x = dc.libs.Process.Class.CUSTOM_STAGE_WIDTH * 0.7;
                apMenuContainer.y = dc.libs.Process.Class.CUSTOM_STAGE_HEIGHT * 0.05;
            }
        }

        public static void OnPlayMenu(Hook_TitleScreen.orig_playMenu orig, TitleScreen self)
        {
            loadDataInPlayMenu = 1;
            orig(self);
            if(loadDataInPlayMenu != 0) loadDataInPlayMenu = 2;
            self.news.hidden = true;
            self.news.updateVisible();
        }

        public static void OnLaunchGame(Hook_Main.orig_launchGame orig, Main self, LaunchMode mode, bool? tpause, double? fadeOutS)
        {
            apMenuContainer = null;
            connectionStatus = null;
            serverIp = null;
            slotName = null;
            password = null;
            connectButton = null;
            isOnMenu = false;
            apVersion = null;
            orig(self, mode, tpause, fadeOutS);
        }

        private static void SetValueFields()
        {
            ConfData confData = GetConfData();
            serverIp?.set_text(confData.serverIp.AsHaxeString());
            slotName?.set_text(confData.slotName.AsHaxeString());
            password?.set_text(confData.password?.AsHaxeString());
        }

        private static void SaveFields()
        {
            if (serverIp != null && slotName != null && password != null)
            {
                ConfData confData = new ConfData()
                {
                    serverIp = serverIp.text.ToString(),
                    slotName = slotName.text.ToString(),
                    password = password.text.ToString(),
                };
                SaveConfData(confData);
            }
        }

        public static string GetConfFilePath()
        {
            return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data", "conf.json");
        }

        public static ConfData GetConfData()
        {
            var confPath = GetConfFilePath();
            var confData = new ConfData();
            if (File.Exists(confPath))
            {
                var json = File.ReadAllText(confPath);
                confData = JsonConvert.DeserializeObject<ConfData>(json) ?? new();
            }
            else
            {
                SaveConfData(confData);
            }
            return confData;
        }

        public static void SaveConfData(ConfData confData)
        {
            var json = JsonConvert.SerializeObject(confData, Formatting.Indented);
            File.WriteAllText(GetConfFilePath(), json);
        }

        public static bool OnSetVisible(Hook_LeaderboardPanel.orig_set_visible orig, LeaderboardPanel self, bool v)
        {
            return false;
        }

        private static void ResetGameData()
        {
            SAVED_DATA = null;
            bossRuneGivenSinceLaunch = 0;
            ProgressionItemGivenSinceLaunch = [];
            fillerItemGivenSinceLaunch = [];
            History = [];
            resetOnNextPrisonStart = false;
            levelMapChallenge = null;
        }

        private static void SetApworldVersion()
        {
            if (ARCHIPELAGO == null) return;
            if (apVersion == null) {
                double scale = 1;
                apVersion = new Text(apMenuContainer, false, false, new Ref<double>(ref scale), null, null)
                {
                    y = 10
                };
            }

            apVersion.set_text($"Apworld: {ARCHIPELAGO.version}".AsHaxeString());
            apVersion.x = ((113-4)*3) - apVersion.textWidth;
            apVersion.posChanged = true;
            if (TooOldApworld())
                apVersion.set_textColor(16711680);

            else if (FutureApworld())
                apVersion.set_textColor(16752934);

            else
                apVersion.set_textColor(2883371);
        }

        public static int Compare(string a, string b)
        {
            var (oldA, partsA) = Parse(a);
            var (oldB, partsB) = Parse(b);

            if (oldA != oldB)
                return oldA ? -1 : 1;

            int len = System.Math.Max(partsA.Length, partsB.Length);
            for (int i = 0; i < len; i++)
            {
                int pa = i < partsA.Length ? partsA[i] : 0;
                int pb = i < partsB.Length ? partsB[i] : 0;
                if (pa != pb)
                    return pa.CompareTo(pb);
            }
            return 0;
        }

        private static (bool isOld, int[] parts) Parse(string version)
        {
            if (string.IsNullOrWhiteSpace(version))
                throw new ArgumentException("Version vide ou nulle", nameof(version));

            bool isOld = version.StartsWith("-");
            string clean = isOld ? version.Substring(1) : version;

            var parts = clean.Split('.')
                            .Select(p => int.TryParse(p, out var n) ? n : 0)
                            .ToArray();

            return (isOld, parts);
        }

        public static bool TooOldApworld()
        {
            if (ARCHIPELAGO == null || ARCHIPELAGO.version == null) return true;
            return Compare(ARCHIPELAGO.version, lastCompatibleApworld) < 0;
        }

        public static bool FutureApworld()
        {
            string? modVersion = GetModVersion();
            if (ARCHIPELAGO == null || ARCHIPELAGO.version == null || modVersion == null) return true;
            return Compare(ARCHIPELAGO.version, modVersion) > 0;
        }

        public static string? GetModVersion()
        {
                var json = File.ReadAllText(GetModInfoFilePath());
                using JsonDocument document = JsonDocument.Parse(json);
                return document.RootElement.GetProperty("version").GetString();
        }

        public static string GetModInfoFilePath()
        {
            return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "modinfo.json");
        }
    }
}