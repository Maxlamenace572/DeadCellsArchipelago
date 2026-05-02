using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.PokeManager;
using dc.en;
using Serilog;
using ModCore.Utilities;
using HaxeProxy.Runtime;
using dc.ui;
using dc.ui.pause;
using dc.hxd.res;
using dc.tool;
using dc.tool._Cooldown;
using dc.ui.hud;

namespace DeadCellsArchipelago {
    public static class HeroManager
    {
        public static string userWithSkillIssue = "";
        public static bool deathLinkReceived = false;
        public static bool resetOnNextPrisonStart = false;
        public static Dictionary<int, Control> Controls { get; set; } = [];
        public static Cooldown? cooldown = null;
        public static bool trapChallenge = false;
        public static bool trapChallengeStartEntered = false;
        public static bool trapChallengeCurseReceived = false;

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
                    resetOnNextPrisonStart = true;
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
                trapChallenge = false;
                trapChallengeStartEntered = false;
                trapChallengeCurseReceived = false;
            }
        }

        public static void OnHeroInit(Hook_Hero.orig_init orig, Hero self)
        {
            orig(self);
            HERO = self;
            
            Log.Information("=== Hero initialized ! ===");
        }

        public static void InitSwitchControls()
        {
            SwitchControls();
            cooldown = new Cooldown(60, (dc.String str, int nb) =>
            {
                SwitchControls();
            });
            
            int key = Cooldown.Class.INDEXES.indexOf("InvertCooldown", null);

            if (key == -1)
            {
                Cooldown.Class.INDEXES.push("InvertCooldown");
                key = Cooldown.Class.INDEXES.length - 1;
            }

            var cdInst = new CdInst(key, 20);
            cooldown.cdList.push(cdInst);
        }

        public static void SwitchControls()
        {
            Invert(0, 1); //jump and roll
            Invert(2, 3); //main and secondary attack
            Invert(4, 5); //skill right and left
            Invert(7, 28); //heal and homo rune
            Invert(10, 12); //up/down
            Invert(11, 13); //left/right
        }

        public static void Invert(int control1, int control2)
        {
            if (HERO != null)
            {
                Control c1 = Controls[control1];
                Control c2 = Controls[control2];
                HERO.controller.parent.bind(control1, c2.padKeyA, c2.padKeyB, c2.padKeyC, c2.keyboardKey, c2.alternate1, c2.alternate2, true);
                HERO.controller.parent.bind(control1, c2.padKeyA, c2.padKeyB, c2.padKeyC, c2.keyboardKey, c2.alternate1, c2.alternate2, false);
                HERO.controller.parent.bind(control2, c1.padKeyA, c1.padKeyB, c1.padKeyC, c1.keyboardKey, c1.alternate1, c1.alternate2, true);
                HERO.controller.parent.bind(control2, c1.padKeyA, c1.padKeyB, c1.padKeyC, c1.keyboardKey, c1.alternate1, c1.alternate2, false);
            }
        }

        public static void RemoveARandomWeapon()
        {
            if(HERO != null)
            {
                List<InventItem> items = new List<InventItem>();
                for(int i = 0; i < 2; i++)
                {
                    InventItem iiw = HERO.inventory.getEquippedWeaponOn(i);
                    InventItem iis = HERO.inventory.getActiveOn(i);
                    if(iiw != null)
                    {
                        items.Add(iiw);
                    }
                    if(iis != null)
                    {
                        items.Add(iis);
                    }
                }
                if(items.Count > 0)
                {
                    InventItem ii = items[new Random().Next(0, items.Count)];
                    HERO.inventory.remove(ii);
                    
                    bool updateHUD = true;
                    bool durings = false;
                    HERO.onEquipedItemsChange(new Ref<bool>(ref updateHUD), new Ref<bool>(ref durings), new Ref<bool>(ref durings));
                }
            }
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

        public static void OnBind(Hook_Controller.orig_bind orig, Controller self, int k, int? padKeyA, int? padKeyB, int? padKeyC, int? keyboardKey, int? alternate1, int? alternate2, bool? forceBindings_normal)
        {
            if (forceBindings_normal == false)
            {
                if (new[] {0, 1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 28}.Contains(k))
                {
                    Controls[k] = new Control
                    {
                        padKeyA = padKeyA,
                        padKeyB = padKeyB,
                        padKeyC = padKeyC,
                        keyboardKey = keyboardKey,
                        alternate1 = alternate1,
                        alternate2 = alternate2,
                        forceBindings_normal = forceBindings_normal
                    };
                }
            }
            orig(self, k, padKeyA, padKeyB, padKeyC, keyboardKey, alternate1, alternate2, forceBindings_normal);
        }
    }
}