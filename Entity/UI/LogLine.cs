using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;


using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class LogLine : Line
    {
        public dc.ui.Text text;
        public string logName;

        public LogLine(double x, double y, string logName, int color)
            : base(400, 50, x, y, color)
        {
            this.logName = logName;

            double scaleText = 1.0/(3*screenScale);
            text = new dc.ui.Text(null, false, false, new Ref<double>(ref scaleText), null, null);

            text.set_text($" {logName}".AsHaxeString());
        }

        public override void AddParent(dc.h2d.Object parent)
        {
            base.AddParent(parent);
            bgBox.addChildAt(text, bgBox.layerCount);

            text.y = (bgBox.sg.height - (text.get_textHeight()*text.scaleX))/2;
        }

        public void Highlight()
        {
            text.set_textColor(16776960);
        }

        public void StopHighlight()
        {
            text.set_textColor(16777215);
        }
    }
}