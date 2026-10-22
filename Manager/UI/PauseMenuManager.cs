using dc;
using dc.h2d;
using dc.h2d.col;
using dc.tool;
using dc.ui.pause;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;
using dc.cine;

using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ModAssetManager;
using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.WorldMapManager;
using static DeadCellsArchipelago.RoomManager;

namespace DeadCellsArchipelago {
    public static class PauseMenuManager
    {
        public static Bitmap? screenBitmap = null;
        public static DefaultPause? defaultPause;
        public static FocusManager? focusManager = null;
        public static TopApMenu? topMenu = null;
        public static HlAction? modifiedUponClosing;
        public static bool changedMethodCallController = false;
        public static SkillShop skillShopMenu = new SkillShop(50, 150);
        public static Bitmap? cellBitmap = null;
        public static dc.ui.Text? cellsNumber = null;
        public static int colorlessShopPrice = 100;
        public static int pokebombShopPrice = 50;
        public static int legendaryShopPrice = 600;
        public static SkillScroller<ItemLine>? scrollerFiller;
        public static SkillScroller<BiomeLine>? scrollerBiome;
        public static PopUpTracker? popUpTracker;
        public static PopUpItemDesc? popUpItemDesc;
        public static SkillScroller<LogLine>? scrollerHistory;
        public static dc.ui.Text? shopTitle = null;
        public static dc.ui.Text? historyTitle = null;
        public static dc.ui.Text? biomeTitle = null;
        public static dc.ui.Text? fillerTitle = null;
        public static dc.ui.Text? menuTitle = null;
        public static int keyToRepeat = -1;
        private const long RepeatIntervalMs = 166; //around 10 frames at 60 fps
        private static long lastRepeatTimestamp = 0;
        public static HlAction<int, bool>? modifiedOnActPressed;
        public static dc.ui.Text? energyTitle = null;
        public static EnergyLink? energyLink = null;
        public static string? warpToBiome = null;
        public static bool isReload = false;

        public static void InitializePauseHooks()
        {
            Log.Information("[AP] Loading Pause Hooks...");

            Hook_DefaultPause.update += OnUpdateDefaultPause;
            Hook_Inventory.swapWeapons += OnSwapWeaponsApMenu;
            Hook_Inventory.swapSkills += OnSwapSkillsApMenu;

            Log.Information("[AP] Pause Hooks loaded");
        }

        private static void OnUpdateDefaultPause(Hook_DefaultPause.orig_update orig, DefaultPause self)
        {
            defaultPause = self;
            orig(self);

            AddFocusManager();
            ActualiseVanillaMenu(self);
            DefineScreenSize(self);
            AddMenuButton(self);

            AddCellsCount();

            AddIncolorMenu(self);
            AddFillerMenu();
            AddBiomeMenu();
            AddHistoryMenu();
            AddTitles(self);

            AddPopUpMenu();
            AddDescriptionMenu();
            AddEnergyLinkMenu();

            AddMenuInterractions();

            MoveCursor(self);
        }

        public static void ActualiseVanillaMenu(DefaultPause self)
        {
            self.title.visible = ShowClassicMenu();

            self.weaLeft.visible = ShowClassicMenu();
            self.arrowTopWea.visible = ShowClassicMenu();
            self.ciSwapWea.visible = ShowClassicMenu();
            self.arrowBotWea.visible = ShowClassicMenu();
            self.weaRight.visible = ShowClassicMenu();

            self.skillLeft.visible = ShowClassicMenu();
            self.arrowTopSki.visible = ShowClassicMenu();
            self.ciSwapSki.visible = ShowClassicMenu();
            self.arrowBotSki.visible = ShowClassicMenu();
            self.skillRight.visible = ShowClassicMenu();

            self.amulet.visible = ShowClassicMenu();
            self.backpackBox?.visible = ShowClassicMenu();
            self.backpackFlow?.visible = ShowClassicMenu();
            self.fbPerks.visible = ShowClassicMenu();
            self.flowPerks.visible = ShowClassicMenu();
            
            self.botMenu.visible = ShowClassicMenu();
            self.bg.botGradient.visible = ShowClassicMenu();
            self.selection.visible = ShowClassicMenu() && !focusManager!.focusModEnabled;

            self.locked = !ShowClassicMenu() || focusManager!.focusModEnabled;
        }

