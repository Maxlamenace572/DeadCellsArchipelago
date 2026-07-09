namespace DeadCellsArchipelago {
    public class EnergyLink
    {
        public EnergyLinkTopText energyLinkTopText;
        public EnergyLinkMiddle energyLinkMiddle;
        public EnergyLinkDown energyLinkDown;

        public EnergyLink(dc.h2d.Object parent)
        {
            energyLinkTopText = new EnergyLinkTopText(parent, 50, 150);
            energyLinkMiddle = new EnergyLinkMiddle(parent, 50, 200);
            energyLinkDown = new EnergyLinkDown(parent, 50, 270);
        }

        public void SetVisible(bool visible)
        {
            energyLinkTopText.SetVisible(visible);
            energyLinkMiddle.SetVisible(visible);
            energyLinkDown.SetVisible(visible);
        }

        public int GetCellValue()
        {
            return energyLinkMiddle.GetCellValue();
        }

        public void UpdateAvailableValue(int bankValue)
        {
            energyLinkTopText.UpdateAvailableValue(bankValue);
        }
    }
}