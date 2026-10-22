using dc.h2d;
using HaxeProxy.Runtime;
using ModCore.Utilities;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.PauseMenuManager;
using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.HeroManager;

namespace DeadCellsArchipelago {
    public class EnergyLinkDown
    {
        public double x;
        public double y;
        public dc.h2d.Object parent;
        public TextButton send;
        public TextButton retrieve;

        public EnergyLinkDown(dc.h2d.Object parent, double x, double y)
        {
            this.x = x;
            this.y = y;
            this.parent = parent;

            send = new TextButton(parent, false, x,  y, false, false, "Send (-20%)", false)
            {
                act = () =>
                {
                    if(ARCHIPELAGO == null || !ARCHIPELAGO.isConnected) return;
                    int res = Math.Min(energyLink!.GetCellValue(), HERO!.cells);
                    AddCells(-res);
                    cellsNumber?.set_text($" {HERO!.cells}".AsHaxeString());
                    ARCHIPELAGO.energyLinkManager!.DepositCells(res);
                },
                onMove = () =>
                {
                    focusManager!.ChangeFocusCursor(send!);
                },
                onOut = () => {},
            };

            retrieve = new TextButton(parent, false, x+166,  y, false, false, "Retrieve", false)
            {
                act = () =>
                {
                    if(ARCHIPELAGO == null || !ARCHIPELAGO.isConnected) return;
                    ARCHIPELAGO.energyLinkManager!.WithdrawCells(energyLink!.GetCellValue());
                },
                onMove = () =>
                {
                    focusManager!.ChangeFocusCursor(retrieve!);
                },
                onOut = () => {},
            };
        }

        public void SetVisible(bool visible)
        {
            send.SetVisible(visible);
            retrieve.SetVisible(visible);
        }
    }
}