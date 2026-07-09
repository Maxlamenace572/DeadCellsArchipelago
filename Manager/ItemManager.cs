
using System.Text.RegularExpressions;
using dc;
using dc.cine;
using dc.en;
using dc.en.inter;
using dc.hl.types;
using dc.hxd;
using dc.level;
using dc.pr;
using dc.tool;
using dc.ui;
using dc.ui.hud;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;
using static dc.tool.InventItemKind;

using static DeadCellsArchipelago.EnemyManager;
using static DeadCellsArchipelago.HeroManager;
using static DeadCellsArchipelago.RoomManager;
using static DeadCellsArchipelago.BlueprintManager;
using static DeadCellsArchipelago.PokeManager;
using static DeadCellsArchipelago.TrapLinkManager;

namespace DeadCellsArchipelago {
    public static class ItemManager
    {
        public static Hero? HERO { get; set; }
        public static ArchipelagoSaveData? SAVED_DATA { get; set; } = null;
        public static ArchipelagoManager? ARCHIPELAGO { get; set; }
        public static User? USER { get; set; }
        public static bool useOriginalUnlockItem { get; set; } = false;
        public static bool useOriginalRevealItem { get; set; } = false;
        public static bool removeCollectorBaseFilterAndLock { get; set; } = false;
        public static string currentFilterFor { get; set; } = "";
        public static bool heroJustDead = false;
        public static int aspectsToIter = 0;
        public static List<string> dropableList = [];
        public static List<string> cosmeticsList = [];
        public static List<string> headList = [];
        public static int bossRuneGivenSinceLaunch = 0;
        public static Dictionary<string, int> ProgressionItemGivenSinceLaunch { get; set; } = [];
        public static Dictionary<string, int> fillerItemGivenSinceLaunch { get; set; } = [];
        public static List<string> History = [];
        public static bool disableTrapOnEndBoss = false;
        public static bool useModdedHasUnlock = false;

        public static void InitLists()
        {
            foreach (var item in Data.Class.item.all)
            {
                int group = -1;
                var match = Regex.Match(item.ToString(), @"group\s*:\s*(\d+)");
                if (match.Success)
                {
                    group = int.Parse(match.Groups[1].Value);
                }
                if(group == 10 || group == 11)
                {
                    dropableList.Add(item.id.ToString());
                }
                if(group == 13 || group == 14)
                {
                    cosmeticsList.Add(item.id.ToString());
                }
                if(group == 14)
                {
                    headList.Add(item.id.ToString());
                }
            }
            dropableList.Add("APGold");
            dropableList.Add("APCells");
            cosmeticsList.Remove("Cultist");
        }

        //Drop the item with the id @itemName to the player position
        //Warning: all items can be dropped, but if it has no pick up implementation, it will crash the game when you take it.
        //Same for using Weapon or Actives without the said uses implemented.
        public static void DropItemToPlayer(string itemName)
        {
            if (HERO != null) {
                try
                {
                    InventItem? inventItem = CreateInventItemById(itemName);

                    if (inventItem != null) {
                        Log.Information($"=== Item {itemName} Created ===");
                        bool inArmoryValue = false;
                        ItemDrop itemDrop = new ItemDrop(
                            HERO._level,
                            HERO.cx,
                            HERO.cy,
                            inventItem,
                            true,
                            new Ref<bool>(ref inArmoryValue)
                        );

                        itemDrop.init();
                        itemDrop.onDropAsLoot();
                        itemDrop.dx = HERO.dx;
                        
                        Log.Information("=== Item Successfully Dropped ! ===");
                    } else
                    {
                        Log.Error($"=== Item {itemName} could not be created ===");
                    }
                }
                catch (Exception ex)
                {
                    Log.Error($"=== Error: {ex.Message} ===");
                    Log.Error($"Stack trace: {ex.StackTrace}");
                }
            }
            else
            {
                Log.Error("=== Cannot log inventory, hero is null ===");
            }
        }

