using dc.en;
using dc.en.loot;
using ModCore.Mods;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.BossManager;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.BlueprintManager;

namespace DeadCellsArchipelago{
    //E:\SteamLibrary\steamapps\common\Dead Cells\coremod\core\host\startup -> path to launch DeadCellsModding.exe
    public class ModEntry(ModInfo info) : ModBase(info)
    {
        private Hero? hero;
        public override void Initialize()
        {
            Log.Information("=== Archipelago Mod is loading... ===");

            InitializeBossHooks();

            Hook_Hero.init += OnHeroInit;

            Hook_Hero.pickBlueprint += OnBlueprintPicked;
            Hook_Hero.hasBlueprint += ReallyHasBlueprint;

            Log.Information("=== Archipelago Mod loaded ! ===");
        }

        private void OnHeroInit(Hook_Hero.orig_init orig, Hero self)
        {
            orig(self);
            hero = self;
            ItemManager.HERO = self;
            BlueprintManager.HERO = self;
            
            Log.Information($"=== Hero initialized ! ===");
            //giving an item to a player saved at a level transition do nothing or errors (can pose future problems)
            //LogInventory();
            GiveItemToPlayer("DiverseDeckWatcher");
            GiveItemToPlayer("AnyUp");
            GiveItemToPlayer("LegendGem");
            UnlockBlueprint("FastBow");
            UnlockBlueprint("EvilSword");
            UnlockBlueprint("FastBow");
            UnlockBlueprint("BackStabber");
        }
    }
}