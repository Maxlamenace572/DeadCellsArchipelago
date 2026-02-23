namespace DeadCellsArchipelago {
    public class ArchipelagoSaveData
    {
        public HashSet<string> SentChecks { get; set; } = [];

        public void SaveCheckSent(string checkName)
        {
            SentChecks.Add(checkName);
        }

        public bool IsCheckSent(string checkName)
        {
            return SentChecks.Contains(checkName);
        }
    }
}