using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace DeadCellsArchipelago {
    public class ArchipelagoSaveData
    {
        public HashSet<string> SentChecks { get; set; } = [];
        public HashSet<string> RecievedItem { get; set; } = [];
        public HashSet<string> BaseItemUnlocked { get; set; } = [];
        public Dictionary<string, int> RecievedProgressionItem { get; set; } = [];
        public Dictionary<string, int> RecievedFillerItem { get; set; } = [];
        public bool isDoingChallenge = false;
        public int bscLevelToWin = 4;
        public int numberOfPokebombUse = 1;
        public string currentLevelId = "PrisonStart";

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
            if(RecievedProgressionItem.ContainsKey(itemName))
            {
                RecievedProgressionItem[itemName]++;
            }
            else
            {
                RecievedProgressionItem[itemName] = 1;
            }
        }

        public void AddFillerItem(string itemName)
        {
            if(RecievedFillerItem.ContainsKey(itemName))
            {
                RecievedFillerItem[itemName]++;
            }
            else
            {
                RecievedFillerItem[itemName] = 1;
            }
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

        public int HowManyProgressionItemRecieved(string itemName)
        {
            if(RecievedProgressionItem.ContainsKey(itemName))
            {
                return RecievedProgressionItem[itemName];
            }
            return 0;
        }

        public int HowManyFillerItemRecieved(string itemName)
        {
            if(RecievedFillerItem.ContainsKey(itemName))
            {
                return RecievedFillerItem[itemName];
            }
            return 0;
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

        public int CountSentAspect()
        {
            int res = 0;
            foreach (string item in SentChecks)
            {
                if ("ASP" == item[..3])
                {
                    res++;
                }
            }

            return res;
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

        public int NumberOfBossRuneRecieved()
        {
            int res = 0;
            foreach (string item in RecievedItem)
            {
                if (item.Length >= 8 && "BossRune" == item[..8])
                {
                    res ++;
                }
            }

            return res;
        }
    }
}