using dc.h2d;
using HaxeProxy.Runtime;
using ModCore.Utilities;

using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.MainMenuManager;
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
            double scale = 3/textPixelScale;
            down = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
            {
                x = x,
                y = y,
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            down.set_text(" < ".AsHaxeString());
            down.set_textColor((int) APColor.White);

            var inter = new Interactive(
                down.get_textWidth(),
                down.get_textHeight(),
                down,
                null
            )
            {
                onClick = (e) =>
                {
                    Act(true);
                },
                onMove = (e) =>
                {
                    Highlight(true);
                },
                onOut = (e) =>
                {
                    StopHighlight(true);
                }
            };

            up = new dc.ui.Text(parent, true, false, new Ref<double>(ref scale), null, null)
            {
                x = x+250,
                y = y,
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            up.set_text(" > ".AsHaxeString());
            up.x -= up.get_textWidth();
            up.set_textColor((int) APColor.White);
            inter = new Interactive(
                up.get_textWidth(),
                up.get_textHeight(),
                up,
                null
            )
            {
                onClick = (e) =>
                {
                    Act(false);
                },
                onMove = (e) =>
                {
                    Highlight(false);
                },
                onOut = (e) =>
                {
                    StopHighlight(false);
                }
            };

            numberBg = UIBox.Class.drawBoxMain(150.0*screenScale, 1.0, 4, 3, 0, null);
            //CenterX(250 - down.get_textWidth() - up.get_textWidth(), numberBg);
            //numberBg.x += down.x + down.get_textWidth();
            numberBg.x = 88;
            //CenterY(down, numberBg);
            //numberBg.y += y;
            numberBg.y = 205;
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
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale,
                onMove = (e) =>
                {
                    number?.set_textColor((int) APColor.Yellow);
                },
                onOut = (e) =>
                {
                    number?.set_textColor((int) APColor.White);
                }
            };
            number.set_text($"0".AsHaxeString());
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

        public void Highlight(bool isDown)
        {
            if (isDown) down?.set_textColor((int) APColor.Yellow);
            else up?.set_textColor((int) APColor.Yellow);
        }

        public void StopHighlight(bool isDown)
        {
            if (isDown) down?.set_textColor((int) APColor.White);
            else up?.set_textColor((int) APColor.White);
        }

        public void Act(bool isDown)
        {
            if (isDown)
            {
                cellsToSend = Math.Max(0, GetCellValue()-1);
                number?.set_text($"{cellsToSend}".AsHaxeString());
            }
            else
            {
                cellsToSend = GetCellValue()+1;
                number?.set_text($"{cellsToSend}".AsHaxeString());
            }
        }
    }
}