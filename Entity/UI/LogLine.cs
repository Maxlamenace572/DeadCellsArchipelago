using dc;
using dc.h2d;
using dc.h2d.col;
using dc.ui;
using dc.ui.hud;
using dc.ui.icon;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.Translator;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public class LogLine : Line
    {
        public dc.ui.Text text;
        public string logName;

        public LogLine(double x, double y, string logName, int color)
            : base(400, 50, x, y, color)
        {
            this.logName = logName;

            double scaleText = 1.0/3;
            text = new dc.ui.Text(null, false, false, new Ref<double>(ref scaleText), null, null);

            text.set_text($" {logName}".AsHaxeString());
        }

        public override void AddParent(dc.h2d.Object parent)
        {
            base.AddParent(parent);
            bgBox.addChildAt(text, bgBox.layerCount);

            text.y = (bgBox.sg.height - (text.get_textHeight()*text.scaleX))/2;
        }
    }
}