        public static void GiveItemToPlayer(string itemName)
        {
            if (HERO != null) {
                try
                {
                    InventItem? inventItem = CreateInventItemById(itemName);

                    if (inventItem != null) {
                        Log.Information($"=== Item {itemName} Created ===");
                        HERO.inventory.add(inventItem);
                    } else
                    {
                        Log.Error($"=== Item {itemName} could not be created ===");
                    }
                }
                catch (Exception ex)
                {
                    Log.Error($"=== Error: {ex.Message} ===");
                    Log.Error($"Stack trace: {ex.StackTrace}");
                }
            }
            else
            {
                Log.Error("=== Cannot log inventory, hero is null ===");
            }
        }

        public static int? GetGroupItem(string itemName)
        {
            var group = -1;
            foreach (var item in Data.Class.item.all)
            {
                if(item.id.ToString() == itemName)
                {
                    var match = Regex.Match(item.ToString(), @"id\s*:\s*(\w+)");
                    if (match.Success && match.Groups[1].Value == itemName)
                    {
                        var matchGroup = Regex.Match(item.ToString(), @"group\s*:\s*(\d+)");
                        if (matchGroup.Success)
                        {
                            group = int.Parse(matchGroup.Groups[1].Value);
                            break;
                        }
                    }
                }
            }
            if (group == -1)
            {
                Log.Error($"=== Item with id : {itemName} doesn't exist ===");
                return null;
            }
            return group;
        }

        private static InventItem? CreateInventItemById(string itemName)
        {
            var group = GetGroupItem(itemName);

            if(group == null) {return null;}

            InventItem? inventItem = null;

            switch (group)
            {
                case 0:
                case 1:
                case 2:
                case 3:
                    inventItem = new InventItem(new InventItemKind.Active(itemName.AsHaxeString()));
                    break;

                case 4:
                case 5:
                case 6:
                    inventItem = new InventItem(new InventItemKind.Weapon(itemName.AsHaxeString()));
                    break;

                case 7:
                    inventItem = new InventItem(new Talisman(itemName.AsHaxeString()));
                    break;

                case 8:
                    inventItem = new InventItem(new BagItem(itemName.AsHaxeString()));
                    break;

                case 9:
                    inventItem = new InventItem(new Meta(itemName.AsHaxeString()));
                    break;

                case 10:
                    inventItem = new InventItem(new Consumable(itemName.AsHaxeString()));
                    break;

                case 11:
                    inventItem = new InventItem(new PreciousLoot(itemName.AsHaxeString()));
                    break;

                case 12:
                    inventItem = new InventItem(new Perk(itemName.AsHaxeString()));
                    break;

                case 13:
                    inventItem = new InventItem(new Skin(itemName.AsHaxeString()));
                    break;

                case 14:
                    inventItem = new InventItem(new Head(itemName.AsHaxeString()));
                    break;

                case 15:
                    inventItem = new InventItem(new Aspect(itemName.AsHaxeString()));
                    break;

                case 16:
                    inventItem = new InventItem(new BossRushStatueUnlock(itemName.AsHaxeString()));
                    break;
            }

            return inventItem;
        }

        public static void LogInventory()
        {
            if(HERO != null) {
                Log.Information("=== Read all inventory ===");
                if (HERO.inventory.items.length > 0)
                {
                    var hasNext = true;
                    var i = 0;
                    var item = HERO.inventory.items.getDyn(i);
                    while (hasNext)
                    {
                        Log.Information($"{i} : {item?.kind}");
                        i++;
                        item = HERO.inventory.items.getDyn(i);
                        if(item == null)
                        {
                            hasNext = false;
                        }
                    }
                }
                Log.Information("=== Inventory end ===");
            }
            else
            {
                Log.Error("=== Cannot log inventory, hero is null ===");
            }
        }

        public static void ReallyRevealAllBaseItems(Hook_ItemMetaManager.orig_revealAllBaseItems orig, ItemMetaManager self)
        {
            //leaving this blank remove base items in collector's shop (upgrade, weapons and skills)
        }

