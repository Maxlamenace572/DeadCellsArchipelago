namespace DeadCellsArchipelago {
    public class ArchipelagoSaveData
    {
        public HashSet<string> SentChecks { get; set; } = [];
        public HashSet<string> RecievedItem { get; set; } = [];
        public HashSet<string> BaseItemUnlocked { get; set; } = [];
        public int bscLevelToWin = 4;

        public void SaveCheckSent(string checkName)
        {
            SentChecks.Add(checkName);
        }

        public void SaveItemRecieved(string itemName)
        {
            RecievedItem.Add(itemName);
        }

        public void AddBaseItemUnlocked(string itemName)
        {
            BaseItemUnlocked.Add(itemName);
        }

        public bool IsCheckSent(string checkName)
        {
            return SentChecks.Contains(checkName);
        }

        public bool IsItemRecieved(string itemName)
        {
            return RecievedItem.Contains(itemName);
        }

        public bool IsBaseItemUnlocked(string itemName)
        {
            return BaseItemUnlocked.Contains(itemName);
        }

        public bool HasReceivedAspect()
        {
            foreach (string item in RecievedItem)
            {
                if ("ASP" == item[..3])
                {
                    return true;
                }
            }

            return false;
        }
    }
}