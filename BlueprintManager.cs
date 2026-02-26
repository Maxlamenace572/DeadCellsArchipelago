using dc.en;
using dc.tool;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class BlueprintManager
    {
        //todo: fix; when the player have hitless bosses on another save, at the 3rd run, "FlawlessBehemoth", "FlawlessBeholder", "FlawlessAssassin", 
        // "FlawlessHotk", "FlawlessGiant", "FlawlessTick" and "FlawlessGardener" skin blueprints are automatically given.
        // I have completed the other 4 flawless (servents, queen, death, dracula), but they may be given later, should search. (maybe when biome unlocked ?)

        
        //Called when the hero get a blueprint, picked in game or by UnlockBlueprint.
        public static bool OnBlueprintPicked(Hook_Hero.orig_pickBlueprint orig, Hero self, dc.String k)
        {
            //the blueprint is comming from the game, so we need to send a archipelago check
            Log.Information($"=== Blueprint picked up: {k} ===");
            // TODO: send check to Archipelago
            SendBlueprintCheck(k.ToString());
            if (SAVED_DATA != null)
            {
                SAVED_DATA.SaveCheckSent(k.ToString());
            } else
            {
                Log.Error($"=== No save loaded for BlueprintManager ===");
            }

            return true;
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
        public static bool ReallyHasBlueprint(dc.tool.Hook_ItemMetaManager.orig_hasRevealedItem orig, dc.tool.ItemMetaManager self, dc.String k)
        {
            if (ITEMS != null && ITEMS.TryGetValue(k.ToString(), out ItemData? itemData) && itemData.IsBaseItem) //todo: may check that later, but if true, add each time the blueprint to the collector
            {
                return false;
            }
            else if (SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString())) //Drop the blueprint only when he is not in the saved checklist
            {
                return true;
            }
            return false;
        }

        public static void SendBlueprintCheck(string blueprintId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck($"Blueprint: {blueprintId}");
            }
            else
            {
                Log.Error($"=== Error while sending blueprint check ===");
            }
        }
    }
}