        //the boolean returned here is for saving or not the item in local data in item received
        public static bool GiveItemFromArchipelago(string itemName, string LogName)
        {
            if (SAVED_DATA == null) Log.Error($"--- saved data at null");
            if (USER == null) {Log.Error($"--- USER at null"); return false;}
            if (USER.itemMeta == null) Log.Error($"--- item meta at null");

            if (USER.itemMeta != null) {
                if(IsItemProgressive(itemName))
                {
                    string? unlockedName = HandleProgressive(itemName);
                    if (unlockedName != null)
                    {
                        UnlockBlueprint(unlockedName);
                        LogItem(unlockedName);
                        AddToHistory(LogName);
                    }
                    return false;
                }

                switch (itemName)
                {
                    case "LadderKey":
                    case "TeleportKey":
                    case "ScoringKey":
                    case "CustomKey":
                    case "BreakableGroundKey":
                    case "WallJumpKey":
                    case "HomKey":
                    case "ExploKey":
                        USER.itemMeta.addPermanentItem(itemName.AsHaxeString());
                        GiveItemToPlayer(itemName);
                        RuneManager.ActivateMinimapTracking(itemName);
                        LogItem(itemName);
                        AddToHistory(LogName);
                        return true;
                    case "BossRune":
                        string? unlockedName = HandleBossRune();
                        if(unlockedName != null)
                        {
                            USER.itemMeta.addPermanentItem(unlockedName.AsHaxeString());
                            LogItem(unlockedName);
                            AddToHistory(LogName);
                        }
                        return false;
                    case "ShipwreckKey":
                        GiveItemToPlayer(itemName);
                        HERO?.hudInitItems();
                        LogItem(itemName);
                        AddToHistory(LogName);
                        return true;
                    case "BossRushUnlock":
                        LogItem(itemName);
                        USER?.story.counters.set("BRUnlockPopUp".AsHaxeString(), 1);
                        return true;
                }
                if (itemName.Length >= 5 && itemName[..5] == "Trap_")
                {
                    if(ShouldDropItem(itemName))
                    {
                        GiveTrapItem(itemName, true);
                        AddToHistory(LogName);
                    }
                    return false;
                }

                if(InDropableList(itemName))
                {
                    if(ShouldDropItem(itemName))
                    {
                        LogItem(itemName);
                        AddToHistory(LogName);
                    }
                    return false;
                }

                if(IsLevelKey(itemName))
                {
                    changeLogDesc = true;
                    logDesc = LogName;
                    LogItem("GenericKey");
                    AddToHistory(LogName);
                    return true;
                }

                if(itemName.Length >= 3 && itemName[..3] == "ASP" || InHeadList(itemName))
                {
                    var progress = new ItemProgress(itemName.AsHaxeString());
                    USER.itemMeta.itemProgress.push(progress);
                    UnlockItem(itemName);
                    USER.itemMeta.getItemProgress(itemName.AsHaxeString()).unlocked = true;
                    if (IsUnlockedByDefault(itemName) && SAVED_DATA != null)
                    {
                        SAVED_DATA.AddBaseItemUnlocked(itemName);
                    }
                }
                else
                {
                    UnlockBlueprint(itemName);
                }
                
                try {
                    LogItem(itemName);
                    AddToHistory(LogName);
                }
                catch (Exception ex)
                {
                    Log.Error($"=== Item {itemName} doesn't exist {ex} ===");
                    return false;
                }
                
                return true;
            }
            return false;
        }

