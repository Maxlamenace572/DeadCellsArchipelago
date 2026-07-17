using dc.en;
using dc.en.inter.npc;
using ModCore.Utilities;
using Serilog;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class NpcManager
    {
        public static void InitializeNpcHooks()
        {
            Log.Information("[AP] Loading Npc Hooks...");
            
            Hook_AspectMaster.onActivate += NoAspectActivate;

            Log.Information("[AP] Npc Hooks loaded");
        }
        
        private static void NoAspectActivate(Hook_AspectMaster.orig_onActivate orig, AspectMaster self, Hero by, bool lp)
        {
            if(SAVED_DATA != null && SAVED_DATA.HasReceivedAspect())
            {
                orig(self, by, lp);
            }
            else
            {
                string[] sentences = {
                    "You don't have any aspects.",
                    "Come back later!",
                    "There is nothing here!"
                };
                Random rnd = new Random();
                var index = rnd.Next(0, sentences.Length);
                self.say(sentences[index].AsHaxeString(), null, null, null);
            }
        }
    }
}