using dc.ui;
using ModCore.Utilities;
using HaxeProxy.Runtime;
using dc.h2d;

using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public class TextButton
    {
        public dc.h2d.Object parent;
        private UIBox bgBox;
        private UIBox outerBox;
        public dc.ui.Text buttonText;
        public Action act;
        private Interactive inter;
        public bool disabled;

        public TextButton(dc.h2d.Object parent, double x, double y, bool centerX, bool centerY, string text, bool disable)
        {
            this.parent = parent;
            disabled = disable;

            act = () => {};

            double scale = 3/textPixelScale;
            buttonText = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            buttonText.set_text(text.AsHaxeString());

            bgBox = new UIBox("boxMain".AsHaxeString(), ((buttonText.get_textWidth() * textBaseScale * scale)+10)*screenScale, ((buttonText.get_textHeight() * textBaseScale * scale)+10)*screenScale, 0, 0)
            {
                scaleX = 3,
                scaleY = 3
            };
            if (centerX) FullCenterX(parent, bgBox);
            else bgBox.x = x;
            if (centerY) FullCenterY(parent, bgBox);
            else bgBox.y = y;
            bgBox.posChanged = true;

            bgBox.colorizeSG(660257);

            outerBox = new UIBox("boxInfo".AsHaxeString(), bgBox.wid, bgBox.hei, 0, 0)
            {
                x = bgBox.x,
                y = bgBox.y,
                scaleX = 3,
                scaleY = 3
            };

            parent.addChild(bgBox);
            parent.addChild(outerBox);

            buttonText.x = bgBox.x+5;
            buttonText.y = bgBox.y+5;
            buttonText.posChanged = true;
            parent.removeChild(buttonText);
            parent.addChild(buttonText);
            if (disabled) buttonText.set_textColor(9868950);

            inter = new Interactive(
                outerBox.wid /(3*screenScale),
                outerBox.hei /(3*screenScale),
                /*(buttonText.get_textWidth()/3) +10,
                (buttonText.get_textHeight()/3) +10,*/
                outerBox,
                null
            )
            {
                onClick = (e) =>
                {
                    if (!disabled) act.Invoke();
                },
                onMove = (e) =>
                {
                    if (!disabled) buttonText.set_textColor(16776960);
                },
                onOut = (e) =>
                {
                    if (!disabled) buttonText.set_textColor(16777215);
                },
                visible = !disabled
            };
        }

        public void SetVisible(bool visible)
        {
            bgBox.visible = visible;
            outerBox.visible = visible;
            buttonText.visible = visible;
        }

        public void SetEnabled(bool enabled)
        {
            disabled = !enabled;
            if (disabled) buttonText.set_textColor(9868950);
            else buttonText.set_textColor(268435455);
            inter.visible = enabled;
        }
    }
}