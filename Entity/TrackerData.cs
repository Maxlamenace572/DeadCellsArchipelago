using System.Text.Json;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago
{
    public static class TrackerData
    {
        private static Dictionary<string, ItemData> ItemsData = [];

        public static Dictionary<string, HashSet<string>> StartCalculate(Dictionary<string, Biome> biomes)
        {
            var json = File.ReadAllText(GetTrackerDataFilePath());
            Dictionary<string, Entry>? data = JsonSerializer.Deserialize<Dictionary<string, Entry>>(json);
            return CalculateTraker(data, biomes);
        }

        public static Dictionary<string, HashSet<string>> CalculateTraker(Dictionary<string, Entry>? data, Dictionary<string, Biome> biomes)
        {
            Dictionary<string, HashSet<string>> res = [];
            ItemsData = [];

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
                            if(CanGoDLC(source.dlc) && GLOBAL_DATA != null)
                            {
                                for (int i = source.min_bc; i <= Math.Min(source.max_bc, GLOBAL_DATA.bscLevelToWin); i++)
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
                        if(SAVED_DATA != null && !SAVED_DATA.IsCheckSent(entry.Key))
                        {
                            res["AllR"].Add(entry.Key);

                            ItemData itD = new();
                            foreach (Source source in entry.Value.sources)
                            {
                                itD.min_bc = Math.Min(source.min_bc, itD.min_bc);
                                if (source.mob != null) itD.mobs.Add(source.mob);
                                if (source.biome == "Challenge" || (biomes[source.biome].accessible && source.min_bc <= SAVED_DATA.CountReceivedStemCell())) itD.accessible = true;
                            }

                            ItemsData[entry.Key] = itD;
                        }
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
            if (GLOBAL_DATA == null) return false;
            switch (dlc)
            {
                case "":
                    return true;
                case "RiseOfTheGiant":
                    return GLOBAL_DATA.riseOfTheGiant;
                case "TheBadSeed":
                    return GLOBAL_DATA.theBadSeed;
                case "FatalFalls":
                    return GLOBAL_DATA.fatalFalls;
                case "TheQueenAndTheSea":
                    return GLOBAL_DATA.theQueenAndTheSea;
                case "Purple":
                    return GLOBAL_DATA.returnToCastlevania;
            }
            return false;
        }

        public static bool CanCosmetics(string type)
        {
            if (GLOBAL_DATA == null) return false;
            if (type == "skin" || type == "head") return GLOBAL_DATA.includeCosmetics;
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

        public static Dictionary<string, Biome> CalculateRegionData()
        {
            var json = File.ReadAllText(GetRegionDataFilePath());
            Dictionary<string, List<TDTransition>> regions = 
                JsonSerializer.Deserialize<Dictionary<string, List<TDTransition>>>(json)!;

            Dictionary<string, Biome> biomes = [];

            foreach (KeyValuePair<string, List<TDTransition>> entry in regions)
            {
                biomes[entry.Key] = new Biome();
            }
            biomes["PrisonStart"].accessible = true;

            foreach (KeyValuePair<string, List<TDTransition>> entry in regions)
            {
                foreach (TDTransition tr in entry.Value)
                {
                    foreach (List<string> line in tr.require)
                    {
                        line.Add("B_" + entry.Key);
                        biomes[tr.to].EveryRequirements.Add(line);
                    }
                }
            }

            int bsc = SAVED_DATA!.CountReceivedStemCell();
            foreach (KeyValuePair<string, Biome> biome in biomes)
            {
                biome.Value.CalculateAccessibility(biomes, bsc);
            }

            return biomes;
        }

        public static string GetRegionDataFilePath()
        {
            return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "region.json");
        }

        public static bool IsItemAccessible(string itemId)
        {
            return ItemsData[itemId].accessible;
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

    public class TDTransition
    {
        public string to { get; set; } = "";
        public List<List<string>> require { get; set; } = [];
    }

    public class Biome
    {
        public bool accessible;
        public List<List<string>> EveryRequirements { get; set; } = [];
        public List<List<string>> RemainingRequirements { get; set; } = [];

        public void CalculateAccessibility(Dictionary<string, Biome> biomes, int bsc)
        {
            foreach (List<string> items in EveryRequirements)
            {
                RemainingRequirements.Add([]);
                bool completeLine = true;
                foreach (string item in items)
                {
                    if (item.Length >= 21 && item[..21] == "Progressive Stem Cell")
                    {
                        int nb = 1;
                        if (item.Length == 23) nb = item[^1]-'0';


                        if (nb > bsc) {
                            for (int i=bsc; i<nb; i++)
                            {
                                RemainingRequirements[^1].Add("Progressive Stem Cell");
                            }
                            completeLine = false;
                        }
                    }
                    else if ((!biomes.ContainsKey(item[2..]) && !SAVED_DATA!.IsItemReceived(item)) || (biomes.ContainsKey(item[2..]) && !biomes[item[2..]].accessible)
                        || (new[] {"Boss_DookuBeast", "Boss_Death"}.Any(item.Contains) && !SAVED_DATA!.IsCheckSent(item)))
                    {
                        RemainingRequirements[^1].Add(item);
                        completeLine = false;
                    }
                }
                if (completeLine)
                {
                    accessible = true;
                    return;
                }
            }
        }
    }

    public class ItemData
    {
        public bool accessible = false;
        public int min_bc = 6;
        public HashSet<string> mobs = [];
        public List<List<string>> requirements = [];
        public string? description;
    }
}