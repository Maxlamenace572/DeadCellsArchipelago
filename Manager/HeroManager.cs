using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.RoomManager;
using static DeadCellsArchipelago.PokeManager;
using dc.en;
using Serilog;
using ModCore.Utilities;
using HaxeProxy.Runtime;
using dc.ui;
using dc.ui.pause;
using dc.hxd.res;

namespace DeadCellsArchipelago {
    public static class HeroManager
    {
        public static string userWithSkillIssue = "";
        public static bool deathLinkReceived = false;

        public static void OnHeroDie(Hook_Hero.orig_onDie orig, Hero self)
        {
            heroJustDead = true;
            Log.Warning("=== It's a death ==="); //test for reset and complete run (I want to do it on reset but not on complete), and what happend when he quit
            orig(self);
            heroJustDead = false;
            aspectsToIter = 0;
            if(ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendDeathLink();
            }
            ResetDataNewRun();
        }

        public static void OnRestart(Hook__Confirmation.orig___constructor__ orig, Confirmation arg1, Process from, dc.String str, HlAction onValidate, HlAction onCancel, dc.String validateStr, dc.String cancelStr, Sound validSfx)
        {
            if(from is DefaultPause)
            {
                ResetFrontPokebomb();

                var originalOnValidate = onValidate;

                onValidate = () => {
                    ResetDataNewRun();
                    originalOnValidate.Invoke();
                };
            }
            orig(arg1, from, str, onValidate, onCancel, validateStr, cancelStr, validSfx);
        }

        public static void ResetDataNewRun()
        {
            if(SAVED_DATA != null)
            {
                SAVED_DATA.currentLevelId = "PrisonStart";
                SAVED_DATA.isDoingChallenge = false;
                SAVED_DATA.numberOfPokebombUse = 1;
            }
        }

        public static void OnHeroInit(Hook_Hero.orig_init orig, Hero self)
        {
            orig(self);
            HERO = self;
            
            Log.Information("=== Hero initialized ! ===");
        }

        public static void DieByDeathLink()
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
                userWithSkillIssue = "";
            }
        }

        public static void CheckDeathLink()
        {
            if(deathLinkReceived)
            {
                DieByDeathLink();
                deathLinkReceived = false;
            }
        }

        public static void OnAddCells(Hook_Hero.orig_addCells orig, Hero self, int v, Ref<bool> noStats)
        {
            v *= 4;
            orig(self, v, noStats);
        }
    }
}