        public static void GiveTrapItem(string itemName, bool canSendTrapLinkFromCall)
        {
            if (!disableTrapOnEndBoss)
            {
                switch (itemName)
                {
                    case "Trap_Curse":
                        if(HERO != null)
                        {
                            bool hidePopup = false;
                            bool useAltSound = false;
                            HERO.curse(50, "Archipelago Curse Trap".AsHaxeString(), new Ref<bool>(ref hidePopup), new Ref<bool>(ref useAltSound));
                        }
                        break;
                    case "Trap_SpawnElite":
                        EliteTrap();
                        break;
                    case "Trap_RemoveGold":
                        if(USER != null && HERO != null)
                        {
                            bool noStats = false;
                            HERO.substractMoney(USER.game.data.money, new Ref<bool>(ref noStats));
                        }
                        break;
                    case "Trap_BreakWeapon":
                        RemoveARandomWeapon();
                        break;
                    case "Trap_InvertControls":
                        InitSwitchControls();
                        break;
                    case "Trap_FlawlessChallenge":
                        if (levelMapChallenge != null && USER != null && HERO != null)
                        {
                            trapChallenge = true;
                            levelMapNotChallenge = USER.game.curLevel.map;
                            try
                            {
                                LevelTransition.Class.gotoSub.Invoke(levelMapChallenge, null);
                            }
                            catch (Exception ex)
                            {
                                Log.Error($"Trap_FlawlessChallenge error : {ex}");
                            }
                        }
                        break;
                    default:
                        Log.Warning("=== Not implemented yet ===");
                        break;
                }
            }
            if (canSendTrapLinkFromCall && ARCHIPELAGO != null && ARCHIPELAGO.trapLinkManager != null) ARCHIPELAGO.trapLinkManager.SendTrapLink(itemName);
        }

        public static void OnPickItem(Hook_Hero.orig_pickItem orig, Hero self, Entity from, InventItem i, HlAction<bool> onComplete)
        {
            if (i._itemData.id.ToString() == "Pokebomb" && IsAnySkillPokebomb())
            {
                SAVED_DATA?.numberOfPokebombUse += 5;
                from.destroy();
            }
                
            else orig(self, from, i, onComplete);
        }

        private static bool ShouldDropItem(string itemName)
        {
            if(SAVED_DATA != null)
            {
                if(!fillerItemGivenSinceLaunch.ContainsKey(itemName))
                {
                    fillerItemGivenSinceLaunch[itemName] = 0;
                }
                if(fillerItemGivenSinceLaunch[itemName] >= SAVED_DATA.HowManyFillerItemReceived(itemName))
                {
                    SAVED_DATA.AddFillerItem(itemName);
                    AddFillerItemGivenSinceLaunch(itemName);
                    return true;
                }
                AddFillerItemGivenSinceLaunch(itemName);
            }
            return false;
        }

        private static void AddFillerItemGivenSinceLaunch(string itemName)
        {
            if(fillerItemGivenSinceLaunch.ContainsKey(itemName))
            {
                fillerItemGivenSinceLaunch[itemName]++;
            }
            else
            {
                fillerItemGivenSinceLaunch[itemName] = 1;
            }
        }

        private static string? HandleProgressive(string itemName)
        {
            if(SAVED_DATA != null)
            {
                if(!ProgressionItemGivenSinceLaunch.ContainsKey(itemName))
                {
                    ProgressionItemGivenSinceLaunch[itemName] = 0;
                }
                if(ProgressionItemGivenSinceLaunch[itemName] >= SAVED_DATA.HowManyProgressionItemReceived(itemName))
                {
                    string? newProgName = NewInCategory(itemName);
                    if (newProgName != null)
                    {
                        SAVED_DATA.SaveItemReceived(newProgName);
                        SAVED_DATA.AddProgressionItem(itemName);
                        AddProgressionItemGivenSinceLaunch(itemName);
                    }
                    return newProgName;
                }
                AddProgressionItemGivenSinceLaunch(itemName);
            }
            return null;
        }

        private static void AddProgressionItemGivenSinceLaunch(string itemName)
        {
            if(ProgressionItemGivenSinceLaunch.ContainsKey(itemName))
            {
                ProgressionItemGivenSinceLaunch[itemName]++;
            }
            else
            {
                ProgressionItemGivenSinceLaunch[itemName] = 1;
            }
        }

