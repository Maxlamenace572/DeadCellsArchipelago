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
        public static dc.ui.Text? send = null;
        public static dc.ui.Text? retrieve = null;

        public EnergyLinkDown(dc.h2d.Object parent, double x, double y)
        {
            this.x = x;
            this.y = y;
            this.parent = parent;
            SetButtons();
        }

        public void SetButtons()
        {
            double scale = 3/textPixelScale;
            send = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null)
            {
                x = x,
                y = y,
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            send.set_text("Send (-20%)".AsHaxeString());
            send.set_textColor((int) APColor.White);

            var inter = new Interactive(
                send.get_textWidth(),
                send.get_textHeight(),
                send,
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

            retrieve = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null)
            {
                x = x+250,
                y = y,
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            retrieve.set_text("Retrieve".AsHaxeString());
            retrieve.x -= retrieve.get_textWidth();
            retrieve.set_textColor((int) APColor.White);
            inter = new Interactive(
                retrieve.get_textWidth(),
                retrieve.get_textHeight(),
                retrieve,
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
        }

        public void SetVisible(bool visible)
        {
            send?.set_visible(visible);
            retrieve?.set_visible(visible);
        }

        public void Highlight(bool isSend)
        {
            if (isSend) send?.set_textColor((int) APColor.Yellow);
            else retrieve?.set_textColor((int) APColor.Yellow);
        }

        public void StopHighlight(bool isSend)
        {
            if (isSend) send?.set_textColor((int) APColor.White);
            else retrieve?.set_textColor((int) APColor.White);
        }

        public void Act(bool isSend)
        {
            if (isSend)
            {
                if(ARCHIPELAGO == null || !ARCHIPELAGO.isConnected) return;
                int res = Math.Min(energyLink!.GetCellValue(), HERO!.cells);
                AddCells(-res);
                cellsNumber?.set_text($" {HERO!.cells}".AsHaxeString());
                ARCHIPELAGO.energyLinkManager!.DepositCells(res);
            }
            else
            {
                if(ARCHIPELAGO == null || !ARCHIPELAGO.isConnected) return;
                ARCHIPELAGO.energyLinkManager!.WithdrawCells(energyLink!.GetCellValue());
            }
        }
    }
}