using dc;
using dc.h2d;
using dc.h2d.col;
using dc.level.lore;
using dc.tool;
using dc.tool.weap.dual;
using dc.ui;
using dc.ui.hud;
using dc.ui.icon;
using dc.ui.pause;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ModAssetManager;

namespace DeadCellsArchipelago {
    public static class PauseMenuManager
    {
        public static DefaultPause? defaultPause;
        public static bool showClassicMenu { get; set; } = true;
        public static Bitmap? logoBitmap = null;
        public static bool changedMethodCall = false;
        public static bool changedMethodCallController = false;
        public static dc.ui.Text? apMenuButton = null;
        public static SkillShop skillShopMenu = new SkillShop(50, 150);
        public static Bitmap? cellBitmap = null;
        public static dc.ui.Text? cellsNumber = null;
        public static int shopPrice = 100;
        public static SkillScroller<ItemLine>? scrollerFiller;
        public static SkillScroller<BiomeLine>? scrollerBiome;
        public static PopUpTracker? popUpTracker;
        public static bool showPopUp;
        public static SkillScroller<LogLine>? scrollerHistory;
        public static dc.ui.Text? shopTitle = null;
        public static dc.ui.Text? historyTitle = null;
        public static dc.ui.Text? biomeTitle = null;
        public static dc.ui.Text? fillerTitle = null;
        public static dc.ui.Text? menuTitle = null;

        

        public static void OnUpdateDefaultPause(Hook_DefaultPause.orig_update orig, DefaultPause self)
        {
            defaultPause = self;
            orig(self);

            ActualiseVanillaMenu(self);
            AddMenuButton(self);

            AddCellsCount(self);

            AddIncolorMenu(self);
            AddFillerMenu(self);
            AddBiomeMenu(self);
            AddHistoryMenu(self);
            AddTitles(self);

            AddPopUpMenu(self);
        }

        public static void ActualiseVanillaMenu(DefaultPause self)
        {
            self.title.visible = showClassicMenu;

            self.weaLeft.visible = showClassicMenu;
            self.arrowTopWea.visible = showClassicMenu;
            self.ciSwapWea.visible = showClassicMenu;
            self.arrowBotWea.visible = showClassicMenu;
            self.weaRight.visible = showClassicMenu;

            self.skillLeft.visible = showClassicMenu;
            self.arrowTopSki.visible = showClassicMenu;
            self.ciSwapSki.visible = showClassicMenu;
            self.arrowBotSki.visible = showClassicMenu;
            self.skillRight.visible = showClassicMenu;

            self.amulet.visible = showClassicMenu;
            self.backpackBox?.visible = showClassicMenu;
            self.backpackFlow?.visible = showClassicMenu;
            self.fbPerks.visible = showClassicMenu;
            self.flowPerks.visible = showClassicMenu;
            
            self.botMenu.visible = showClassicMenu;
            self.bg.botGradient.visible = showClassicMenu;
            self.selection.visible = showClassicMenu;

            self.locked = !showClassicMenu;
        }

        private static void AddMenuButton(DefaultPause self)
        {
            if (!changedMethodCall)
            {
                changedMethodCall = true;
                HlAction previousAction = self.uponClosing;
                self.uponClosing = () =>
                {
                    previousAction.Invoke();
                    ResetUI();
                };
            }

            if (!changedMethodCallController)
            {
                changedMethodCallController = true;
                HlAction<int, bool> previousAct = self.controller.onActPressed;
                self.controller.onActPressed = (int i, bool b) =>
                {
                    if(showPopUp && i == 8)
                    {
                        showPopUp = false;
                    }
                    else if(!showClassicMenu && i == 8)
                    {
                        showClassicMenu = true;
                    }
                    else
                    {
                        previousAct.Invoke(i, b);
                    }
                };
            }

            if (logoBitmap == null)
            {
                var logoTile = archipelagoLogoTile.clone();

                logoBitmap = new Bitmap(logoTile, self.bg)
                {
                    x = 1400,
                    y = 10,
                    scaleX = 0.015,
                    scaleY = 0.015,
                };
            }
            
            if (apMenuButton == null)
            {
                Bounds boundsLogo = logoBitmap.getSize(new Bounds());
                double scale = 1;
                apMenuButton = new dc.ui.Text(self.bg, true, false, new Ref<double>(ref scale), null, null)
                {
                    x = logoBitmap.x + boundsLogo.xMax
                };
                apMenuButton.set_text("Switch Menu".AsHaxeString());
                apMenuButton.y = logoBitmap.y + ((boundsLogo.yMax - apMenuButton.textHeight) /2);
                apMenuButton.set_textColor(16777215);
                var inter = new Interactive(
                    boundsLogo.xMax + apMenuButton.get_textWidth(),
                    boundsLogo.yMax,
                    apMenuButton,
                    null
                )
                {
                    x = -boundsLogo.xMax,
                    y = -(boundsLogo.yMax - apMenuButton.textHeight) /2,

                    onClick = (e) =>
                    {
                        showClassicMenu = !showClassicMenu;
                    },
                    onMove = (e) =>
                    {
                        apMenuButton.set_textColor(16776960);
                    },
                    onOut = (e) =>
                    {
                        apMenuButton.set_textColor(16777215);
                    }
                };
            }
        }

