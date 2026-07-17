using dc.level;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.RuneManager;

namespace DeadCellsArchipelago {
    public static class EnemyManager
    {
        public static bool changeNextCallDmgTier = false;
        public static bool changeNextCallLifeTier = false;

        public static void InitializeEnemyHooks()
        {
            Log.Information("[AP] Loading Enemy Hooks...");

            dc.en.Hook_Mob.onDie += OnOnDie;
            Hook_LootGen.generateLootOnMobs += OnGenerateLootOnMobs;
            Hook_MobsGen.getLifeTier += OnGetLifeTier;
            Hook_MobsGen.getDmgTier += OnGetDmgTier;
            
            Log.Information("[AP] Enemy Hooks loaded");
        }

        private static void OnOnDie(dc.en.Hook_Mob.orig_onDie orig, dc.en.Mob self)
        {
            orig(self);

            int randomNumber = new Random().Next(1, 1001);
            if (randomNumber == 1)
            {
                DropItemToPlayer("TimeDistorsion");
            }
        }

        public static void SpawnMobOnPlayer(string id, bool elite, bool anger)
        {
            if (HERO != null)
            {
                int lifeTier = HERO._level.map.mobLifeTier;
                dc.en.Mob mob = dc.en.Mob.Class.create(id.AsHaxeString(), HERO._level, HERO.cx, HERO.cy, HERO._level.map.mobDmgTier, new Ref<int>(ref lifeTier));
                if (elite)
                {
                    mob.setElite(false);
                }
                if (anger)
                {
                    bool bump = false;
                    mob.eliteAnger(new Ref<bool>(ref bump));
                }
                double reductionValue = 0;
                mob.setAffectS(8, 1, new Ref<double>(ref reductionValue), true); //8 is for a stun effect
            }
        }

        public static void EliteTrap()
        {
            List<List<string>> teams = [
                ["Demon", "Curser"],
                ["FlyingShooter", "FatZombie"],
                ["Golem", "Defender"],
                ["Hammer", "Necromant"],
                ["Shielder", "Comboter", "Shocker"],
                ["PirateChief", "Harpy"],
                ["Hurler", "Fogger", "ClusterGrenader"],
            ];
            List<string> selectedTeam = teams[new Random().Next(0, teams.Count)];
            foreach (string mob in selectedTeam)
            {
                SpawnMobOnPlayer(mob, true, true);
            }
        }

        private static void OnGenerateLootOnMobs(dc.level.Hook_LootGen.orig_generateLootOnMobs orig, dc.level.LootGen self)
        {
            useOriginalHasPermanentItem = false;
            orig(self);
            useOriginalHasPermanentItem = true;
        }

        public static int GetDailyLife()
        {
            if (SAVED_DATA == null) return 0;

            if (!SAVED_DATA.IsCheckSent("SpeedBlade")) return 0;
            else if (!SAVED_DATA.IsCheckSent("DamageAura")) return 1;
            else if (!SAVED_DATA.IsCheckSent("DashSword")) return 3;
            return 5;
        }

        public static int GetDailyDmg()
        {
            if (SAVED_DATA == null) return 0;

            if (!SAVED_DATA.IsCheckSent("SpeedBlade")) return 0;
            else if (!SAVED_DATA.IsCheckSent("DamageAura")) return 3;
            else if (!SAVED_DATA.IsCheckSent("DashSword")) return 7;
            return 10;
        }

        private static int OnGetLifeTier(Hook_MobsGen.orig_getLifeTier orig, MobsGen self, LevelMap map, Room room, int levelMaxDist)
        {
            if (changeNextCallLifeTier) return orig(self, map, room, levelMaxDist) + GetDailyLife();
            return orig(self, map, room, levelMaxDist);
        }

        private static int OnGetDmgTier(Hook_MobsGen.orig_getDmgTier orig, MobsGen self, LevelMap map, Room room, int levelMaxDist)
        {
            if (changeNextCallDmgTier) return orig(self, map, room, levelMaxDist) + GetDailyDmg();
            return orig(self, map, room, levelMaxDist);
        }
    }
}