        private static bool ShowClassicMenu()
        {
            return focusManager!.page == 0;
        }

        private static void DefineScreenSize(DefaultPause self)
        {
        if (screenBitmap == null)
            {
                Tile screenTile = VoidBackground1080Tile.clone();

                screenBitmap = new Bitmap(screenTile, self.bg)
                {
                    scaleX = screenScale,
                    scaleY = screenScale
                };
            }
        }

        private static void AddFocusManager()
        {
            if (focusManager == null)
            {
                focusManager = new FocusManager(new FocusItem());
            }
        }

        private static void AddMenuButton(DefaultPause self)
        {
            if (modifiedUponClosing == null)
            {
                HlAction previousAction = self.uponClosing;
                modifiedUponClosing = () =>
                {
                    previousAction.Invoke();
                    ResetUI();
                };
            }
            self.uponClosing = modifiedUponClosing;

            if (!changedMethodCallController)
            {
                changedMethodCallController = true;
                HlAction<int, bool> previousAct = self.controller.onActPressed;
                self.controller.onActPressed = (int i, bool b) =>
                {
                    //continue input up/left/down/right when down
                    lastRepeatTimestamp = Environment.TickCount64;
                    if (i == 10 || i == 11 || i == 12 || i == 13 || i == 0) keyToRepeat = i;
                    else keyToRepeat = -1;

                    if (focusManager != null && ((!focusManager.focusModEnabled && i == 10) || focusManager.focusModEnabled))
                        focusManager.Controller(i);
                    else
                        previousAct.Invoke(i, b);
                };
                modifiedOnActPressed = self.controller.onActPressed;
            }

            if (topMenu == null)
            {
                topMenu = new TopApMenu(screenBitmap!, focusManager!);
            }
            topMenu.ActualiseTopMenu();
        }

        private static void AddCellsCount()
        {
            if (HERO != null)
            {
                if (cellBitmap == null)
                {
                    int frame = 0;
                    double XY = 0;
                    var logoTile = Assets.Class.gameElements.getTile("cell".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);

                    cellBitmap = new Bitmap(logoTile, screenBitmap)
                    {
                        x = 50,
                        y = 40,
                    };
                }
                
                if (cellsNumber == null)
                {
                    Bounds boundsLogo = cellBitmap.getSize(new Bounds());
                    double scale = 3/textPixelScale;
                    cellsNumber = new dc.ui.Text(screenBitmap, true, false, new Ref<double>(ref scale), null, null)
                    {
                        x = cellBitmap.x + boundsLogo.xMax,
                        scaleX = textBaseScale * scale,
                        scaleY = textBaseScale * scale
                    };
                    cellsNumber.set_text($" {HERO.cells}".AsHaxeString());
                    CenterYTextTo(cellBitmap, cellsNumber, 46);
                    cellsNumber.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));
                }
            }

