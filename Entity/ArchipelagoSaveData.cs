using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace DeadCellsArchipelago {
    public class ArchipelagoSaveData
    {
        public HashSet<string> SentChecks { get; set; } = [];
        public HashSet<string> ReceivedItem { get; set; } = [];
        public HashSet<string> BaseItemUnlocked { get; set; } = [];
        public Dictionary<string, int> ReceivedProgressionItem { get; set; } = [];
        public Dictionary<string, int> ReceivedFillerItem { get; set; } = [];
        public Dictionary<string, int> GivenFillerItem { get; set; } = [];
        public bool isDoingChallenge = false;
        public int bscLevelToWin = 4;
        public int numberOfPokebombUse = 1;
        public string currentLevelId = "PrisonStart";

        public void SaveCheckSent(string checkName)
        {
            SentChecks.Add(checkName);
        }

        public void SaveItemReceived(string itemName)
        {
            ReceivedItem.Add(itemName);
        }

        public void AddBaseItemUnlocked(string itemName)
        {
            BaseItemUnlocked.Add(itemName);
        }

        public void AddProgressionItem(string itemName)
        {
            if(ReceivedProgressionItem.ContainsKey(itemName))
            {
                ReceivedProgressionItem[itemName]++;
            }
            else
            {
                ReceivedProgressionItem[itemName] = 1;
            }
        }

        public void AddFillerItem(string itemName)
        {
            if(ReceivedFillerItem.ContainsKey(itemName))
            {
                ReceivedFillerItem[itemName]++;
            }
            else
            {
                ReceivedFillerItem[itemName] = 1;
            }
        }

        public void AddFillerItemGiven(string itemName)
        {
            if(GivenFillerItem.ContainsKey(itemName))
            {
                GivenFillerItem[itemName]++;
            }
            else
            {
                GivenFillerItem[itemName] = 1;
            }
        }

        public bool IsCheckSent(string checkName)
        {
            return SentChecks.Contains(checkName);
        }

        public bool IsItemReceived(string itemName)
        {
            return ReceivedItem.Contains(itemName);
        }

        public bool IsBaseItemUnlocked(string itemName)
        {
            return BaseItemUnlocked.Contains(itemName);
        }

        public int HowManyProgressionItemReceived(string itemName)
        {
            if(ReceivedProgressionItem.ContainsKey(itemName))
            {
                return ReceivedProgressionItem[itemName];
            }
            return 0;
        }

        public int HowManyFillerItemReceived(string itemName)
        {
            if(ReceivedFillerItem.ContainsKey(itemName))
            {
                return ReceivedFillerItem[itemName];
            }
            return 0;
        }

        public int HowManyFillerItemGiven(string itemName)
        {
            if(GivenFillerItem.ContainsKey(itemName))
            {
                return GivenFillerItem[itemName];
            }
            return 0;
        }

        public bool HasReceivedAspect()
        {
            foreach (string item in ReceivedItem)
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

        public int NumberOfBossRuneReceived()
        {
            int res = 0;
            foreach (string item in ReceivedItem)
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