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
            Hook_Behemoth.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Beholder.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_MamaTick.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Death.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); }; //need to be tested

            Hook_TimeKeeper.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Giant.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_GardenerBoss.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };

            Hook_KingsHand.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Fx.servantChaseDefeat += (orig, self, e) => { orig(self, e); OnBossKilled("TODO : servants "); }; //need to be tested
            Hook_Dooku.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); }; //might not use it, dracula first form

            Hook_Queen.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_DookuBeast.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Collector.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            
            Log.Information("=== Boss Hooks loaded ! ===");
        }

        private static void OnBossKilled(string bossName)
        {
            Log.Information($"=== {bossName} killed! TODO: send check to Archipelago ===");
            if (SAVED_DATA != null && !SAVED_DATA.IsCheckSent(bossName)){
                SendBossCheck(bossName);
            }
            switch(bossName)
            {
                case "KingsHand":
                case "Collector":
                case "Queen":
                case "DookuBeast":
                    if (ARCHIPELAGO != null && SAVED_DATA != null && USER != null &&
                        SAVED_DATA.bscLevelToWin == USER.bossRuneActivated)
                    {
                        ARCHIPELAGO.SendVictory();
                    }
                    break;
            }
        }

        public static void SendBossCheck(string bossName)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("Boss_" + bossName, bossName, "Boss:");
            }
            else
            {
                Log.Error("=== Error while sending Boss check ===");
            }
        }
    }
}