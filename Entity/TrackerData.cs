using System.Text.Json;
using static DeadCellsArchipelago.ItemManager;
using Serilog;

namespace DeadCellsArchipelago
{
    public static class TrackerData
    {
        public static Dictionary<string, HashSet<string>> StartCalculate()
        {
            var json = File.ReadAllText(GetTrackerDataFilePath());
            Dictionary<string, Entry>? data = JsonSerializer.Deserialize<Dictionary<string, Entry>>(json);
            return CalculateTraker(data);
        }

        public static Dictionary<string, HashSet<string>> CalculateTraker(Dictionary<string, Entry>? data)
            {
                Dictionary<string, HashSet<string>> res = [];

                if (SAVED_DATA == null || data == null) return res;

                res["AllT"] = new HashSet<string>();
                res["AllR"] = new HashSet<string>();
                res["TAspect"] = new HashSet<string>();
                res["RAspect"] = new HashSet<string>();
                foreach (KeyValuePair<string, Entry> entry in data)
                {
                    string key = "";
                    bool added = false;
                    
                    if(CanGoDLC(entry.Value.dlc) && CanCosmetics(entry.Value.type))
                    {
                        if (entry.Value.type == "aspect")
                        {
                            key = "Aspect";
                            IncToDict(ref res, key, entry.Key);
                            added = true;
                        }
                        else
                        {
                            foreach (Source source in entry.Value.sources)
                            {
                                if(CanGoDLC(source.dlc) && SAVED_DATA != null)
                                {
                                    for (int i = source.min_bc; i <= Math.Min(source.max_bc, SAVED_DATA.bscLevelToWin); i++)
                                    {
                                        key = source.biome + i;
                                        IncToDict(ref res, key, entry.Key);
                                        added = true;
                                    }
                                }
                            }
                        }
                        if(added)
                        {
                            res["AllT"].Add(entry.Key);
                            if(SAVED_DATA != null && !SAVED_DATA.IsCheckSent(entry.Key)) res["AllR"].Add(entry.Key);
                        }
                    }
                }
                foreach (string biomeId in GetBiomesId())
                {
                    List<string> start = ["T", "R"];
                    foreach (string kind in start)
                    {
                        var allItems = new HashSet<string>();
                        for (int difficulty = 0; difficulty <= 5; difficulty++)
                        {
                            string key = $"{kind}{biomeId}{difficulty}";
                            if (res.ContainsKey(key))
                            {
                                allItems.UnionWith(res[key]);
                            }
                        }
                        res[$"{kind}{biomeId}T"] = allItems;
                    }
                }
                return res;
            }

            public static bool CanGoDLC(string dlc)
            {
                if (ARCHIPELAGO == null) return false;
                switch (dlc)
                {
                    case "":
                        return true;
                    case "RiseOfTheGiant":
                        return ARCHIPELAGO.riseOfTheGiant;
                    case "TheBadSeed":
                        return ARCHIPELAGO.theBadSeed;
                    case "FatalFalls":
                        return ARCHIPELAGO.fatalFalls;
                    case "TheQueenAndTheSea":
                        return ARCHIPELAGO.theQueenAndTheSea;
                    case "Purple":
                        return ARCHIPELAGO.returnToCastlevania;
                }
                return false;
            }

            public static bool CanCosmetics(string type)
            {
                if (ARCHIPELAGO == null) return false;
                if (type == "skin" || type == "head") return ARCHIPELAGO.includeCosmetics;
                return true;
            }

            public static void IncToDict(ref Dictionary<string, HashSet<string>> res, string key, string check)
            {
                string keyT = "T" + key;
                string keyR = "R" + key;
                if (!res.ContainsKey(keyT))
                {
                    res[keyT] = new HashSet<string>();
                }
                res[keyT].Add(check);

                if (SAVED_DATA != null && !SAVED_DATA.IsCheckSent(check))
                {
                    if (!res.ContainsKey(keyR))
                    {
                        res[keyR] = new HashSet<string>();
                    }
                    res[keyR].Add(check);
                }
            }

            public static string GetTrackerDataFilePath()
            {
                return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "trackerData.json");
            }

            public static List<string> GetBiomesId()
            {
                return [
                    "PrisonStart", "PrisonCourtyard", "SewerShort", "PurpleGarden", "Greenhouse",
                    "PrisonDepths", "PrisonCorrupt", "PrisonRoof", "Ossuary", "SewerDepths", "DookuCastle",
                    "Swamp", "Bridge", "BeholderPit", "DeathArena", "SwampHeart", "StiltVillage",
                    "AncientTemple", "Tumulus", "Cemetery", "ClockTower", "Crypt", "Cliff",
                    "Cavern", "TopClockTower", "GardenerStage", "Giant", "Castle", "DookuCastleHard",
                    "Shipwreck", "Distillery", "Throne", "DookuArena", "Lighthouse", "QueenArena",
                    "Astrolab", "Observatory", "Bank", "Challenge"
                ];
            }
    }
    public class Source
    {
        public string biome { get; set; } = "";
        public int min_bc { get; set; }
        public int max_bc { get; set; }
        public string dlc { get; set; } = "";
        public string? mob { get; set; }
    }

    public class Entry
    {
        public string type { get; set; } = "";
        public string dlc { get; set; } = "";
        public string? rarity { get; set; }
        public List<Source> sources { get; set; } = [];
    }
}