        private static string? HandleBossRune()
        {
            var newRuneName = NewRuneBossName();
            if(SAVED_DATA != null && newRuneName != null)
            {
                SAVED_DATA.SaveItemReceived(newRuneName);
                return newRuneName;
            }
            return null;
        }

        private static string? NewRuneBossName()
        {
            if (SAVED_DATA != null)
            {
                if (bossRuneGivenSinceLaunch < SAVED_DATA.NumberOfBossRuneReceived())
                {
                    bossRuneGivenSinceLaunch++;
                    return null;
                }
                else if (SAVED_DATA.NumberOfBossRuneReceived() < 5)
                {
                    string? res = null;
                    if (SAVED_DATA.IsItemReceived("BossRune4"))
                    {
                        res = "BossRune5";
                    }
                    else if (SAVED_DATA.IsItemReceived("BossRune3"))
                    {
                        res = "BossRune4";
                    }
                    else if (SAVED_DATA.IsItemReceived("BossRune2"))
                    {
                        res = "BossRune3";
                    }
                    else if (SAVED_DATA.IsItemReceived("BossRune1"))
                    {
                        res = "BossRune2";
                    }
                    else
                    {
                        res = "BossRune1";
                    }
                    bossRuneGivenSinceLaunch++;
                    return res;
                }
            }
            return null;
        }

        public static bool InDropableList(string itemName)
        {
            if(!dropableList.Any())
            {
                InitLists();
            }
            foreach (var item in dropableList)
            {
                if(item == itemName)
                {
                    return true;
                }
            }
            return false;
        }

        public static bool InCosmeticList(string itemName)
        {
            if(!cosmeticsList.Any())
            {
                InitLists();
            }
            foreach (var item in cosmeticsList)
            {
                if(item == itemName)
                {
                    return true;
                }
            }
            return false;
        }

        public static bool InHeadList(string itemName)
        {
            if(!headList.Any())
            {
                InitLists();
            }
            foreach (var item in headList)
            {
                if(item == itemName)
                {
                    return true;
                }
            }
            return false;
        }

        public static void LogItem(string itemId)
        {
            if(USER != null && USER.game != null)
            {
                if(USER.game.log == null) Log.Error($"game's log at null");

                showBlueprintLog = true;
                USER.game.log?.blueprint(itemId.AsHaxeString(), "Always".AsHaxeString(), false, false);
                showBlueprintLog = false;
            }
        }

        public static void UnlockItem(string itemId)
        {
            if(USER != null)
            {
                useOriginalUnlockItem = true;
                USER.itemMeta.unlockItem(itemId.AsHaxeString());
                useOriginalUnlockItem = false;
            }
        }

        public static bool OnUnlockItem(Hook_ItemMetaManager.orig_unlockItem orig, ItemMetaManager self, dc.String k)//utilisé pour les items comme la poelle 
        {
            //Log.Warning($"||| This method was called for {k} in on unlock |||");//to be removed when all unlocked item with this are found
            if(!useOriginalUnlockItem && (!InCosmeticList(k.ToString()) || (ARCHIPELAGO != null && ARCHIPELAGO.includeCosmetics)))
            {
                SendItemWithoutBlueprintCheck(k.ToString());
                return false;
            }
            return orig(self, k);
        }

        public static bool OnRevealItem(Hook_ItemMetaManager.orig_revealItem orig, ItemMetaManager self, dc.String k, bool showAsNew)
        {
            if(!useOriginalRevealItem && (!InCosmeticList(k.ToString()) || (ARCHIPELAGO != null && ARCHIPELAGO.includeCosmetics)))
            {
                SendItemWithoutBlueprintCheck(k.ToString());
                return false;
            }
            return orig(self, k, showAsNew);
        }

        public static bool OnCanInvestOnItem(Hook_ItemMetaManager.orig_canInvestOnItem orig, ItemMetaManager self, dc.String k)
        {
            removeCollectorBaseFilterAndLock = true;
            bool res = orig(self, k);
            removeCollectorBaseFilterAndLock = false;
            return res;
        }

