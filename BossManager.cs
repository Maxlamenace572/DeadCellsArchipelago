using dc;
using dc.en.mob.boss;
using dc.en.mob.boss.death;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class BossManager
    {
        public static void InitializeBossHooks()
        {
            Log.Information("=== Loading Boss Hooks... ===");
            // Hooking boss death events
            Hook_Behemoth.onDie += (orig, self) => { orig(self); OnBossKilled("The Concierge"); };
            Hook_Beholder.onDie += (orig, self) => { orig(self); OnBossKilled("Conjunctivius"); };
            Hook_MamaTick.onDie += (orig, self) => { orig(self); OnBossKilled("Mama Tick"); };
            Hook_Death.onDie += (orig, self) => { orig(self); OnBossKilled("Death"); }; //need to be tested

            Hook_TimeKeeper.onDie += (orig, self) => { orig(self); OnBossKilled("The Time Keeper"); };
            Hook_Giant.onDie += (orig, self) => { orig(self); OnBossKilled("The Giant"); };
            Hook_GardenerBoss.onDie += (orig, self) => { orig(self); OnBossKilled("Scarecrow"); };

            Hook_KingsHand.onDie += (orig, self) => { orig(self); OnBossKilled("The Hand of the King"); };
            Hook_Fx.servantChaseDefeat += (orig, self, e) => { orig(self, e); OnBossKilled("The Servants"); }; //need to be tested
            Hook_Dooku.onDie += (orig, self) => { orig(self); OnBossKilled("Dracula"); }; //might not use it, dracula first form

            Hook_Queen.onDie += (orig, self) => { orig(self); OnBossKilled("The Queen"); };
            Hook_DookuBeast.onDie += (orig, self) => { orig(self); OnBossKilled("Dracula - Final Form"); };
            Hook_Collector.onDie += (orig, self) => { orig(self); OnBossKilled("The Collector"); };
            
            Log.Information("=== Boss Hooks loaded ! ===");
        }

        private static void OnBossKilled(string bossName)
        {
            Log.Information($"=== {bossName} killed! TODO: send check to Archipelago ===");
            // TODO: send check to Archipelago

            // Test give item to player if concierge
            if(bossName == "The Concierge")
            {
                for (int i = 0; i < 20; i++)
                {
                    GiveItemToPlayer("AnyUp");
                }
            }
        }
    }
}