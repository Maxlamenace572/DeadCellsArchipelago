using dc;
using dc.en;
using dc.en.mob;
using dc.en.mob.boss;
using dc.en.mob.boss.death;
using dc.hl.types;
using ModCore.Utilities;
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
            Hook_Death.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };

            Hook_TimeKeeper.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Giant.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_GardenerBoss.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };

            Hook_KingsHand.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };

            Hook_AmazonBrutal.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_AmazonTactic.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_AmazonSurvival.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };

            Hook_Queen.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_DookuBeast.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };
            Hook_Collector.onDie += (orig, self) => { orig(self); OnBossKilled(self._infos.id.ToString()); };

            Hook_Mob.onDie += OnOnDie;
            
            Log.Information("=== Boss Hooks loaded ! ===");
        }

        private static void OnBossKilled(string bossName)
        {
            if (SAVED_DATA != null && !SAVED_DATA.IsCheckSent(bossName)){
                SendBossCheck(bossName);
            }
            switch(bossName)
            {
                case "KingsHand":
                case "Collector":
                case "Queen":
                case "DookuBeast":
                    disableTrapOnEndBoss = true;
                    if (ARCHIPELAGO != null && SAVED_DATA != null && USER != null &&
                        SAVED_DATA.bscLevelToWin == USER.bossRuneActivated)
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
                ARCHIPELAGO.SendCheck("Boss_" + bossName, bossName, "Boss:");
            }
            else
            {
                Log.Error("=== Error while sending Boss check ===");
            }
        }

        public static void SendUTBossCheckHelper(string bossName)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("D_" + bossName, bossName, "Boss:");
            }
            else
            {
                Log.Error("=== Error while sending Boss check ===");
            }
        }

        public static void OnOnDie(Hook_Mob.orig_onDie orig, Mob self)
        {
            orig(self);

            int randomNumber = new Random().Next(1, 1001);
            if (randomNumber == 1)
            {
                DropItemToPlayer("TimeDistorsion");
            }
        }
        
        public static void TempFixRemoveFromLoot(Hook_Mob.orig_removeFromLoot orig, Mob self, LootType k)
        {
            //This is a fix for a bug in dccm 35.9.23. 
            //The first LootType with a matching Index is removed instead of removing the one with matching values.
            //Once the bug is resolved in dccm, this hook should be deleted.
            int i = 0;
            foreach (LootType loot in self.loots)
            {
                if (loot is LootType.Blueprint && ((LootType.Blueprint) loot).Param0.ToString() == ((LootType.Blueprint) k).Param0.ToString())
                {
                    ArrayObj ar1 = (ArrayObj) self.loots.splice(0, i);
                    ArrayObj ar2 = (ArrayObj) self.loots.splice(i+1, self.loots.length-i-1);
                    self.loots = ar1.concat(ar2);
                }
                i++;
            }
        }
    }
}