using dc.en;
using ModCore.Utilities;
using Serilog;

namespace DeadCellsArchipelago {
    public static class BlueprintManager
    {
        public static Hero? HERO { get; set; }
        
        public static bool OnBlueprintPicked(Hook_Hero.orig_pickBlueprint orig, Hero self, dc.String k)
        {
            if (k.substring(0, 1).ToString() == "#")    //if the id start with a '#', it's comming from archipelago and we need to unlock it
            {
                //TODO: let the drop of this game blueprint
                Log.Information($"=== Blueprint unlocked : {k.substring(1, null)} ===");
                orig(self, k.substring(1, null));
            }
            else    //else, it's comming from the game and we need to send a archipelago check //
            {
                //TODO: disable the drop of the archipelago blueprint
                Log.Information($"=== Blueprint picked up : {k} ===");
                // TODO: envoyer le check Archipelago
            }

            return true;
        }

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

        //todo: hasBlueprint may be the check the allow or not the blueprint to spawn
        public static bool ReallyHasBlueprint(Hook_Hero.orig_hasBlueprint orig, Hero self, dc.String k)
        {
            Log.Warning($"=== Calling this method ===");
            return false;
        }
    }
}