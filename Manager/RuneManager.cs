using dc;
using dc.en;
using dc.en.inter;
using dc.hl.types;
using dc.tool;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class RuneManager
    {
        public static bool useOriginalHasPermanentItem { get; set;} = true;

        public static void OnApplyItemPickEffect(Hook_Hero.orig_applyItemPickEffect orig, Hero self, Entity from, InventItem i)
        {   //called each time the player take any item not blueprint
            Log.Warning($"=== pick effect on {i._itemData.id} ===");
            switch (i._itemData.id.ToString())
            {
                case "LadderKey":
                case "TeleportKey":
                case "ScoringKey":
                case "CustomKey":
                case "BreakableGroundKey":
                case "WallJumpKey":
                case "HomKey":
                case "ExploKey":
                    SendRuneCheck(i._itemData.id.ToString());
                    break;
                case "BossRune1":
                case "BossRune2":
                case "BossRune3":
                case "BossRune4":
                case "BossRune5":
                    SendBscCheck(i._itemData.id.ToString());
                    break;
                default:
                    orig(self, from, i);
                    break;
            }
        }

        public static void ActivateMinimapTracking(string itemName)
        {
            if (USER != null)
            {
                if (itemName == "LadderKey")
                {
                    ArrayObj array = USER.game.curLevel.entitiesByClass.get(35400); //35400 is the internal id for VineLadder
                    for (int i = 0; i < array.length; i++)
                    {
                        VineLadder vineLadder = (VineLadder) array.getDyn(i);
                        vineLadder.minimapTracking();
                    }
                }
                else if (itemName == "TeleportKey")
                {
                    ArrayObj array = USER.game.curLevel.entitiesByClass.get(23651); //23651 is the internal id for RedTeleporter
                    for (int i = 0; i < array.length; i++)
                    {
                        RedTeleporter redTeleporter = (RedTeleporter) array.getDyn(i);
                        redTeleporter.minimapTracking();
                    }
                }
                else if (itemName == "BreakableGroundKey")
                {
                    ArrayObj array = USER.game.curLevel.entitiesByClass.get(32866); //32866 is the internal id for BreakableGround
                    for (int i = 0; i < array.length; i++)
                    {
                        BreakableGround breakableGround = (BreakableGround) array.getDyn(i);
                        breakableGround.minimapTracking();
                    }
                }
            }
        }

        public static void SendRuneCheck(string runeId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("Rune_" + runeId, runeId, "Rune:");
            }
            else
            {
                Log.Error("=== Error while sending Rune check ===");
            }
        }

        public static bool ReallyHasPermanentItem(Hook_ItemMetaManager.orig_hasPermanentItem orig, ItemMetaManager self, dc.String k)
        {
            if(k.ToString() != "WallJumpKey" && k.ToString() != "BackpackUnlock" && k.ToString() != "ExploKey")
            {
                Log.Error($"=== rune {k} {useOriginalHasPermanentItem} {SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString())}===");
            }
            if (useOriginalHasPermanentItem) //this flag should change to false only when generating rooms, to have rune arena
            {
                return orig(self, k);
            }
            return SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString()); //If we already have the rune check, don't generate the arena
        }

        public static void SendBscCheck(string bscId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("BSC_" + bscId, bscId, "BSC:");
            }
            else
            {
                Log.Error("=== Error while sending BSC check ===");
            }
        }

        public static void OnNextScene(Hook_Throne.orig_nextScene orig, Throne self, Hero by)
        { //for HomKey
            useOriginalHasPermanentItem = false;
            orig(self, by);
            useOriginalHasPermanentItem = true;
        }

        public static bool OnAddPermanentItem(Hook_ItemMetaManager.orig_addPermanentItem orig, ItemMetaManager self, dc.String k)
        { //for HomKey
            if(useOriginalHasPermanentItem)
            {
                return orig(self, k);
            }
            SendRuneCheck(k.ToString());
            return false;
        }
    }
}