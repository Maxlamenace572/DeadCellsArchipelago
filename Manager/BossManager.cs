using dc;
using dc.en;
using dc.en.mob;
using dc.en.mob.boss;
using dc.en.mob.boss.death;
using Serilog;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class BossManager
    {
        public static void InitializeBossHooks()
        {
            Log.Information("[AP] Loading Boss Hooks...");
            
            Hook_Behemoth.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_Beholder.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_MamaTick.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_Death.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };

            Hook_TimeKeeper.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_Giant.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_GardenerBoss.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };

            Hook_KingsHand.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };

            Hook_AmazonBrutal.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_AmazonTactic.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_AmazonSurvival.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };

            Hook_Queen.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_DookuBeast.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            Hook_Collector.onDie += (orig, self) => { OnBossKilled(self._infos.id.ToString()); orig(self); };
            
            Log.Information("[AP] Boss Hooks loaded");
        }

        private static void OnBossKilled(string bossName)
        {
            if (HERO!.noDamageDuringBossBattle == true)
            {
                GLOBAL_DATA!.FlawlessBoss.Add(bossName);
            }

            if (IsBossHead(bossName) && GLOBAL_DATA != null)
            {
                if (!GLOBAL_DATA.BossHeadKilled.ContainsKey(bossName)) GLOBAL_DATA.BossHeadKilled[bossName] = 0;
                GLOBAL_DATA.BossHeadKilled[bossName]++;
                GLOBAL_DATA.SaveGlobalSaveJson();
            }

            if (SAVED_DATA != null && !SAVED_DATA.IsCheckSent("Boss_" + bossName)){
                SendBossCheck(bossName);
                SendUTBossCheckHelper(bossName);
            }
            switch(bossName)
            {
                case "KingsHand":
                case "Collector":
                case "Queen":
                case "DookuBeast":
                    disableTrapOnEndBoss = true;
                    if (ARCHIPELAGO != null && GLOBAL_DATA != null && USER != null &&
                        GLOBAL_DATA.bscLevelToWin == USER.bossRuneActivated)
                    {
                        ARCHIPELAGO.SendVictory();
                    }
                    break;

                case "Behemoth":
                    if(USER != null && USER.game.isScoring())
                    {
                        if(SAVED_DATA != null && SAVED_DATA.IsCheckSent("SpeedBlade") && SAVED_DATA.IsCheckSent("DamageAura") && SAVED_DATA.IsCheckSent("DashSword"))
                        {
                            SAVED_DATA.AddFillerItem("Pokebomb");
                        }
                    }
                    break;
            }
        }

        public static void SendBossCheck(string bossName)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("Boss_" + bossName);
            }
            else
            {
                SAVED_DATA?.SaveOfflineCheck("Boss_" + bossName);
            }
        }

        public static void SendUTBossCheckHelper(string bossName)
        {
            if (bossName.ToString().Length >= 6 && bossName.ToString()[..6] == "Amazon") return;

            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("D_" + bossName);
            }
            else
            {
                SAVED_DATA?.SaveOfflineCheck("D_" + bossName);
            }
        }

        public static bool IsBossHead(string mob)
        {
            return new [] {"Behemoth", "Beholder", "MamaTick", "TimeKeeper", "Giant", "GardenerBoss", "KingsHand", "Queen",
                "Collector", "AmazonBrutal", "AmazonTactic", "AmazonSurvival"}.Any(mob.Contains);
        }
    }
}