        private static void AddCellsCount(DefaultPause self)
        {
            if (HERO != null)
            {
                if (cellBitmap == null)
                {
                    int frame = 0;
                    double XY = 0;
                    var logoTile = Assets.Class.gameElements.getTile("cell".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);

                    cellBitmap = new Bitmap(logoTile, self.bg)
                    {
                        x = 50,
                        y = 40,
                    };
                }
                
                if (cellsNumber == null)
                {
                    Bounds boundsLogo = cellBitmap.getSize(new Bounds());
                    double scale = 1;
                    cellsNumber = new dc.ui.Text(self.bg, true, false, new Ref<double>(ref scale), null, null)
                    {
                        x = cellBitmap.x + boundsLogo.xMax
                    };
                    cellsNumber.set_text($" {HERO.cells}".AsHaxeString());
                    cellsNumber.y = cellBitmap.y + ((boundsLogo.yMax - cellsNumber.textHeight) /2);
                    cellsNumber.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));
                }
            }

            cellBitmap?.visible = !showClassicMenu;
            cellsNumber?.visible = !showClassicMenu;
        }

        private static void AddIncolorMenu(DefaultPause self)
        {
            skillShopMenu.AddIncolorWeapons(self, false);
            skillShopMenu.AddIncolorSkills(self, false);

            skillShopMenu.SetVisible(!showClassicMenu);
            
        }

        private static void AddFillerMenu(DefaultPause self) {
            if (scrollerFiller == null)
            {
                scrollerFiller = new SkillScroller<ItemLine>(50, 550, self.bg, 500, true);
                scrollerFiller.Refresh(10);

                Dictionary<string, int> ids = CalculateDiffFiller();

                scrollerFiller.SetContentItemLine(ids, 660257);
            }
            scrollerFiller.SetVisible(!showClassicMenu);
        }

        private static void AddBiomeMenu(DefaultPause self) {
            if (scrollerBiome == null)
            {
                scrollerBiome = new SkillScroller<BiomeLine>(800, 150, self.bg, 900, true);
                scrollerBiome.Refresh(25);
                scrollerBiome.SetContentBiomeLine();
            }
            scrollerBiome.SetVisible(!showClassicMenu);
        }

        private static void AddPopUpMenu(DefaultPause self) {
            if (popUpTracker == null)
            {
                popUpTracker = new PopUpTracker(self.bg);
                showPopUp = false;
                popUpTracker.AddFillerMenu();
            }
            popUpTracker.SetVisible(showPopUp && !showClassicMenu);
        }

        private static void AddHistoryMenu(DefaultPause self) {
            if (scrollerHistory == null)
            {
                scrollerHistory = new SkillScroller<LogLine>(350, 150, self.bg, 265, false);
                scrollerHistory.Refresh(10);

                scrollerHistory.SetContentLogLine(History, 660257);
                scrollerHistory.SetScrollAtEnd();
            }
            scrollerHistory.SetVisible(!showClassicMenu);
        }

        private static void AddTitles(DefaultPause self) {
            if (shopTitle == null)
            {
                double scale = 1;
                shopTitle = new dc.ui.Text(self.bg, false, true, new Ref<double>(ref scale), null, null);
                shopTitle.set_text("Colorless Shop".AsHaxeString());
                CenterX(250, shopTitle);
                shopTitle.x += 50;
                shopTitle.y = 80;

                historyTitle = new dc.ui.Text(self.bg, false, true, new Ref<double>(ref scale), null, null);
                historyTitle.set_text("History".AsHaxeString());
                if (scrollerHistory != null && scrollerHistory.mask != null)
                {
                    CenterX(400, historyTitle);
                    historyTitle.x += scrollerHistory.mask.x;
                }
                historyTitle.y = 80;

                biomeTitle = new dc.ui.Text(self.bg, false, true, new Ref<double>(ref scale), null, null);
                biomeTitle.set_text("Biomes".AsHaxeString());
                if (scrollerBiome != null && scrollerBiome.mask != null)
                {
                    CenterX(scrollerBiome.mask.width, biomeTitle);
                    biomeTitle.x += scrollerBiome.mask.x;
                }
                biomeTitle.y = 80;

                fillerTitle = new dc.ui.Text(self.bg, false, true, new Ref<double>(ref scale), null, null);
                fillerTitle.set_text("Filler Inventory".AsHaxeString());
                if (scrollerFiller != null && scrollerFiller.mask != null)
                {
                    CenterX(700, fillerTitle);
                    fillerTitle.x += scrollerFiller.mask.x;
                }
                fillerTitle.y = 480;

                menuTitle = new dc.ui.Text(self.bg, false, true, new Ref<double>(ref scale), null, null);
                menuTitle.set_text("ARCHIPELAGO MENU".AsHaxeString());
                CenterX(self.bg, menuTitle);
                menuTitle.y = self.title.y;
            }
            shopTitle?.visible = !showClassicMenu;
            historyTitle?.visible = !showClassicMenu;
            biomeTitle?.visible = !showClassicMenu;
            fillerTitle?.visible = !showClassicMenu;
            menuTitle?.visible = !showClassicMenu;
        }

        public static void UpdateTopPopUp() {
            if (popUpTracker != null)
            {
                popUpTracker.UpdateTopContent();
            }
        }
        public static void UpdateScrollContent(HashSet<string> itemIds) {
            if (popUpTracker != null)
            {
                popUpTracker.UpdateScrollContent(itemIds);
            }
        }

        public static void ResetUI()
        {
            logoBitmap = null;
            changedMethodCall = false;
            apMenuButton = null;
            skillShopMenu.Reset();
            cellBitmap = null;
            cellsNumber = null;
            scrollerFiller = null;
            scrollerBiome = null;
            popUpTracker = null;
            showPopUp = false;
            scrollerHistory = null;
            shopTitle = null;
            historyTitle = null;
            biomeTitle = null;
            fillerTitle = null;
            menuTitle = null;
        }

        public static void OnSwapWeaponsApMenu(Hook_Inventory.orig_swapWeapons orig, Inventory self)
        {
            skillShopMenu.SwapWeaponsApMenu(orig, self);
        }

        public static void OnSwapSkillsApMenu(Hook_Inventory.orig_swapSkills orig, Inventory self)
        {
            skillShopMenu.SwapSkillsApMenu(orig, self);
        }

        public static Dictionary<string, int> CalculateDiffFiller()
        {
            Dictionary<string, int> res = new Dictionary<string, int>();
            if (SAVED_DATA == null) return res;

            foreach (KeyValuePair<string, int> item in SAVED_DATA.ReceivedFillerItem)
            {
                if (!(item.Key.Length >= 5 && item.Key[..5] == "Trap_"))
                {
                    if (SAVED_DATA.GivenFillerItem.ContainsKey(item.Key) && item.Value - SAVED_DATA.GivenFillerItem[item.Key] != 0)
                    {
                        res[item.Key] = item.Value - SAVED_DATA.GivenFillerItem[item.Key];
                    }
                    else if (!SAVED_DATA.GivenFillerItem.ContainsKey(item.Key))
                    {
                        res[item.Key] = item.Value;
                    }
                }
            }

            return res;
        }
    }
}