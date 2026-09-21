using dc.ui;
using HaxeProxy.Runtime;
using ModCore.Utilities;

using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public class TextField
    {
        public dc.h2d.Object parent;
        public double x;
        public double y;
        private bool centerX;
        private bool centerY;
        public UIBox bgField;
        public dc.h2d.TextInput textInput;
        public Action textChanged;
        public int bgColor = (int) APColor.DeepBlue;
        public int textColor = (int) APColor.White;
        public int highlightColor = (int) APColor.Yellow;

        public TextField(dc.h2d.Object parent, double x, double y, bool centerX, bool centerY, string text, int? bgColor, double width)
        {
            this.parent = parent;
            this.centerX = centerX;
            this.centerY = centerY;
            if (bgColor != null) this.bgColor = (int) bgColor;

            textChanged = () => {};


            bgField = UIBox.Class.drawBoxMain(width*screenScale, 1.0, 4, 3, 0, null);

            if (centerX) FullCenterX(parent, bgField);
            else bgField.x = x;
            if (centerY) FullCenterY(parent, bgField);
            else bgField.y = y;
            bgField.posChanged = true;
            
            bgField.colorizeSG(this.bgColor);
            bgField.scaleX = 3;
            bgField.scaleY = 3;

            this.x = bgField.x;
            this.y = bgField.y;

            parent.addChild(bgField);

            double scale = 3/textPixelScale;
            Text frontInput = new Text(parent, false, false, new Ref<double>(ref scale), null, null);
            textInput = new dc.h2d.TextInput(frontInput.font, parent)
            {
                x = bgField.x+6,
                y = bgField.y+2,
                inputWidth = (int) width+12,
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale,
                onMove = (e) =>
                {
                    Highlight();
                },
                onOut = (e) =>
                {
                    StopHighlight();
                },
                onChange = () => {
                    textChanged.Invoke();
                }
            };
            textInput.set_text(text.AsHaxeString());
        }

        public void Highlight()
        {
            textInput.set_textColor(highlightColor);
        }

        public void StopHighlight()
        {
            textInput.set_textColor(textColor);
        }

        public string GetFieldValue()
        {
            return textInput.text.ToString();
        }

        public void SetFieldValue(string text)
        {
            textInput.set_text(text.AsHaxeString());
        }

        public void SetVisible(bool visible)
        {
            bgField.visible = visible;
            textInput.visible = visible;
        }
    }
}