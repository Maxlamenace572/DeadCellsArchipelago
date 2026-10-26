using dc;
using dc.hl.types;
using Hashlink.Marshaling;
using ModCore.Utilities;
using Serilog;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.TrackerData;

namespace DeadCellsArchipelago {
    public static class MirrorManager
    {

        public static void InitializeMirrorHooks()
        {
            Log.Information("[AP] Loading Mirror Hooks...");
            
            Hook_User.listLootableMonstersOnDifficulty += OnListLootableMonsters;

            Log.Information("[AP] Mirror Hooks loaded");
        }

        private static ArrayObj OnListLootableMonsters(Hook_User.orig_listLootableMonstersOnDifficulty orig, User self, int diff, ArrayObj invBlueprints)
        {
            ArrayObj res = new ArrayObj()
            {
                array = new(HashlinkMarshal.Module.KnownTypes.String, 0),
                length = 0
            };

            if (GLOBAL_DATA!.currentMirrorEnemy != null)
            {
                res.push(GLOBAL_DATA!.currentMirrorEnemy.AsHaxeString());
                return res;
            }

            HashSet<string> accessibleEnemies = GetAccessibleMobsInBSC(diff);
            double sum = 0;
            foreach(string enemy in accessibleEnemies)
            {
                int weight = GLOBAL_DATA!.GetMirrorEnemyWeight(enemy);
                sum += 1.0/weight;
            }
            GLOBAL_DATA!.SaveGlobalSaveJson();

            double chosen = new Random().NextDouble();
            double cumulativeProba = 0;
            foreach (string enemy in accessibleEnemies)
            {
                cumulativeProba += 1.0/GLOBAL_DATA!.GetMirrorEnemyWeight(enemy) / sum;
                if (cumulativeProba >= chosen)
                {
                    GLOBAL_DATA!.currentMirrorEnemy = enemy;
                    GLOBAL_DATA.SaveGlobalSaveJson();
                    res.push(enemy.AsHaxeString());
                    return res;
                }
            }

            //should not happens if my maths are good
            Log.Error($"[AP] Error selecting random mirror target");
            res.push("Runner".AsHaxeString());
            return res;
        }

        public static void EnemyKilled(string mobId)
        {
            if (mobId != GLOBAL_DATA!.currentMirrorEnemy) return;

            GLOBAL_DATA.MirrorEnemies[GLOBAL_DATA!.currentMirrorEnemy]++;
            GLOBAL_DATA.currentMirrorEnemy = null;

            string? locationToHint = GetRandomAccessibleCheck();
            if (locationToHint == null)
                IncreaseShopSales(4);
            else
            {
                IncreaseShopSales(2);
                ARCHIPELAGO!.HintLocation(locationToHint);
            }
            GLOBAL_DATA.SaveGlobalSaveJson();
        }

        public static string? GetRandomAccessibleCheck()
        {
            if (ARCHIPELAGO == null || !ARCHIPELAGO.isConnected) return null;

            HashSet<string> remainingItems = StartCalculate(CalculateRegionData())["AllR"];
            List<string> accessibleItems = [];
            ARCHIPELAGO.UpdateRevealedHints();
            foreach (string item in remainingItems)
            {
                if (ItemsData[item].accessible && !ARCHIPELAGO.IsLocationHinted(item))
                    accessibleItems.Add(item);
            }

            if (accessibleItems.Count == 0) return null;
            return accessibleItems[new Random().Next(0, accessibleItems.Count)];

        }

        private static void IncreaseShopSales(int nb)
        {
            GLOBAL_DATA!.reducedPercentageShop = System.Math.Min(90, GLOBAL_DATA.reducedPercentageShop+nb);
        }
    }
}