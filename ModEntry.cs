using dc.en;
using dc.en.loot;
using ModCore.Mods;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.BossManager;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.BlueprintManager;
using static DeadCellsArchipelago.RuneManager;
using static DeadCellsArchipelago.RoomManager;
using static DeadCellsArchipelago.AchievementManager;
using static DeadCellsArchipelago.NpcManager;
using static DeadCellsArchipelago.HeroManager;
using static DeadCellsArchipelago.ItemQueue;
using dc.en.mob;
using dc._Data;
using dc.pr;
using dc.level;
using dc.tool;
using ModCore.Events.Interfaces.Game.Save;
using Newtonsoft.Json;
using System.Text.Json;
using dc;
using dc.hl.types;
using dc.cine;
using dc.hxd;
using dc.tool.hero;
using HaxeProxy.Runtime;
using dc.en.inter;
using dc.steam.ugc;
using Archipelago.MultiClient.Net.Models;
using dc.tool.utils;
using dc.level.@struct;
using dc.en.inter.door;
using dc.level.lore;
using dc.ui;
using Hashlink.Virtuals;
using ModCore.Events.Interfaces.Game.Hero;
using dc.uicore;
using dc.hl;
using dc.uicore.element;
using dc.achievements;
using dc.en.inter.npc;
using ModCore.Modules;


namespace DeadCellsArchipelago{
    //E:\SteamLibrary\steamapps\common\Dead Cells\coremod\core\host\startup -> path to launch DeadCellsModding.exe
    public class ModEntry(ModInfo info) : ModBase(info), 
        IOnAfterLoadingSave,
        IOnBeforeSavingSave,
        IOnHeroUpdate
    {
        private ArchipelagoManager archipelago = new();
        private ArchipelagoSaveData savedData = new();

        public override void Initialize()
        {
            Log.Information("=== Archipelago Mod is loading... ===");

            InitializeBossHooks();

            Hook_Hero.init += OnHeroInit;
            Hook_Hero.pickBlueprint += OnBlueprintPicked;
            Hook_Hero.applyItemPickEffect += OnApplyItemPickEffect; //used for runes
            Hook_Hero.onDie += OnHeroDie;

            Hook_ItemMetaManager.hasRevealedItem += ReallyHasBlueprint; //might check rune
            Hook_ItemMetaManager.revealAllBaseItems += ReallyRevealAllBaseItems;
            Hook_ItemMetaManager.unlockItem += OnUnlockItem;
            //hasPermanentItem (5559) is used on too many things. should check on what call it later for bsc
            Hook_ItemMetaManager.hasPermanentItem += ReallyHasPermanentItem;
            Hook_ItemMetaManager.addPermanentItem += OnAddPermanentItem;
            Hook_LevelGen.generate += OnLevelGenGenerate;
            dc.en.inter.Hook_Throne.nextScene += OnNextScene;
            
            InitializeRoomHooks();

            //PerkSelect;
            //TriggeredDoor;
            Hook_TriggeredDoor.onActivate += OnTriggeredDoorActivate;
            Hook_Door.closeFast += OnDoorCloseFast;

            //LevelGen
            Hook_LevelGen.generate += OnGenerate;

            
            Hook_SteamAchievementManager.isUnlocked += RemoveIsUnlocked;
            Hook_SteamAchievementManager.unlock += RemoveUnlock;
            Hook_SteamAchievementManager.shouldDisplayInGameNotification += RemoveShouldDisplayInGameNotification;

            Hook_LogManager.blueprint += BlueprintUILog;
            Hook_LogManager.head += HeadUILog;
            Hook_ItemMetaManager.hasUnlockedItem += OnHasUnlockedItem;
            Hook_ItemMetaManager.investOnItemProgress += OnInvestOnItemProgress;
            Hook_AspectMaster.onActivate += NoAspectActivate;
            //AspectMaster
            //ItemMetaManager
            //InventItemKind

            //archipelago.EnableMockMode();
            // TODO: Get infos from ui
            var confData = GetConfData();

            archipelago.Connect(confData.serverIp, confData.slotName, confData.password);
            ARCHIPELAGO = archipelago;

            Log.Information("=== Archipelago Mod loaded ! ===");
            //dc.level.@struct.Throne
        }

        public void OnHeroUpdate(double dt)
        {
            if (HERO != null)
            {    
                GiveItemInQueue();
            }
        }

        public void OnAfterLoadingSave(User data)
        {
            savedData = new();
            if (data != null)
            {
                ITEM_META_MANAGER = data.itemMeta;
                var items = ITEM_META_MANAGER.getAllUnlockedWeapons();

                if (items.length > 0)
                {
                    var hasNext = true;
                    var i = 0;
                    var item = items.getDyn(i);
                    while (hasNext)
                    {
                        Log.Information($"{i} : {item}");
                        i++;
                        item = items.getDyn(i);
                        if(item == null)
                        {
                            hasNext = false;
                        }
                    }
                }
                
                USER = data;

                Log.Information($"=== Chargement de la save slot {data.userId} ===");
                
                // Load Archipelago data for this game
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
            SAVED_DATA = savedData;
            if(ARCHIPELAGO != null)
            {
                SAVED_DATA.bscLevelToWin = ARCHIPELAGO.bscOption;
            }
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
            string saveDir = System.IO.Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data");
            
            Directory.CreateDirectory(saveDir);
            return System.IO.Path.Combine(saveDir, $"archipelagoUserId_{slot}.json");
        }

        private string GetConfFilePath()
        {
            return System.IO.Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "conf.json");
        }

        private ArrayObj OnLevelGenGenerate(Hook_LevelGen.orig_generate orig, LevelGen self, User user, int seed, Hashlink.Virtuals.virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_ ldat, Ref<bool> resetCount)
        {
            if(USER == null)
            {
                USER = user;
            }
            ITEM_META_MANAGER = user.itemMeta;
            var result = orig(self, user, seed, ldat, resetCount);
            return result;
        }

        private ConfData GetConfData()
        {
            var confPath = GetConfFilePath();
            var confData = new ConfData();
            if (System.IO.File.Exists(confPath))
            {
                var json = System.IO.File.ReadAllText(confPath);
                confData = JsonConvert.DeserializeObject<ConfData>(json) ?? new();
            }
            else
            {
                var json = JsonConvert.SerializeObject(confData, Formatting.Indented);
                System.IO.File.WriteAllText(confPath, json);
            }
            return confData;
        }
    }
}