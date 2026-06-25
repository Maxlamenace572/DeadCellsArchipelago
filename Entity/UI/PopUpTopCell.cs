using dc;
using dc.ui;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;
using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class PopUpTopCell
    {
        public Text label;
        public Text number;
        public dc.h2d.Bitmap bitmap;
        public HashSet<string> toChecks;
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

            double scale = 1;
            label = new Text(bitmap, true, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = 1,
                scaleY = 1
            };
            label.set_text($"{labelS}".AsHaxeString());

            number = new Text(bitmap, true, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = 1,
                scaleY = 1
            };;
            number.set_text($"{max-toChecks.Count}/{max}".AsHaxeString());
            number.y = label.get_textHeight();
            
            if(number.get_textWidth() < label.get_textWidth())
            {
                number.x = (label.get_textWidth() - number.get_textWidth())/2;
                interW = label.get_textWidth();
            }
            else
            {
                label.x = (number.get_textWidth() - label.get_textWidth())/2;
                interW = number.get_textWidth();
                interX = -label.x;
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