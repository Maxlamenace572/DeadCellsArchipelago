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
using static DeadCellsArchipelago.EnemyManager;
using static DeadCellsArchipelago.PauseMenuManager;
using static DeadCellsArchipelago.UnlockItemManager;
using dc.pr;
using dc.level;
using dc.tool;
using ModCore.Events.Interfaces.Game.Save;
using Newtonsoft.Json;
using dc;
using dc.hl.types;
using dc.cine;
using dc.hxd;
using dc.tool.hero;
using HaxeProxy.Runtime;
using dc.en.inter;
using dc.level.@struct;
using dc.en.inter.door;
using dc.ui;
using Hashlink.Virtuals;
using ModCore.Events.Interfaces.Game.Hero;
using dc.achievements;
using dc.en.inter.npc;
using ModCore.Events.Interfaces.Game;
using dc.pow;
using dc.ui.pause;
using dc.en.hero;
using dc.tool.bossRush;
using dc.hxd.snd;
using dc.ui.icon;
using dc.en.mob;
using dc.level.lore;


namespace DeadCellsArchipelago{
    //E:\SteamLibrary\steamapps\common\Dead Cells\coremod\core\host\startup -> path to launch DeadCellsModding.exe
    public class ModEntry(ModInfo info) : ModBase(info), 
        IOnAfterLoadingSave,
        IOnBeforeSavingSave,
        IOnHeroUpdate,
        IOnAfterLoadingCDB
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
            Hook_CollectorPanel.userFilter += OnUserFilter;
            Hook_ItemMetaManager.countUnlockedItems += OnCountUnlockedItems;
            Hook_LootGen.generateLootOnMobs += OnGenerateLootOnMobs;
            Hook_Hero.hudInitItems += OnHudInitItems;

            //DefaultPause
            //dc.h2d.Layers
            Hook_DefaultPause.update += OnUpdateDefaultPause;
            Hook_Inventory.swapSkills += OnSwapSkillsApMenu;
            Hook_Inventory.swapWeapons += OnSwapWeaponsApMenu;
            Hook_TrainingDoor.onActivate += OnActivateTrainingDoor;
            Hook_User.getPokebombBlueprintFor += OnGetPokebombBlueprintFor;
            Hook_ItemMetaManager.hasRevealedItemOrInCollector += OnHasRevealedItemOrInCollector;
            Hook_User.getDailyRewards += OnGetDailyRewards;
            Hook_MobsGen.getDmgTier += OnGetDmgTier;
            Hook_MobsGen.getLifeTier += OnGetLifeTier;
            UnlockItemHooks();
            Hook__RewardPopup.__constructor__ += OnRewardPopup;
            Hook__Achievements.hasAchievement += OnHasAchievement;
            Hook__Achievements.setAchievement += OnSetAchievement;
            Hook__ItemTools.getBlueprintLocalizedName += OnGetBlueprintLocalizedName;
            Hook__Icon.createItemIcon += OnCreateItemIcon;
            dc.en.Hook_Mob.removeFromLoot += TempFixRemoveFromLoot;
            Log.Information("=== Archipelago hooks loaded ! ===");
            //LogManager
            //BrBlueprint
            //BossRushData
        }

        public void OnHeroUpdate(double dt)
        {
            if (HERO != null && HERO.awake)
            {    
                GiveItemInQueue();
                ShowLogInQueue();
                CheckDeathLink();

                if (shouldGiveItemsNewRun && SAVED_DATA != null)
                {
                    shouldGiveItemsNewRun = false;
                    if (SAVED_DATA.IsItemReceived("ShipwreckKey"))
                    {
                        GiveItemToPlayer("ShipwreckKey");
                        HERO?.hudInitItems();
                    }

                    if (ARCHIPELAGO != null && ARCHIPELAGO.respawnUpScroll)
                    {
                        foreach (string itemName in GetUpScrolls())
                        {
                            SAVED_DATA.GivenFillerItem[itemName] = 0;
                        }
                    }
                }
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

                        if (ARCHIPELAGO != null && loadDataInPlayMenu == 1)
                        {
                            ARCHIPELAGO.SyncAll();
                            loadDataInPlayMenu = 0;
                        }
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
                if (ARCHIPELAGO != null && loadDataInPlayMenu == 2)
                {
                    ARCHIPELAGO.SyncAll();
                    loadDataInPlayMenu = 0;
                }
            }
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
            var result = orig(self, user, seed, ldat, resetCount);
            return result;
        }

        public void OnAfterLoadingCDB(_Data_ cdb)
        {
            Dictionary<string, int> newHeadsCount = BossHeadsCount();
            foreach (KeyValuePair<string, int> head in newHeadsCount)
            {
                var itemPropsDyn = (HaxeDynObj) cdb.item.byId.get(head.Key.AsHaxeString()).props;
                var itemProps = itemPropsDyn.ToVirtual<virtual_ang_aoeDuration_bonus_buff_bump_castTime_chance_color_color2_cooldown_count_debuff_distance_dotDps_dps_dps2_duration_duration2_duration3_effectCD_effectCharge_frict_height_item2_life_limit_lock_max_maxNumberOfMarks_min_mob_offsetX_offsetY_power_power2_power3_prct_prct2_prct3_range_size_speed_speed2_tick_triggerOnHit_uses_width_>();
                itemProps.count = head.Value;
            }

            List<string> priceAt1 = UnlockedByDefault();
            foreach (string itemName in priceAt1)
            {
                cdb.item.byId.get(itemName.AsHaxeString()).cellCost = 1;
            }

            var item = ((HaxeDynObj) cdb.item.byId.get("DeathMoney".AsHaxeString())).ToVirtual<virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_>();
            virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_ newItem = new virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_
            {
                group = item.group,
                id = "APGold".AsHaxeString(),
                tags = item.tags,
                synergy = item.synergy,
                props = item.props,
                name = "Archipelago Money Bag".AsHaxeString(),
                moneyCost = item.moneyCost,
                legendAffixes = item.legendAffixes,
                icon = item.icon,
                gameplayDesc = "No cost too great.".AsHaxeString(),
                droppable = item.droppable,
                commonProps = item.commonProps,
                cellCost = item.cellCost,
                castCD = item.castCD,
            };
            cdb.item.byId.set("APGold".AsHaxeString(), newItem);
            cdb.item.all.push(newItem);

            item = ((HaxeDynObj) cdb.item.byId.get("DeathCells".AsHaxeString())).ToVirtual<virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_>();
            newItem = new virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_
            {
                group = item.group,
                id = "APCells".AsHaxeString(),
                tags = item.tags,
                synergy = item.synergy,
                props = item.props,
                name = "Archipelago Cells Bag".AsHaxeString(),
                moneyCost = item.moneyCost,
                legendAffixes = item.legendAffixes,
                icon = item.icon,
                gameplayDesc = "It's dangerous to go alone! Take this.".AsHaxeString(),
                droppable = item.droppable,
                commonProps = item.commonProps,
                cellCost = item.cellCost,
                castCD = item.castCD,
            };
            cdb.item.byId.set("APCells".AsHaxeString(), newItem);
            cdb.item.all.push(newItem);

            
            Log.Information("=== Archipelago Mod loaded ! ===");
        }
    }
}