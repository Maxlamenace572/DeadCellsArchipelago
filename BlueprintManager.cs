using dc.en;
using ModCore.Storage;
using ModCore.Utilities;
using Serilog;

namespace DeadCellsArchipelago {
    public static class BlueprintManager
    {
        //todo: fix; when the player have hitless bosses on another save, at the 3rd run, "FlawlessBehemoth", "FlawlessBeholder", "FlawlessAssassin", 
        // "FlawlessHotk", "FlawlessGiant", "FlawlessTick" and "FlawlessGardener" skin blueprints are automatically given.
        // I have completed the other 4 flawless (servents, queen, death, dracula), but they may be given later, should search. (maybe when biome unlocked ?)
        public static Hero? HERO { get; set; }
        public static ArchipelagoSaveData? SAVED_DATA { get; set; }
        public static ArchipelagoManager? ARCHIPELAGO { get; set; }
        
        //Called when the hero get a blueprint, picked in game or by UnlockBlueprint.
        public static bool OnBlueprintPicked(Hook_Hero.orig_pickBlueprint orig, Hero self, dc.String k)
        {
            if (k.substring(0, 1).ToString() == "#")    //if the id start with a '#', it's comming from archipelago and we need to unlock it
            {
                Log.Information($"=== Blueprint unlocked : {k.substring(1, null)} ===");
                orig(self, k.substring(1, null));
            }
            else    //else it's comming from the game, and we need to send a archipelago check
            {
                Log.Information($"=== Blueprint picked up : {k} ===");
                // TODO: send check to Archipelago
                SendBlueprintCheck(k.ToString());
                if (SAVED_DATA != null)
                {
                    SAVED_DATA.SaveCheckSent(k.ToString());
                } else
                {
                    Log.Error($"=== No save loaded for BlueprintManager ===");
                }
            }

            return true;
        }

        //Instantly unlock the blueprint, without validating the archipelago check
        public static void UnlockBlueprint(string blueprintId)
        {
            if (HERO != null)
            {
                try
                {
                    var success = HERO.pickBlueprint(("#" + blueprintId).AsHaxeString());   //the '#' is a tag I use to distinguish between a blueprint given by archipelago and the game
                    HERO.revealBlueprints();
                    
                    if (!success)
                    {
                        Log.Warning($"=== Blueprint {blueprintId} already owned or not valid ===");
                    }
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
            if (SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString())) //Drop the blueprint only when he is not in the saved checklist
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