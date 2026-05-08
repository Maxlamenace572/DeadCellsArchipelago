using dc.h2d;
using dc.h2d.col;
using dc.ui;
using dc.ui.pause;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public static class PauseMenuManager
    {
        public static bool showClassicMenu { get; set; } = true;
        public static Bitmap? logoBitmap = null;
        public static bool changedMethodCall = false;
        public static dc.ui.Text? apMenuButton = null;

        public static void OnUpdateDefaultPause(Hook_DefaultPause.orig_update orig, DefaultPause self)
        {
            orig(self);

            ActualiseMenu(self);

            if (!changedMethodCall)
            {
                changedMethodCall = true;
                HlAction previousAction = self.uponClosing;
                self.uponClosing = () =>
                {
                    previousAction.Invoke();
                    logoBitmap = null;
                    changedMethodCall = false;
                    apMenuButton = null;
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

        public static void ActualiseMenu(DefaultPause self)
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
            self.backpackBox.visible = showClassicMenu;
            self.backpackFlow.visible = showClassicMenu;
            self.fbPerks.visible = showClassicMenu;
            self.flowPerks.visible = showClassicMenu;
            
            self.botMenu.visible = showClassicMenu;
            self.bg.botGradient.visible = showClassicMenu;
            self.selection.visible = showClassicMenu;

            self.locked = !showClassicMenu;
        }
    }
}