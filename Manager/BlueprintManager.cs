using dc.en;
using dc.tool;
using dc.ui;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class BlueprintManager
    {
        public static bool showBlueprintLog = false;

        //Called when the hero get a blueprint, picked in game or by UnlockBlueprint.
        public static bool OnBlueprintPicked(Hook_Hero.orig_pickBlueprint orig, Hero self, dc.String k)
        {
            //the blueprint is comming from the game, so we need to send a archipelago check
            if(ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics))
            {
                SendBlueprintCheck(k.ToString());
                return true;
            }
            return orig(self, k);
        }

        //Instantly unlock the blueprint
        public static void UnlockBlueprint(string blueprintId)
        {
            if (HERO != null && ITEM_META_MANAGER != null)
            {
                try
                {
                    ITEM_META_MANAGER.revealItem(blueprintId.AsHaxeString(), true);
                    Log.Information($"=== Blueprint unlocked:  {blueprintId} ===");
                }
                catch (Exception ex)
                {
                    Log.Error($"=== Error while giving blueprint: {ex.Message} ===");
                }
            }
        }

        //hasRevealedItem allow or not the blueprint to spawn
        public static bool ReallyHasBlueprint(Hook_ItemMetaManager.orig_hasRevealedItem orig, ItemMetaManager self, dc.String k)
        {
            if(ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics))
            {
                return SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString()); //Drop the blueprint only when he is not in the saved checklist
            }
            return orig(self, k);
        }

        public static void SendBlueprintCheck(string blueprintId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("Blueprint_" + blueprintId, blueprintId, "Blueprint:");
            }
            else
            {
                Log.Error("=== Error while sending blueprint check ===");
            }
        }

        public static void BlueprintUILog(Hook_LogManager.orig_blueprint orig, LogManager self, dc.String k, dc.String baseRarity, bool isRevealed, bool isScoring)
        {
            if (showBlueprintLog)
            {
                orig(self, k, baseRarity, isRevealed, isScoring);
            }
            if (ARCHIPELAGO != null && !ARCHIPELAGO.includeCosmetics && InCosmeticList(k.ToString()))
            {
                orig(self, k, baseRarity, isRevealed, false);
            }
        }

        public static void HeadUILog(Hook_LogManager.orig_head orig, LogManager self, dc.String headKind)
        {
            if (ARCHIPELAGO != null && !ARCHIPELAGO.includeCosmetics)
            {
                orig(self, headKind);
            }
        }
    }
}