        public static bool OnUserFilter(Hook_CollectorPanel.orig_userFilter orig, CollectorPanel self, ItemProgress data)
        {
            removeCollectorBaseFilterAndLock = true;
            currentFilterFor = data.itemId.ToString();
            bool res = orig(self, data);
            removeCollectorBaseFilterAndLock = false;
            currentFilterFor = "";
            return res;
        }

        public static int OnCountUnlockedItems(Hook_ItemMetaManager.orig_countUnlockedItems orig, ItemMetaManager self)
        {
            if(removeCollectorBaseFilterAndLock)
            {
                return 100;
            }
            return orig(self);
        }

        public static void SendItemWithoutBlueprintCheck(string itemId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck(itemId, itemId, "Item:");
            }
            else
            {
                SAVED_DATA?.SaveOfflineCheck(itemId, itemId);
            }
        }

        public static bool OnInvestOnItemProgress(Hook_ItemMetaManager.orig_investOnItemProgress orig, ItemMetaManager self, dc.String k)
        {
            var isUnlocked = orig(self, k);
            if(isUnlocked && IsUnlockedByDefault(k.ToString()) && SAVED_DATA != null)
            {
                SAVED_DATA.AddBaseItemUnlocked(k.ToString());
            }
            return isUnlocked;
        }

