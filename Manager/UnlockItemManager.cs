using dc.en.hero;
using dc.level.@struct;
using Hashlink.Virtuals;
using HaxeProxy.Runtime;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class UnlockItemManager
    {
        //here should be every item that decided not to do as the others, and have a hasUnlockedItem on them

        public static void OnDisplayCursePopup(Hook_Beheaded.orig_displayCursePopup orig, Beheaded self, int count, dc.String reason, Ref<bool> hidePopup)
        {//BlackHoleWhite
            useModdedHasUnlock = true;
            orig(self, count, reason, hidePopup);
            useModdedHasUnlock = false;
        }

        public static bool OnCanGenerateThisLoreRoomShipwreck(Hook_Shipwreck.orig_canGenerateThisLoreRoom orig, Shipwreck self, virtual_arc_examinables_fxEmitters_Intention_levels_onlyUseOnce_rarity_requiredLore_requiredMeta_room_roomLoot_sprites_status_structMode_ lore)
        {//Trident
            useModdedHasUnlock = true;
            var res = orig(self, lore);
            useModdedHasUnlock = false;
            return res;
        }
    }
}