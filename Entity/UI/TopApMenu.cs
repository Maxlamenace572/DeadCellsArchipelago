using dc.h2d;
using dc.h2d.col;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using static DeadCellsArchipelago.ModAssetManager;
using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class TopApMenu
    {
        public TopApMenuButton menuButton;
        public TopApMenuArrow apMenuLeft;
        public TopApMenuArrow apMenuRight;

        public TopApMenu(dc.h2d.Object parent, FocusManager fm)
        {
            menuButton = new TopApMenuButton(parent, fm);
            apMenuLeft = new TopApMenuArrow(parent, -1, menuButton, fm);
            apMenuRight = new TopApMenuArrow(parent, 1, menuButton, fm);

            FocusItem.SetLeftRight(apMenuLeft, menuButton);
            FocusItem.SetLeftRight(menuButton, apMenuRight);
        }

        public void ActualiseTopMenu()
        {
            apMenuLeft.ActualiseVisibility();
            apMenuRight.ActualiseVisibility();
        }

        public void SetDown(FocusItem? fiDown)
        {
            apMenuLeft.down = fiDown;
            menuButton.down = fiDown;
            apMenuRight.down = fiDown;
        }
    }
    
    public class TopApMenuButton : FocusItem
    {
        public dc.ui.Text menuButtonText;
        public Bitmap logoBitmap;
        FocusManager focusManager;

        public TopApMenuButton(dc.h2d.Object parent, FocusManager fm)
        {
            focusManager = fm;
            var logoTile = archipelagoLogoTile.clone();

            logoBitmap = new Bitmap(logoTile, parent)
            {
                x = 1400,
                y = 10,
                scaleX = 0.015,
                scaleY = 0.015,
            };
            
            
            Bounds boundsLogo = logoBitmap.getSize(new Bounds());
            double scale = 3/textPixelScale;
            menuButtonText = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
            {
                x = logoBitmap.x + boundsLogo.xMax,
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            menuButtonText.set_text("Switch Menu".AsHaxeString());
            //apMenuButton.y = logoBitmap.y + ((boundsLogo.yMax - apMenuButton.textHeight) /2);
            CenterYTextTo(logoBitmap, menuButtonText, 46);
            menuButtonText.set_textColor((int) APColor.White);
            var inter = new Interactive(
                (boundsLogo.xMax/menuButtonText.scaleX) + menuButtonText.get_textWidth(),
                boundsLogo.yMax,
                menuButtonText,
                null
            )
            {
                x = -boundsLogo.xMax/menuButtonText.scaleX,
                y = -(boundsLogo.yMax - menuButtonText.textHeight) /2,

                onClick = (e) =>
                {
                    Act();
                },
                onMove = (e) =>
                {
                    focusManager.InitializeModFocus();
                },
                onOut = (e) =>
                {
                    if (focusManager.page == 0) focusManager.EndModFocus();
                }
            };
        }

        public Bounds GetLogoBounds()
        {
            return logoBitmap.getSize(new Bounds());
        }

        public Bounds GetTextBounds()
        {
            return menuButtonText.getSize(new Bounds());
        }

        public override void Highlight()
        {
            menuButtonText.set_textColor((int) APColor.Yellow);
        }

        public override void StopHighlight()
        {
            menuButtonText.set_textColor((int) APColor.White);
        }

        public override void Act()
        {
            if (focusManager.page == 0)
            {
                focusManager.page = focusManager.lastPage;
            }
            else
            {
                focusManager.lastPage = focusManager.page;
                focusManager.page = 0;
            }
            focusManager.ChangeApMenuButtonDownTarget();
        }
    }

    public class TopApMenuArrow : FocusItem
    {
        public dc.ui.Text menuArrow;
        public int kind;
        FocusManager focusManager;

        public TopApMenuArrow(dc.h2d.Object parent, int kind, TopApMenuButton mainButton, FocusManager fm)
        {
            this.kind = kind;
            focusManager = fm;
            Bounds boundsMenuButton = mainButton.GetTextBounds();
            Bounds boundsLogo = mainButton.GetLogoBounds();
            double scale = 3/textPixelScale;
            if (kind == 1)
            {
                menuArrow = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
                {
                    x = mainButton.menuButtonText.x + boundsMenuButton.xMax,
                    y = mainButton.menuButtonText.y,
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                menuArrow.set_text(" > ".AsHaxeString());
            }
            else
            {
                menuArrow = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
                {
                    y = mainButton.menuButtonText.y,
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                menuArrow.set_text(" < ".AsHaxeString());
                menuArrow.x = mainButton.logoBitmap.x - menuArrow.textWidth;
            }
            
            menuArrow.set_textColor((int) APColor.White);
            var inter = new Interactive(
                menuArrow.get_textWidth(),
                boundsLogo.yMax,
                menuArrow,
                null
            )
            {
                y = -(boundsLogo.yMax - mainButton.menuButtonText.textHeight) /2,

                onClick = (e) =>
                {
                    Act();
                },
                onMove = (e) =>
                {
                    focusManager!.ChangeFocusCursor(this);
                }
            };
        }

        public void ActualiseVisibility()
        {
            menuArrow.set_visible(IsVisible());
            focusDisabled = !IsVisible();
            if (!IsVisible() && focusManager.currentFocus == this)
                focusManager.ChangeFocus(topMenu!.menuButton);
        }

        private bool IsVisible()
        {
            return !(focusManager.page == 0 || (focusManager.page == 1 && kind == -1) || (focusManager.page == focusManager.nbPage && kind == 1));
        }

        public override void Highlight()
        {
            menuArrow.set_textColor((int) APColor.Yellow);
        }

        public override void StopHighlight()
        {
            menuArrow.set_textColor((int) APColor.White);
        }

        public override void Act()
        {
            focusManager.page += kind;
            focusManager.ChangeApMenuButtonDownTarget();
        }
    }
}