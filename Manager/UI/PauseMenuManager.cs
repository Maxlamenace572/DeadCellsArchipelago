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

namespace DeadCellsArchipelago {
    public static class PauseMenuManager
    {
        public static DefaultPause? defaultPause;
        public static bool showClassicMenu { get; set; } = true;
        public static Bitmap? logoBitmap = null;
        public static bool changedMethodCall = false;
        public static dc.ui.Text? apMenuButton = null;
        public static SkillShopSlot buttonWeapon1 = new SkillShopSlot();
        public static SkillShopSlot buttonWeapon2 = new SkillShopSlot();
        public static SkillShopSlot buttonSkill1 = new SkillShopSlot();
        public static SkillShopSlot buttonSkill2 = new SkillShopSlot();
        public static Bitmap? cellBitmap = null;
        public static dc.ui.Text? cellsNumber = null;
        public static int shopPrice = 400;
        public static SkillScroller<ItemLine>? scrollerFiller;

        

        public static void OnUpdateDefaultPause(Hook_DefaultPause.orig_update orig, DefaultPause self)
        {
            defaultPause = self;
            orig(self);

            ActualiseVanillaMenu(self);
            AddMenuButton(self);

            AddCellsCount(self);
            AddIncolorMenu(self);
            AddFillerMenu(self);
            
            
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

            if (logoBitmap == null)
            {
                var logoTile = LoadTileFromPng(GetResPath("logo.png"));

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
                        x = 700,
                        y = 10,
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
            AddIncolorWeapons(self, false);
            AddIncolorSkills(self, false);

            buttonWeapon1.SetVisible(!showClassicMenu);
            buttonWeapon2.SetVisible(!showClassicMenu);
            buttonSkill1.SetVisible(!showClassicMenu);
            buttonSkill2.SetVisible(!showClassicMenu);
            
        }

        private static void AddIncolorWeapons(DefaultPause self, bool invert)
        {
            if(!invert)
            {
                buttonWeapon1.InitButton(self, 100, 100, () => HERO?.inventory.getEquippedWeaponOn(0), self.weaLeft);
                buttonWeapon2.InitButton(self, 250, 100, () => HERO?.inventory.getEquippedWeaponOn(1), self.weaRight);
            }
            else
            {
                buttonWeapon1.InitButton(self, 100, 100, () => HERO?.inventory.getEquippedWeaponOn(1), self.weaLeft);
                buttonWeapon2.InitButton(self, 250, 100, () => HERO?.inventory.getEquippedWeaponOn(0), self.weaRight);
            }
            
        }

        private static void AddIncolorSkills(DefaultPause self, bool invert)
        {
            if(!invert)
            {
                buttonSkill1.InitButton(self, 250, 250, () => HERO?.inventory.getActiveOn(0), self.skillRight);
                buttonSkill2.InitButton(self, 100, 250, () => HERO?.inventory.getActiveOn(1), self.skillLeft);
            }
            else
            {
                buttonSkill1.InitButton(self, 250, 250, () => HERO?.inventory.getActiveOn(1), self.skillRight);
                buttonSkill2.InitButton(self, 100, 250, () => HERO?.inventory.getActiveOn(0), self.skillLeft);
            }
        }

        private static void AddFillerMenu(DefaultPause self) {
            if (scrollerFiller == null)
            {
                scrollerFiller = new SkillScroller<ItemLine>(50, 550, self.bg, 450);
                scrollerFiller.Refresh();

                List<string> ids = new List<string>();
                for (int i = 0; i < 20; i++) {
                    ids.Add($"Gardener{(i%4)+1}");
                }
                scrollerFiller.SetContentItemLine(ids);
            }
            scrollerFiller.SetVisible(!showClassicMenu);
        }

        public static void ResetUI()
        {
            logoBitmap = null;
            changedMethodCall = false;
            apMenuButton = null;
            buttonWeapon1.Reset();
            buttonWeapon2.Reset();
            buttonSkill1.Reset();
            buttonSkill2.Reset();
            cellBitmap = null;
            cellsNumber = null;
            scrollerFiller = null;
        }

        public static void OnSwapWeaponsApMenu(Hook_Inventory.orig_swapWeapons orig, Inventory self)
        {
            buttonWeapon1.Reset();
            buttonWeapon2.Reset();
            if (defaultPause != null) AddIncolorWeapons(defaultPause, true);
            orig(self);
        }

        public static void OnSwapSkillsApMenu(Hook_Inventory.orig_swapSkills orig, Inventory self)
        {
            buttonSkill1.Reset();
            buttonSkill2.Reset();
            if (defaultPause != null) AddIncolorSkills(defaultPause, true);
            orig(self);
        }
    }
}