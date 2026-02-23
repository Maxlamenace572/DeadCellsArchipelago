using dc.en;
using dc.en.loot;
using ModCore.Mods;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.BossManager;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.BlueprintManager;
using dc.en.mob;
using dc._Data;
using dc.pr;
using dc.level;
using dc.tool;
using ModCore.Events.Interfaces.Game.Save;
using Newtonsoft.Json;
using dc;


namespace DeadCellsArchipelago{
    //E:\SteamLibrary\steamapps\common\Dead Cells\coremod\core\host\startup -> path to launch DeadCellsModding.exe
    public class ModEntry(ModInfo info) : ModBase(info), 
        IOnAfterLoadingSave,
        IOnBeforeSavingSave
    {
        private ArchipelagoSaveData savedData = new();
        private Hero? hero;
        public override void Initialize()
        {
            Log.Information("=== Archipelago Mod is loading... ===");

            InitializeBossHooks();

            Hook_Hero.init += OnHeroInit;

            Hook_Hero.pickBlueprint += OnBlueprintPicked;
            Hook_ItemMetaManager.hasRevealedItem += ReallyHasBlueprint;;

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
            /*GiveItemToPlayer("DiverseDeckWatcher");
            GiveItemToPlayer("AnyUp");
            GiveItemToPlayer("LegendGem");
            UnlockBlueprint("FastBow");
            UnlockBlueprint("EvilSword");
            UnlockBlueprint("FastBow");
            UnlockBlueprint("BackStabber");*/
        }

        public void OnAfterLoadingSave(User data)
        {
            savedData = new();
            if (data != null)
            {
                Log.Information($"=== Chargement de la save slot {data.userId} ===");
                
                // Charger les données Archipelago pour ce slot
                var savePath = GetSaveFilePath(data.userId);
                if (System.IO.File.Exists(savePath))
                {
                    try
                    {
                        var json = System.IO.File.ReadAllText(savePath);
                        savedData = JsonConvert.DeserializeObject<ArchipelagoSaveData>(json) ?? new();
                        
                        Log.Information($"=== Données chargées : {savedData.SentChecks.Count} checks envoyés ===");
                    }
                    catch (Exception ex)
                    {
                        Log.Error($"=== Erreur chargement save : {ex.Message} ===");
                    }
                }
            }
            else
            {
                Log.Information($"=== New Save ===");
            }
            BlueprintManager.SAVED_DATA = savedData;
        }
        
        public void OnBeforeSavingSave(IOnBeforeSavingSave.EventData data)
        {
            Log.Information($"=== Sauvegarde slot {data.Data.userId} ===");
            
            var savePath = GetSaveFilePath(data.Data.userId);
            try
            {
                var json = JsonConvert.SerializeObject(savedData, Formatting.Indented);
                System.IO.File.WriteAllText(savePath, json);
                
                Log.Information($"=== Sauvegarde réussie : {savedData.SentChecks.Count} checks ===");
            }
            catch (Exception ex)
            {
                Log.Error($"=== Erreur sauvegarde : {ex.Message} ===");
            }
        }
        
        private string GetSaveFilePath(int slot)
        {
            var saveDir = "./coremod/mods/DeadCellsArchipelago/data";
            
            Directory.CreateDirectory(saveDir);
            return System.IO.Path.Combine(saveDir, $"archipelagoUserId_{slot}.json");
        }
    }
}