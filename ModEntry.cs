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
using static DeadCellsArchipelago.LinkQueue;
using static DeadCellsArchipelago.ModAssetManager;
using dc.level;
using dc.tool;
using ModCore.Events.Interfaces.Game.Save;
using Newtonsoft.Json;
using dc;
using dc.hl.types;
using dc.cine;
using HaxeProxy.Runtime;
using Hashlink.Virtuals;
using ModCore.Events.Interfaces.Game.Hero;
using ModCore.Events.Interfaces.Game;

namespace DeadCellsArchipelago{
    public class ModEntry(ModInfo info) : ModBase(info), 
        IOnAfterLoadingSave,
        IOnBeforeSavingSave,
        IOnHeroUpdate,
        IOnAfterLoadingCDB
    {
        private ArchipelagoManager archipelago = new();

        public override void Initialize()
        {
            Log.Information("[AP] Archipelago Mod is loading...");

            Save.Class.NUM_SLOTS = 99;
            IdToApName = LoadModApTranslation();
            ApNameToId = Invert(IdToApName);
            
            InitializeBossHooks();
            InitializeItemHooks();
            InitializeHeroHooks();
            InitializeBlueprintHooks();
            InitializeRuneHooks();
            InitializeRoomHooks();
            InitializeNpcHooks();
            InitializeAchievementHooks();
            InitializeEnemyHooks();
            InitializeMainMenuHooks();
            InitializeImageHooks();
            InitializePokeHooks();
            InitializeUnlockItemHooks();
            InitializePauseHooks();
            
            Hook_LevelGen.generate += OnLevelGenGenerate;

            Log.Information("[AP] Archipelago hooks loaded");
            //SaveChoice
            //BrBlueprint
            //BossRushData
            //for biome rando: LevelTransition.Class.@goto("Lighthouse".AsHaxeString());
        }

        public void OnHeroUpdate(double dt)
        {
            if (HERO != null && HERO.awake)
            {    
                GiveItemInQueue();
                ShowLogInQueue();
                CheckDeathLink();
                DoEveryLinks();
                if (logError) ShowLogError();

                if (shouldGiveItemsNewRun && SAVED_DATA != null)
                {
                    shouldGiveItemsNewRun = false;
                    if (SAVED_DATA.IsItemReceived("ShipwreckKey"))
                    {
                        GiveItemToPlayer("ShipwreckKey");
                        HERO.hudInitItems();
                    }

                    if (ARCHIPELAGO != null && ARCHIPELAGO.respawnUpScroll)
                    {
                        foreach (string itemName in GetUpScrolls())
                        {
                            SAVED_DATA.GivenFillerItem[itemName] = 0;
                        }
                    }
                    LoadLinks();
                }

                if (newConnection)
                {
                    LoadLinks();
                    newConnection = false;
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

                Log.Information($"[AP] Loading save slot {data.userId}");
                
                // Load Archipelago data for this game
                var savePath = GetSaveFilePath(data.userId);
                if (System.IO.File.Exists(savePath))
                {
                    try
                    {
                        var json = System.IO.File.ReadAllText(savePath);
                        SAVED_DATA = JsonConvert.DeserializeObject<ArchipelagoSaveData>(json) ?? new();
                        
                        Log.Information($"[AP] loaded with {SAVED_DATA.SentChecks.Count} checks send");

                        if (ARCHIPELAGO != null && loadDataInPlayMenu == 1)
                        {
                            ARCHIPELAGO.SyncAll();
                            loadDataInPlayMenu = 0;
                        }
                    }
                    catch (Exception ex)
                    {
                        Log.Error($"[AP] Error loading save : {ex.Message}");
                    }
                }
            }
            else
            {
                Log.Information($"[AP] New Save");
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
            Log.Information($"[AP] Saving slot {data.Data.userId}");
            
            var savePath = GetSaveFilePath(data.Data.userId);
            try
            {
                var json = JsonConvert.SerializeObject(SAVED_DATA, Formatting.Indented);
                System.IO.File.WriteAllText(savePath, json);
                
                Log.Information($"[AP] Save ended with {SAVED_DATA?.SentChecks.Count} checks");
            }
            catch (Exception ex)
            {
                Log.Error($"[AP] Error saving : {ex.Message}");
            }
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
                cellCost = item.cellCost
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
                cellCost = item.cellCost
            };
            cdb.item.byId.set("APCells".AsHaxeString(), newItem);
            cdb.item.all.push(newItem);

            if(!cosmeticsList.Any())
            {
                InitLists();
            }
            foreach (string skinId in cosmeticsList)
            {
                cdb.item.byId.get(skinId.AsHaxeString()).cellCost = 50;
            }
            
            Log.Information("[AP] CDB Changed");
        }
    }
}