using dc.h2d;
using HaxeProxy.Runtime;
using ModCore.Utilities;

using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.PauseMenuManager;
using static DeadCellsArchipelago.ItemManager;
using dc.ui;

namespace DeadCellsArchipelago {
    public class EnergyLinkMiddle
    {
        public double x;
        public double y;
        public dc.h2d.Object parent;
        public static dc.ui.Text? up = null;
        public static dc.ui.Text? down = null;
        public static dc.h2d.TextInput? number = null;
        public static UIBox? numberBg = null;
        public int cellsToSend = 0;

        public EnergyLinkMiddle(dc.h2d.Object parent, double x, double y)
        {
            this.x = x;
            this.y = y;
            this.parent = parent;
            SetButtons();
        }

        public void SetButtons()
        {
            double scale = 1;
            down = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
            {
                x = x,
                y = y,
                scaleX = 1,
                scaleY = 1
            };
            down.set_text(" < ".AsHaxeString());
            down.set_textColor(16777215);

            var inter = new Interactive(
                down.get_textWidth(),
                down.get_textHeight(),
                down,
                null
            )
            {
                onClick = (e) =>
                {
                    cellsToSend = Math.Max(0, GetCellValue()-1);
                    number?.set_text($"{cellsToSend}".AsHaxeString());
                },
                onMove = (e) =>
                {
                    down?.set_textColor(16776960);
                },
                onOut = (e) =>
                {
                    down?.set_textColor(16777215);
                }
            };

            up = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
            {
                x = x+250,
                y = y,
                scaleX = 1,
                scaleY = 1
            };
            up.set_text(" > ".AsHaxeString());
            up.x -= up.get_textWidth();
            up.set_textColor(16777215);
            inter = new Interactive(
                up.get_textWidth(),
                up.get_textHeight(),
                up,
                null
            )
            {
                onClick = (e) =>
                {
                    cellsToSend = GetCellValue()+1;
                    number?.set_text($"{cellsToSend}".AsHaxeString());
                },
                onMove = (e) =>
                {
                    up?.set_textColor(16776960);
                },
                onOut = (e) =>
                {
                    up?.set_textColor(16777215);
                }
            };

            numberBg = UIBox.Class.drawBoxMain(150.0*screenScale, 1.0, 4, 3, 0, null);
            CenterX(250 - down.get_textWidth() - up.get_textWidth(), numberBg);
            numberBg.x += down.x + down.get_textWidth();
            CenterY(down, numberBg);
            numberBg.y += y;
            numberBg.alpha = 0.85;
            numberBg.sg.color = ColorVectorRGBA(17*numberBg.alpha, 17*numberBg.alpha, 37*numberBg.alpha, 1);
            numberBg.scaleX = 3;
            numberBg.scaleY = 3;

            parent.addChild(numberBg);

            dc.ui.Text frontInput = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null);
            number = new dc.h2d.TextInput(frontInput.font, parent)
            {
                x = numberBg.x+6,
                y = numberBg.y+2,
                inputWidth = 164,
                onMove = (e) =>
                {
                    number?.set_textColor(16776960);
                },
                onOut = (e) =>
                {
                    number?.set_textColor(16777215);
                }
            };
        }

        public void SetVisible(bool visible)
        {
            up?.set_visible(visible);
            down?.set_visible(visible);
            number?.set_visible(visible);
            number?.set_visible(visible);
            numberBg?.set_visible(visible);
        }

        public int GetCellValue()
        {
            int res;
            if (int.TryParse(number?.text.ToString(), out int valeur))
            {
                res = valeur;
            }
            else
            {
                res = cellsToSend;
                number?.set_text($"{res}".AsHaxeString());
            }
            return res;
        }
    }
}