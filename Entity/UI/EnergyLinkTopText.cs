using dc;
using dc.h2d;
using dc.h2d.col;
using HaxeProxy.Runtime;
using ModCore.Utilities;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public class EnergyLinkTopText
    {
        public double x;
        public double y;
        public dc.ui.Text? title = null;
        public Bitmap? cellBitmap = null;
        public dc.ui.Text? cellsNumber = null;
        public dc.h2d.Object parent;

        public EnergyLinkTopText(dc.h2d.Object parent, double x, double y)
        {
            this.x = x;
            this.y = y;
            this.parent = parent;
            SetTexts();
        }

        public void SetTexts()
        {
            double scale = 1;
            title = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null)
            {
                x = x,
                y = y,
                scaleX = 1,
                scaleY = 1
            };
            title.set_text("Available:".AsHaxeString());
            Bounds boundsText = title.getSize(new Bounds());

            int frame = 0;
            double XY = 0;
            var logoTile = Assets.Class.gameElements.getTile("cell".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
            cellBitmap = new Bitmap(logoTile, parent)
            {
                y = y+2,
            };
            Bounds boundsLogo = cellBitmap.getSize(new Bounds());
            cellBitmap.x = 250 + x - (boundsLogo.xMax - boundsLogo.xMin);
            cellBitmap.posChanged = true;

            cellsNumber = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null)
            {
                y = y,
                scaleX = 1,
                scaleY = 1
            };
            int bankValue = 0;
            if (ARCHIPELAGO != null && ARCHIPELAGO.energyLinkManager != null) bankValue = ARCHIPELAGO.energyLinkManager.ShowStorageNumberCells();
            cellsNumber.set_text($"{bankValue}".AsHaxeString());
            CenterX((int)(250 - (boundsLogo.xMax - boundsLogo.xMin) - title.textWidth), cellsNumber);
            cellsNumber.x += boundsText.xMax + 50;
            cellsNumber.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));
        }

        public void SetVisible(bool visible)
        {
            title?.set_visible(visible);
            cellBitmap?.set_visible(visible);
            cellsNumber?.set_visible(visible);
        }

        public void UpdateAvailableValue(int bankValue)
        {
            if (cellsNumber == null || cellBitmap == null || title == null) return;
            Bounds boundsText = title.getSize(new Bounds());
            Bounds boundsLogo = cellBitmap.getSize(new Bounds());

            cellsNumber.set_text($"{bankValue}".AsHaxeString());
            CenterX((int)(250 - (boundsLogo.xMax - boundsLogo.xMin) - title.textWidth), cellsNumber);
            cellsNumber.x += boundsText.xMax + 50;
        }
    }
}