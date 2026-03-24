using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.RoomManager;
using static DeadCellsArchipelago.ItemQueue;
using dc.en;
using Serilog;
using ModCore.Utilities;

namespace DeadCellsArchipelago {
    public static class HeroManager
    {
        public static void OnHeroDie(Hook_Hero.orig_onDie orig, Hero self)
        {
            lastLevel = null;
            heroJustDead = true;
            Log.Warning("=== It's a death ==="); //test for reset and complete run (I want to do it on reset but not on complete), and what happend when he quit
            orig(self);
            heroJustDead = false;
            aspectsToIter = 0;
            if(ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendDeathLink();
            }
        }

        public static void OnHeroInit(Hook_Hero.orig_init orig, Hero self)
        {
            orig(self);
            HERO = self;
            
            Log.Information("=== Hero initialized ! ===");
        }

        public static void DieByDeathLink(string userWithSkillIssue)
        {
            if(HERO != null && ARCHIPELAGO != null)
            {
                if(ARCHIPELAGO.deathLinkEnabled == 0)
                {
                    HERO.kill();
                }
                else if (ARCHIPELAGO.deathLinkEnabled > 0)
                {
                    bool hidePopup = false;
                    bool useAltSound = false;
                    HERO.curse(ARCHIPELAGO.deathLinkEnabled, $"{userWithSkillIssue} died !".AsHaxeString(), new HaxeProxy.Runtime.Ref<bool>(ref hidePopup), new HaxeProxy.Runtime.Ref<bool>(ref useAltSound));
                }
            }
        }
    }
}