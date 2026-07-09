namespace DeadCellsArchipelago {
    public class TrapData
    {
        public string itemName;
        public bool canSendTrapLinkFromCall;

        public TrapData(string itemName, bool canSendTrapLinkFromCall)
        {
            this.itemName = itemName;
            this.canSendTrapLinkFromCall = canSendTrapLinkFromCall;
        }
    }
}