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
using static DeadCellsArchipelago.Translator;
using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.PokeManager;
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
using ModCore.Events.Interfaces.Game;
using ModCore.Events.Interfaces;
using dc.level.disp;
using dc.h2d.col;
using dc.en.gr;
using dc.pow;
using dc.ui.pause;
using dc.hxd.res;
using dc.ui.hud;
using dc.tool.weap.dual;


namespace DeadCellsArchipelago{
    //E:\SteamLibrary\steamapps\common\Dead Cells\coremod\core\host\startup -> path to launch DeadCellsModding.exe
    public class ModEntry(ModInfo info) : ModBase(info), 
        IOnAfterLoadingSave,
        IOnBeforeSavingSave,
        IOnHeroUpdate//,
        //IOn
    {
        private ArchipelagoManager archipelago = new();

        public override void Initialize()
        {
            Log.Information("=== Archipelago Mod is loading... ===");

            //TitleScreen

            Hook_TitleScreen.mainMenu += OnMainMenu;
            Hook_TitleScreen.onResize += OnOnResize;
            Hook_TitleScreen.playMenu += OnPlayMenu;
            Hook_Main.launchGame += OnLaunchGame;

            Hook_Pixels.convert += OnConvert;
            //UIDlc

            InitializeBossHooks();

            Hook_Hero.init += OnHeroInit;
            Hook_Hero.pickBlueprint += OnBlueprintPicked;
            Hook_Hero.applyItemPickEffect += OnApplyItemPickEffect; //used for runes
            Hook_Hero.onDie += OnHeroDie;
            Hook_Hero.addCells += OnAddCells;

            Hook_ItemMetaManager.hasRevealedItem += ReallyHasBlueprint; //might check rune
            Hook_ItemMetaManager.revealItem += OnRevealItem;
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
            Hook_ItemMetaManager.canInvestOnItem += OnCanInvestOnItem;
            Hook_AspectMaster.onActivate += NoAspectActivate;
            //AspectMaster
            //ItemMetaManager
            //InventItemKind
            //archipelago.EnableMockMode();
            // TODO: Get infos from ui
            //var confData = GetConfData();

            IdToApName = LoadModApTranslation();
            ApNameToId = Invert(IdToApName);
/*            archipelago.Connect(confData.serverIp, confData.slotName, confData.password);
            ARCHIPELAGO = archipelago;*/

            //dc.level.@struct.Throne

            //Exit
            //dc.pr.Game
            Hook_Exit.onActivate += OnActiviteExit;

            TextInput.Class.MAX_LENGTH = 50;

            Hook_LootGen.addBlueprintAt += FixNotSpawningBlueprint;

            Hook_Pokecharge.removeItem += OnRemoveItemPokecharge;
            //DefaultPause
            //dc.h2d.Interactive
            //botMenu
            //dc.pr.Game

            //Hook_ControllerAccess.onActPressed += OnActPressed;

            Hook__Confirmation.__constructor__ += OnRestart;
            Hook_Portal.onActivate += OnActivatePortal;
            Hook_Portal.close += OnClosePortal;

            Hook_HeroActiveSkillsManager.onActiveSkill += OnOnActiveSkill;
            Hook_HeroActiveSkillsManager.canUseActiveSkill += OnCanUseActiveSkill;
            Hook_HeroActiveSkillsManager.updateSkills += OnUpdateSkills;
            Hook_Inventory.swapSkills += OnSwapSkills;
            Hook_TreasureChest.onActivate += OnActivateTreasureChest;

            Hook_Controller.bind += OnBind;
            //Controller
            //HeroMainSkill
            //Challenge
            //LevelGen
            //ModCore.Utilities.ArrayUtils
            //dc.haxe.ds.
            Hook_LeaderboardPanel.set_visible += OnSetVisible;
            Log.Information("=== Archipelago Mod loaded ! ===");
        }

        public void OnHeroUpdate(double dt)
        {
            if (HERO != null && HERO.awake)
            {    
                GiveItemInQueue();
                CheckDeathLink();
            }

            if(cooldown != null)
            {
                cooldown.update(dt);
            }

            if (trapChallenge && USER != null && HERO != null)
            {
                Room room = USER.game.curLevel.map.getRoomAt(HERO.cx, HERO.cy);
                if (room != null)
                {
                    if (room.name.ToString() == "end")
                    {
                        LevelTransition.Class.gotoSub.Invoke(levelMapNotChallenge, null);
                        trapChallenge = false;
                        trapChallengeStartEntered = false;
                        HERO.reduceCurse(1);
                        trapChallengeCurseReceived = false;
                    }
                    if (room.name.ToString() == "start")
                    {
                        trapChallengeStartEntered = true;
                    }
                    if (!trapChallengeCurseReceived && trapChallengeStartEntered && room.name.ToString() != "start")
                    {
                        bool hidePopup = false;
                        bool useAltSound = false;
                        HERO.curse(1, "Archipelago Challenge Trap".AsHaxeString(), new Ref<bool>(ref hidePopup), new Ref<bool>(ref useAltSound));
                        trapChallengeCurseReceived = true;
                    }
                }
            }
        }

        public void OnAfterLoadingSave(User data)
        {
            SAVED_DATA = new();
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
                        SAVED_DATA = JsonConvert.DeserializeObject<ArchipelagoSaveData>(json) ?? new();
                        
                        Log.Information($"=== Données chargées : {SAVED_DATA.SentChecks.Count} checks envoyés ===");
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
            Log.Information($"=== {SAVED_DATA.numberOfPokebombUse} ===");
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
                var json = JsonConvert.SerializeObject(SAVED_DATA, Formatting.Indented);
                System.IO.File.WriteAllText(savePath, json);
                
                Log.Information($"=== Sauvegarde réussie : {SAVED_DATA?.SentChecks.Count} checks ===");
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
    }
}