using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class EnergyLinkMiddle
    {
        public double x;
        public double y;
        public dc.h2d.Object parent;
        public TextButton upButton;
        public TextButton downButton;
        public TextField number;
        public int cellsToSend = 0;

        public EnergyLinkMiddle(dc.h2d.Object parent, double x, double y)
        {
            this.x = x;
            this.y = y;
            this.parent = parent;

            downButton = new TextButton(parent, false, x,  y, false, false, " < ", false)
            {
                act = () =>
                {
                    cellsToSend = Math.Max(0, GetCellValue()-10);
                    number?.SetFieldValue($"{cellsToSend}");
                },
                onMove = () =>
                {
                    focusManager!.ChangeFocusCursor(downButton!);
                },
                onOut = () => {},
                canRepeatAct = true
            };

            number = new TextField(parent, 94, y+2, false, false, "", (int)APColor.DeepBlue, 140)
            {
                onFocus = () =>
                {
                    focusManager!.textFieldFocused = true;
                },
                onQuitFocus = () =>
                {
                    focusManager!.textFieldFocused = false;
                },
            };
            number.SetFieldValue("0");

            upButton = new TextButton(parent, false, x+220,  y, false, false, " > ", false)
            {
                act = () =>
                {
                    cellsToSend = GetCellValue()+10;
                    number?.SetFieldValue($"{cellsToSend}");
                },
                onMove = () =>
                {
                    focusManager!.ChangeFocusCursor(upButton!);
                },
                onOut = () => {},
                canRepeatAct = true
            };
        }

        public void SetVisible(bool visible)
        {
            upButton.SetVisible(visible);
            downButton.SetVisible(visible);
            number.SetVisible(visible);
        }

        public int GetCellValue()
        {
            int res;
            if (int.TryParse(number.GetFieldValue().ToString(), out int valeur))
            {
                res = valeur;
            }
            else
            {
                res = cellsToSend;
                number.SetFieldValue($"{res}");
            }
            return res;
        }
    }
}