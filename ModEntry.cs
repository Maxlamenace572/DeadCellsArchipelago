using dc.en;
using ModCore.Mods;
using Serilog;

using static DeadCellsArchipelago.BossManager;
using static DeadCellsArchipelago.ItemManager;

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

            Log.Information("=== Archipelago Mod loaded ! ===");
        }


        private void OnHeroInit(Hook_Hero.orig_init orig, Hero self)
        {
            orig(self);
            hero = self;
            HERO = self;
            
            Log.Information($"=== Hero initialized ! ===");
            //will be removed, but giving an item to a player saved at a level transition do nothing (can pose future problems)
            LogInventory();
            //test each category
            GiveItemToPlayer("HeavyTurret");
            GiveItemToPlayer("FastGrenade");
            GiveItemToPlayer("SideTurret");
            GiveItemToPlayer("SlowOrb");
            GiveItemToPlayer("AdminWeapon");
            GiveItemToPlayer("ExplosiveCrossBow");
            GiveItemToPlayer("IceShield");
            GiveItemToPlayer("Immortality");
            GiveItemToPlayer("MariaCatKey");
            GiveItemToPlayer("BreakableGroundKey");
            GiveItemToPlayer("AnyUp");
            GiveItemToPlayer("LegendGem");
            GiveItemToPlayer("P_ManyMobsAround");
            GiveItemToPlayer("PrisonerGold");
            GiveItemToPlayer("HandOfTheKingFlame");
            GiveItemToPlayer("ASP_ToxinLover");
            GiveItemToPlayer("BRS_Skull");
        }
    }
}