            cellBitmap?.visible = !ShowClassicMenu();
            cellsNumber?.visible = !ShowClassicMenu();
        }

        private static void AddIncolorMenu(DefaultPause self)
        {
            if(screenBitmap == null) return;
            skillShopMenu.AddIncolorWeapons(screenBitmap, self, false);
            skillShopMenu.AddIncolorSkills(screenBitmap, self, false);

            skillShopMenu.SetVisible(focusManager!.page == 1);
            
        }

        private static void AddFillerMenu() {
            if(screenBitmap == null) return;
            if (scrollerFiller == null)
            {
                scrollerFiller = new SkillScroller<ItemLine>(50, 550, screenBitmap, 500, true, true, false);
                scrollerFiller.Refresh(10);

                Dictionary<string, int> ids = CalculateDiffFiller();

                scrollerFiller.SetContentItemLine(ids, (int) APColor.DeepBlue);
            }
            scrollerFiller.SetVisible(focusManager!.page == 1);
        }

        private static void AddBiomeMenu() {
            if(screenBitmap == null) return;
            if (scrollerBiome == null)
            {
                scrollerBiome = new SkillScroller<BiomeLine>(800, 150, screenBitmap, 900, true, true, true);
                scrollerBiome.Refresh(25);
                scrollerBiome.SetContentBiomeLine();
            }
            scrollerBiome.SetVisible(focusManager!.page == 1);
        }

        private static void AddPopUpMenu() {
            if(screenBitmap == null) return;
            if (popUpTracker == null)
            {
                popUpTracker = new PopUpTracker(screenBitmap);
                popUpTracker.AddFillerMenu();
            }
            popUpTracker.SetVisible(focusManager!.page == 1 && (focusManager!.popUp == 1 || focusManager!.popUp == 2));
        }

        private static void AddDescriptionMenu() {
            if(screenBitmap == null) return;
            if (popUpItemDesc == null)
            {
                popUpItemDesc = new PopUpItemDesc(screenBitmap);
            }
            popUpItemDesc.SetVisible(focusManager!.page == 1 && focusManager!.popUp == 2);
        }

        private static void AddHistoryMenu() {
            if(screenBitmap == null) return;
            if (scrollerHistory == null)
            {
                scrollerHistory = new SkillScroller<LogLine>(350, 150, screenBitmap, 265, false, true, false);
                scrollerHistory.Refresh(10);

                scrollerHistory.SetContentLogLine(History, (int) APColor.DeepBlue);
                scrollerHistory.SetScrollAtEnd();
            }
            scrollerHistory.SetVisible(focusManager!.page == 1);
        }

        private static void AddTitles(DefaultPause self) {
            if(screenBitmap == null) return;
            if (shopTitle == null)
            {
                double scale = 3/textPixelScale;
                shopTitle = new dc.ui.Text(screenBitmap, false, true, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                shopTitle.set_text("Special Shop".AsHaxeString());
                CenterX(250, shopTitle);
                shopTitle.x += 50;
                shopTitle.y = 80;

                energyTitle = new dc.ui.Text(screenBitmap, false, true, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                energyTitle.set_text("Energy Link".AsHaxeString());
                CenterX(250, energyTitle);
                energyTitle.x += 50;
                energyTitle.y = 80;

                historyTitle = new dc.ui.Text(screenBitmap, false, true, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                historyTitle.set_text("History".AsHaxeString());
                if (scrollerHistory != null && scrollerHistory.mask != null)
                {
                    CenterX(400, historyTitle);
                    historyTitle.x += scrollerHistory.mask.x;
                }
                historyTitle.y = 80;

                biomeTitle = new dc.ui.Text(screenBitmap, false, true, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                biomeTitle.set_text("Biomes".AsHaxeString());
                if (scrollerBiome != null && scrollerBiome.mask != null)
                {
                    CenterX(scrollerBiome.mask.width, biomeTitle);
                    biomeTitle.x += scrollerBiome.mask.x;
                }
                biomeTitle.y = 80;

                fillerTitle = new dc.ui.Text(screenBitmap, false, true, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                fillerTitle.set_text("Filler Inventory".AsHaxeString());
                if (scrollerFiller != null && scrollerFiller.mask != null)
                {
                    CenterX(700, fillerTitle);
                    fillerTitle.x += scrollerFiller.mask.x;
                }
                fillerTitle.y = 480;

                menuTitle = new dc.ui.Text(screenBitmap, false, true, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                menuTitle.set_text("ARCHIPELAGO MENU".AsHaxeString());
                CenterX(1920, menuTitle);
                menuTitle.y = self.title.y / screenScale;
            }
            shopTitle?.visible = focusManager!.page == 1;
            historyTitle?.visible = focusManager!.page == 1;
            biomeTitle?.visible = focusManager!.page == 1;
            fillerTitle?.visible = focusManager!.page == 1;
            menuTitle?.visible = focusManager!.page == 1;

            energyTitle?.visible = focusManager!.page == 2;
        }

        public static void UpdateTopPopUp() {
            if (popUpTracker != null)
            {
                popUpTracker.UpdateTopContent();
                popUpTracker.UpdateWarpButton();
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
            screenBitmap = null;
            focusManager = null;
            topMenu = null;
            skillShopMenu.Reset();
            cellBitmap = null;
            cellsNumber = null;
            scrollerFiller = null;
            scrollerBiome = null;
            popUpTracker = null;
            popUpItemDesc = null;
            scrollerHistory = null;
            shopTitle = null;
            historyTitle = null;
            biomeTitle = null;
            fillerTitle = null;
            menuTitle = null;
            energyTitle = null;
            energyLink = null;
        }

        private static void OnSwapWeaponsApMenu(Hook_Inventory.orig_swapWeapons orig, Inventory self)
        {
            skillShopMenu.SwapWeaponsApMenu(orig, self);
        }

        private static void OnSwapSkillsApMenu(Hook_Inventory.orig_swapSkills orig, Inventory self)
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

                    if (GLOBAL_DATA!.flawlessScrolls && item.Key == "AllUp" && GLOBAL_DATA!.FlawlessBoss.Any())
                    {
                        if (!res.ContainsKey(item.Key)) res[item.Key] = 0;
                        res[item.Key] += GLOBAL_DATA!.FlawlessBoss.Count();
                        if (res[item.Key] == 0) res.Remove(item.Key);
                    }
                }
            }

            return res;
        }

        private static void MoveCursor(DefaultPause self)
        {
            if (keyToRepeat != -1 && self.controller != null && self.controller.isAnyActionDown())
            {
                if (keyToRepeat != 0 || focusManager!.currentFocus.canRepeatAct)
                {
                    long now = Environment.TickCount64;
                    if (now - lastRepeatTimestamp >= RepeatIntervalMs)
                    {
                        lastRepeatTimestamp = now;
                        modifiedOnActPressed?.Invoke(keyToRepeat, true);
                    }
                }
            }
        }

        private static void AddEnergyLinkMenu() {
            if(screenBitmap == null) return;
            if (energyLink == null)
            {
                energyLink = new EnergyLink(screenBitmap);
            }
            energyLink.SetVisible(focusManager!.page == 2);
        }

        public static void WarpSelected()
        {
            if (warpToBiome == null) return;
            if (!isReload)
            {
                SAVED_DATA!.ResetUps();
            }
            else
            {
                addBackLoreRooms = true;
                isReload = false;
            }
            LevelTransition.Class.@goto(warpToBiome.AsHaxeString());
            SAVED_DATA!.currentLevelId = warpToBiome;
            SAVED_DATA!.lastLevelDepthSeen = GetMapLevelDepth(warpToBiome);
            warpToBiome = null;
        }

        private static void AddMenuInterractions()
        {
            skillShopMenu.SetRight(scrollerHistory!);
            skillShopMenu.SetDown(scrollerFiller!);
            FocusItem.SetLeftRight(scrollerHistory!, scrollerBiome!);
            scrollerHistory!.down = scrollerFiller;
            scrollerFiller!.right = scrollerBiome;
            scrollerBiome!.up = topMenu!.menuButton;

            energyLink!.energyLinkMiddle.upButton.up = topMenu!.menuButton;
            energyLink!.energyLinkMiddle.downButton.up = topMenu!.menuButton;
        }
    }
}