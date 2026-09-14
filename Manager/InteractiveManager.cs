using dc.en;
using dc.en.inter;
using dc.en.inter.npc;
using ModCore.Utilities;
using Serilog;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class InteractiveManager
    {
        public static void InitializeInteractiveHooks()
        {
            Log.Information("[AP] Loading Interactive Hooks...");
            
            Hook_AspectMaster.onActivate += NoAspectActivate;
            Hook_UpgradeShrine.onActivate += OnOnActivateUpgradeShrine;
            Hook_RunicShrine.onActivate += OnOnActivateRunicShrine;

            Log.Information("[AP] Interactive Hooks loaded");
        }

        private static void OnOnActivateUpgradeShrine(Hook_UpgradeShrine.orig_onActivate orig, UpgradeShrine self, Hero by, bool lp)
        {
            switch (self.item._itemData.id.ToString())
            {
                case "AnyUp":
                    SAVED_DATA!.tripleUpsTaken++;
                    break;
                case "BTUp":
                case "BSUp":
                case "TSUp":
                    SAVED_DATA!.doubleUpsTaken++;
                    break;
            }
            
            orig(self, by, lp);
        }

        private static void OnOnActivateRunicShrine(Hook_RunicShrine.orig_onActivate orig, RunicShrine self, Hero by, bool lp)
        {
            if (self.item._itemData.id.ToString() == "QuarterUp")
            {
                if (self.neededRunes == 3) SAVED_DATA!.quarterUpsBC3Taken++;
                else if (self.neededRunes == 4) SAVED_DATA!.quarterUpsBC4Taken++;
            }
            orig(self, by, lp);
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