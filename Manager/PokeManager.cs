using dc;
using dc.pow;
using dc.tool;
using dc.tool.hero;
using dc.ui;
using dc.ui.hud;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ImageManager;
using dc.hl.types;
using Serilog;

namespace DeadCellsArchipelago {
    public static class PokeManager
    {
        public static dc.h2d.Bitmap? fgDisabled = null;
        public static Text? nb = null;
        private static bool enemyDiedWhileExtracting = false;

        public static void InitializePokeHooks()
        {
            Log.Information("[AP] Loading Poke Hooks...");
            
            Hook_Pokecharge.removeItem += OnRemoveItemPokecharge;
            Hook_HeroActiveSkillsManager.updateSkills += OnUpdateSkills;
            Hook_HeroActiveSkillsManager.canUseActiveSkill += OnCanUseActiveSkill;
            Hook_HeroActiveSkillsManager.onActiveSkill += OnOnActiveSkill;
            Hook_Inventory.swapSkills += OnSwapSkills;
            Hook_User.getPokebombBlueprintFor += OnGetPokebombBlueprintFor;
            Hook_ItemMetaManager.hasRevealedItemOrInCollector += OnHasRevealedItemOrInCollector;
            Hook_Entity.popError += OnPopError;

            Log.Information("[AP] Poke Hooks loaded");
        }

        private static void OnRemoveItemPokecharge(Hook_Pokecharge.orig_removeItem orig, Pokecharge self)
        {
            orig(self);
            if (!enemyDiedWhileExtracting)
            {
                DropItemToPlayer("Pokebomb");
                if(SAVED_DATA != null) SAVED_DATA.numberOfPokebombUse --;
            }
            else enemyDiedWhileExtracting = false;
        }
        
        private static void OnUpdateSkills(Hook_HeroActiveSkillsManager.orig_updateSkills orig, HeroActiveSkillsManager self)
        {
            if(self.hudGetSkillPower(0).ii != null && self.hudGetSkillPower(0).ii._itemData.id.ToString() == "Pokebomb")
            {
                PokebombUI(self, 0);
            }
            else if(self.hudGetSkillPower(1).ii != null && self.hudGetSkillPower(1).ii._itemData.id.ToString() == "Pokebomb")
            {
               PokebombUI(self, 1);
            }
            orig(self);
        }

        public static void PokebombUI(HeroActiveSkillsManager heroActiveSkillsManager, int id)
        {
            if(SAVED_DATA != null)
            {
                if (SAVED_DATA.numberOfPokebombUse == 0 && fgDisabled == null)
                {
                    int frame = 0;
                    double XY = 0;
                    dc.h2d.Tile bgTileApMenu = Assets.Class.ui.getTile("walterWhite".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);

                    var scale = 30;
                    fgDisabled = new dc.h2d.Bitmap(bgTileApMenu, heroActiveSkillsManager.hudGetSkillPower(id).icon)
                    {
                        scaleX = scale,
                        scaleY = scale,
                        x = -scale/2,
                        y = -scale/2,
                        color = ColorVectorRGBA(0, 0, 0, 0.6),
                    };
                }

                double screenScale = dc.libs.Process.Class.CUSTOM_STAGE_WIDTH / 1920.0;
                double scaleT = 1.0/(3*screenScale);
                if (nb == null)
                {
                    nb = new Text(heroActiveSkillsManager.hudGetSkillPower(id).icon, true, false, new Ref<double>(ref scaleT), null, null);
                    nb.set_textColor(16777215);
                }
                nb.set_text(SAVED_DATA.numberOfPokebombUse.ToString().AsHaxeString());
                nb.x = -(nb.get_textWidth()*(1.0/3))/2;
                nb.y = -(nb.get_textHeight()*(1.0/3))/2;
            }
        }

        private static bool OnCanUseActiveSkill(Hook_HeroActiveSkillsManager.orig_canUseActiveSkill orig, HeroActiveSkillsManager self, int id)
        {
            Skill hudSkill = self.hudGetSkillPower(id);
            if (hudSkill.ii != null && hudSkill.ii._itemData.id.ToString() == "Pokebomb")
            {
                if(SAVED_DATA != null && SAVED_DATA.numberOfPokebombUse == 0)
                {
                    return false;
                }
            }
            return orig(self, id);
        }

        private static void OnOnActiveSkill(Hook_HeroActiveSkillsManager.orig_onActiveSkill orig, HeroActiveSkillsManager self, int id, double ratio)
        {
            Skill hudSkill = self.hudGetSkillPower(id);
            if (hudSkill.ii._itemData.id.ToString() == "Pokebomb")
            {
                ResetFrontPokebomb();
            }
            orig(self, id, ratio);
        }

        public static void ResetFrontPokebomb()
        {
            fgDisabled?.remove();
            nb?.remove();
            fgDisabled = null;
            nb = null;
        }

        private static void OnSwapSkills(Hook_Inventory.orig_swapSkills orig, Inventory self)
        {
            ResetFrontPokebomb();
            orig(self);
        }

        private static dc.String OnGetPokebombBlueprintFor(Hook_User.orig_getPokebombBlueprintFor orig, User self, dc.String k, ArrayObj invBlueprints)
        {
            useModdedHasUnlock = true;
            var res = orig(self, k, invBlueprints);
            useModdedHasUnlock = false;
            return res;
        }

        private static bool OnHasRevealedItemOrInCollector(Hook_ItemMetaManager.orig_hasRevealedItemOrInCollector orig, ItemMetaManager self, dc.String k)
        {
            if (useModdedHasUnlock && SAVED_DATA != null)
            {
                return SAVED_DATA.IsCheckSent(k.ToString());
            }
            return orig(self, k);
        }

        private static bool OnPopError(Hook_Entity.orig_popError orig, Entity self, dc.String str, int? col)
        {
            if (((dc.String) Lang.Class.t.texts.get("Échec".AsHaxeString())).ToString() == str.ToString()) enemyDiedWhileExtracting = true;
            return orig(self, str, col);
        }

        public static bool IsAnySkillPokebomb()
        {
            HeroActiveSkillsManager asm = HERO!.activeSkillsManager;
            return (asm.hudGetSkillPower(0).ii != null && asm.hudGetSkillPower(0).ii._itemData.id.ToString() == "Pokebomb") || (asm.hudGetSkillPower(1).ii != null && asm.hudGetSkillPower(1).ii._itemData.id.ToString() == "Pokebomb");
        }
    }
}