        public static bool OnHasUnlockedItem(Hook_ItemMetaManager.orig_hasUnlockedItem orig, ItemMetaManager self, dc.String k)
        {
            if (SAVED_DATA != null)
            {
                if (heroJustDead && k.ToString().Length >= 3 && k.ToString()[..3] == "ASP" && aspectsToIter <= 12)//the game use hasUnlockedItem to add aspects in its random give pool
                {
                    aspectsToIter++;
                    return SAVED_DATA.IsCheckSent(k.ToString());
                }

                if (useModdedHasUnlock && ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics))
                {
                    return SAVED_DATA.IsCheckSent(k.ToString());
                }

                if(removeCollectorBaseFilterAndLock && currentFilterFor != "")
                {
                    if(new[] {"Money1", "Recycling1", "MirrorUnlock", "ForgeRefine1", "KingWhite"}.Any(currentFilterFor.Contains))
                    {
                        return true;
                    }
                }
                else if(removeCollectorBaseFilterAndLock)
                {
                    return true;
                }

                if (IsUnlockedByDefault(k.ToString()))
                {
                    return SAVED_DATA.IsBaseItemUnlocked(k.ToString());
                }
            }
            return orig(self, k);
        }

        public static void AddToHistory(string logName)
        {
            History.Add(logName);
        }

        public static bool IsUnlockedByDefault(string id)
        {
            return UnlockedByDefault().Contains(id);
        }

        public static List<string> UnlockedByDefault(){
            return [
                "DualDaggers",
                "StunMace",
                "DualBow",
                "ThrowingKnife",
                "LightningWhip",
                "ThrowingTorch",
                "Freeze",
                "Shield",
                "GreedShield",
                "StandardTurret",
                "RootTrap",
                "FastGrenade",
                "IceBomb",
                "ExtraHeal",
                "QuickSword",
                "P_CDR_Kill",
                "P_DmgKill",
                "P_DmgRevenge",
                "P_DeployedDmg",
                "P_NoMobAround",
                "P_CDR_Distance",
                "P_CDR_Parry",
                "P_DmgParry",
                "P_HealOnKill",
                "P_Yolo",
                "P_CDR_Crit",
                "ASP_Firestarter",
                "ASP_ToxinLover",
                "ASP_Shatter",
                "PrisonerGOG",
                "PrisonerFrench",
                "PrisonerRetro",
                "Snowman",
                "SantaKLOS",
                "BlackHoleViolet",
                "VortexHelloDarkness",
                "BlowTorch",
                "BobbyFlame",
                "KingDefault",
                "KingWhite"
            ];
        }

        public static bool IsItemProgressive(string itemName)
        {
            switch (itemName)
            {
                case "Flask":
                case "Money":
                case "Recycling":
                    return true;
            }
            return false;
        }

        private static string? NewInCategory(string itemName)
        {
            string? res = null;
            if(SAVED_DATA != null)
            {
                switch(itemName[0]){
                    case 'F':
                        if (SAVED_DATA.IsItemReceived("Flask4"))
                        {
                            res = null;
                        }
                        else if (SAVED_DATA.IsItemReceived("Flask3"))
                        {
                            res = "Flask4";
                        }
                        else if (SAVED_DATA.IsItemReceived("Flask2"))
                        {
                            res = "Flask3";
                        }
                        else if (SAVED_DATA.IsItemReceived("Flask1"))
                        {
                            res = "Flask2";
                        }
                        else
                        {
                            res = "Flask1";
                        }
                        break;
                    case 'M':
                        if (SAVED_DATA.IsItemReceived("Money5"))
                        {
                            res = null;
                        }
                        else if (SAVED_DATA.IsItemReceived("Money4"))
                        {
                            res = "Money5";
                        }
                        else if (SAVED_DATA.IsItemReceived("Money3"))
                        {
                            res = "Money4";
                        }
                        else if (SAVED_DATA.IsItemReceived("Money2"))
                        {
                            res = "Money3";
                        }
                        else if (SAVED_DATA.IsItemReceived("Money1"))
                        {
                            res = "Money2";
                        }
                        else
                        {
                            res = "Money1";
                        }
                        break;
                    case 'R':
                        if (SAVED_DATA.IsItemReceived("Recycling2"))
                        {
                            res = null;
                        }
                        else if (SAVED_DATA.IsItemReceived("Recycling1"))
                        {
                            res = "Recycling2";
                        }
                        else
                        {
                            res = "Recycling1";
                        }
                        break;
                }
            }
            return res;
        }

        private static bool IsLevelKey(string itemName)
        {
            switch (itemName)
            {
                case "PrisonDepths":
                case "PrisonCorrupt":
                case "Ossuary":
                case "SewerDepths":
                case "BeholderPit":
                case "StiltVillage":
                case "AncientTemple":
                case "Cemetery":
                case "ClockTower":
                case "Crypt":
                case "TopClockTower":
                case "Castle":
                case "Distillery":
                case "Throne":
                case "Cavern":
                case "Giant":
                case "Astrolab":
                case "Observatory":
                case "Greenhouse":
                case "Swamp":
                case "SwampHeart":
                case "Tumulus":
                case "Cliff":
                case "GardenerStage":
                case "Shipwreck":
                case "Lighthouse":
                case "QueenArena":
                case "PurpleGarden":
                case "DookuCastle":
                case "DeathArena":
                case "DookuArena":
                    return true;
            }
            return false;
        }

        public static List<string> GetUpScrolls()
        {
            return ["AnyUp", "BTUp", "BSUp", "TSUp", "AllUp"];
        }

        public static Dictionary<string, int> BossHeadsCount()
        {
            Dictionary<string, int> res = [];
            res.Add("ConciergeFlame", 8);
            res.Add("ConjunctiviusHead", 7);
            res.Add("MamaTickEye", 2);
            res.Add("TimeKeeperHat", 8);
            res.Add("GiantFlame", 4);
            res.Add("ScarecrowHat", 2);
            res.Add("HandOfTheKingFlame", 2);
            res.Add("ServantsMask", 4);
            res.Add("QueenFlame", 2);
            res.Add("CollectorHood", 3);
            return res;
        }

        public static string RandomTrapId()
        {
            List<string> trap = [
                "Trap_Curse",
                "Trap_SpawnElite",
                "Trap_RemoveGold",
                "Trap_BreakWeapon",
                "Trap_InvertControls",
                "Trap_FlawlessChallenge"
            ];
            return trap[new Random().Next(0, trap.Count)];
        }
    }
}