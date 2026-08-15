using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

using static DeadCellsArchipelago.ModAssetManager;
using static DeadCellsArchipelago.ItemManager;
using dc.haxe;

namespace DeadCellsArchipelago {
    public class ArchipelagoSaveData
    {
        public HashSet<string> SentChecks { get; set; } = [];
        public HashSet<string> OfflineChecks { get; set; } = [];
        public HashSet<string> ReceivedItem { get; set; } = [];
        public HashSet<string> BaseItemUnlocked { get; set; } = [];
        public Dictionary<string, int> ReceivedProgressionItem { get; set; } = [];
        public Dictionary<string, int> ReceivedFillerItem { get; set; } = [];
        public Dictionary<string, int> GivenFillerItem { get; set; } = [];
        public bool isDoingChallenge = false;
        public int numberOfPokebombUse = 1;
        public string currentLevelId = "PrisonStart";
        public string archipelagoSeed = "";
        public bool hasDoneBank = false;

        public void InitValues(string seed)
        {
            if (archipelagoSeed != "") return;
            archipelagoSeed = seed;

            foreach(string scroll in GetUpScrolls())
            {
                ReceivedFillerItem[scroll] = 0;
                GivenFillerItem[scroll] = 0;
            }
        }

        public void SaveCheckSent(string checkName)
        {
            SentChecks.Add(checkName);
        }

        public void SaveOfflineCheck(string internalId)
        {
            OfflineChecks.Add(internalId);
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
            return SentChecks.Contains(checkName) || OfflineChecks.Contains(checkName);
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
            if (!File.Exists(savePath))
            {
                var saveJson = JsonConvert.SerializeObject(SAVED_DATA, Formatting.Indented);
                File.WriteAllText(savePath, saveJson);
            }
            var json = File.ReadAllText(savePath);
            var jObject = JObject.Parse(json);

            var array = (JArray?)jObject["SentChecks"];
            
            if (array != null && !array.Values<string>().Contains(value))
                array.Add(value);

            File.WriteAllText(savePath, jObject.ToString(Formatting.Indented));
        }

        public void RemoveFromOfflineChecksJson(string value, int slot)
        {
            var savePath = GetSaveFilePath(slot);
            var json = File.ReadAllText(savePath);
            var jObject = JObject.Parse(json);

            var array = (JArray?)jObject["OfflineChecks"];
            var token = array?.FirstOrDefault(t => t.Value<string>() == value);

            token?.Remove();

            File.WriteAllText(savePath, jObject.ToString(Formatting.Indented));
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

        public int CountItemSend()
        {
            if(!itemList.Any()) InitLists();

            int count = 0;
            foreach (string check in SentChecks)
            {
                if (itemList.Contains(check) || outfitList.Contains(check)) count ++;
            }
            return count;
        }

        public int CountOutfitSend()
        {
            if(!outfitList.Any()) InitLists();

            int count = 0;
            foreach (string check in SentChecks)
            {
                if (outfitList.Contains(check)) count ++;
            }
            return count;
        }

        public int CountReceivedStemCell()
        {
            int res = 0;
            foreach (string item in ReceivedItem)
            {
                if (item.Length >= 8 && "BossRune" == item[..8])
                {
                    res++;
                }
            }

            return res;
        }
    }
}