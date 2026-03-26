using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace DeadCellsArchipelago {
    public class ArchipelagoSaveData
    {
        public HashSet<string> SentChecks { get; set; } = [];
        public HashSet<string> RecievedItem { get; set; } = [];
        public HashSet<string> BaseItemUnlocked { get; set; } = [];
        public HashSet<string> RecievedProgressionItem { get; set; } = [];
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

        public void AddProgressionItem(string itemName)
        {
            RecievedProgressionItem.Add(itemName);
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

        public bool IsProgressionItemRecieved(string itemName)
        {
            return RecievedProgressionItem.Contains(itemName);
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

        public void AppendToSentChecksJson(string value, int slot)
        {
            var savePath = GetSaveFilePath(slot);
            var json = File.ReadAllText(savePath);
            var jObject = JObject.Parse(json);

            var array = (JArray?)jObject["SentChecks"];
            
            if (array != null && !array.Values<string>().Contains(value))
                array.Add(value);

            File.WriteAllText(savePath, jObject.ToString(Formatting.Indented));
        }

        private string GetSaveFilePath(int slot)
        {
            string saveDir = Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data");
            
            Directory.CreateDirectory(saveDir);
            return Path.Combine(saveDir, $"archipelagoUserId_{slot}.json");
        }
    }
}