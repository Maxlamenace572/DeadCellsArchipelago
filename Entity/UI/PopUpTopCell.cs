using dc;
using dc.ui;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;
using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.PauseMenuManager;
using static DeadCellsArchipelago.MainMenuManager;
using dc.h2d.col;

namespace DeadCellsArchipelago {
    public class PopUpTopCell
    {
        public Text label;
        public Text number;
        public dc.h2d.Bitmap bitmap;
        public HashSet<string> toChecks;
        public double width;
        public double interW;
        public double interX;

        public PopUpTopCell(dc.h2d.Object parent, string labelS, HashSet<string> toChecks, int max)
        {
            this.toChecks = toChecks;
            int frame = 0;
            double XY = 0;
            dc.h2d.Tile tile = Assets.Class.ui.getTile("walterWhite".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
            bitmap = new dc.h2d.Bitmap(tile, parent)
            {
                color = ColorVectorRGBA(0, 0, 0, 0)
            };

            double scale = 3/textPixelScale;
            label = new Text(bitmap, true, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            label.set_text($"{labelS}".AsHaxeString());

            number = new Text(bitmap, true, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };;
            number.set_text($"{max-toChecks.Count}/{max}".AsHaxeString());
            number.y = 46;

            Bounds boundsL = label.getSize(new Bounds());
            Bounds boundsN = number.getSize(new Bounds());
            if(boundsN.xMax < boundsL.xMax)
            {
                CenterX(label, number);
                interW = label.get_textWidth();
                width = boundsL.xMax;
            }
            else
            {
                CenterX(number, label);
                interW = number.get_textWidth();
                width = boundsN.xMax;
                interX = -label.x/label.scaleX;
            }

            if(toChecks.Count == 0)
            {
                label.set_textColor(16776960);
                number.set_textColor(16776960);
            }

            var inter = new dc.h2d.Interactive(
                interW,
                label.get_textHeight() + number.get_textHeight(),
                label,
                null
            )
            {
                x = interX,
                onClick = (e) =>
                {
                    UpdateScrollContent(toChecks);
                }
            };
        }

        public void Highlight()
        {
            label.set_textColor(16777087);
            number.set_textColor(16777087);
        }

        public void StopHighlight()
        {
            if(toChecks.Count == 0)
            {
                label.set_textColor(16776960);
                number.set_textColor(16776960);
            }
            else
            {
                label.set_textColor(16777215);
                number.set_textColor(16777215);
            }
        }
    }
}