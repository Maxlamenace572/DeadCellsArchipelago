namespace DeadCellsArchipelago {
    public class EnergyLink
    {
        public EnergyLinkTopText energyLinkTopText;
        public EnergyLinkMiddle energyLinkMiddle;
        public EnergyLinkDown energyLinkDown;
        public int lastHighlight = -1;

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

        public void Highlight(int index)
        {
            switch (index)
            {
                case 0:
                    energyLinkMiddle.Highlight(true);
                    break;
                case 1:
                    energyLinkMiddle.Highlight(false);
                    break;
                case 2:
                    energyLinkDown.Highlight(true);
                    break;
                case 3:
                    energyLinkDown.Highlight(false);
                    break;
            }
            StopHighlight(lastHighlight);
            lastHighlight = index;
        }

        public void StopHighlight(int index)
        {
            switch (index)
            {
                case 0:
                    energyLinkMiddle.StopHighlight(true);
                    break;
                case 1:
                    energyLinkMiddle.StopHighlight(false);
                    break;
                case 2:
                    energyLinkDown.StopHighlight(true);
                    break;
                case 3:
                    energyLinkDown.StopHighlight(false);
                    break;
            }
        }

        public void StopHighlight()
        {
            StopHighlight(lastHighlight);
            lastHighlight = -1;
        }

        public void Act(int index)
        {
            switch (index)
            {
                case 0:
                    energyLinkMiddle.Act(true);
                    break;
                case 1:
                    energyLinkMiddle.Act(false);
                    break;
                case 2:
                    energyLinkDown.Act(true);
                    break;
                case 3:
                    energyLinkDown.Act(false);
                    break;
            }
        }
    }
}