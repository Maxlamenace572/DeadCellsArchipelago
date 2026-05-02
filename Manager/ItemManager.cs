
using System.Text.RegularExpressions;
using dc;
using dc.cine;
using dc.en;
using dc.en.inter;
using dc.hl.types;
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

namespace DeadCellsArchipelago {
    public static class ItemManager
    {
        public static Hero? HERO { get; set; }
        public static ArchipelagoSaveData? SAVED_DATA { get; set; }
        public static ArchipelagoManager? ARCHIPELAGO { get; set; }
        public static ItemMetaManager? ITEM_META_MANAGER { get; set; }
        public static User? USER { get; set; }
        public static bool useOriginalUnlockItem { get; set; } = false;
        public static bool useOriginalRevealItem { get; set; } = false;
        public static bool removeCollectorBaseFilterAndLock { get; set; } = false;
        public static string currentFilterFor { get; set; } = "";
        public static bool heroJustDead = false;
        public static int aspectsToIter = 0;
        public static List<string> dropableList = [];
        public static List<string> cosmeticsList = [];
        public static int bossRuneGivenSinceLaunch = 0;
        public static Dictionary<string, int> ProgressionItemGivenSinceLaunch { get; set; } = [];
        public static Dictionary<string, int> fillerItemGivenSinceLaunch { get; set; } = [];

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
            }
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

                        if (itemName == "DeathMoney")
                        {
                            itemDrop.item._itemData.name = "Archipelago Money Bag".AsHaxeString();
                            itemDrop.item._itemData.gameplayDesc = "No cost too great.".AsHaxeString();
                            
                        }
                        else if (itemName == "DeathCells")
                        {
                            itemDrop.item._itemData.name = "Archipelago Cells Bag".AsHaxeString();
                            itemDrop.item._itemData.gameplayDesc = "It's dangerous to go alone! Take this.".AsHaxeString();
                        }
                        
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

        //the boolean returned here is for saving or not the item in local data
        public static bool GiveItemFromArchipelago(string itemName)
        {
            if (ITEM_META_MANAGER != null) {
                if(IsItemProgressive(itemName))
                {
                    string? unlockedName = HandleProgressive(itemName);
                    if (unlockedName != null)
                    {
                        BlueprintManager.UnlockBlueprint(unlockedName);
                        LogItem(unlockedName);
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
                        ITEM_META_MANAGER.addPermanentItem(itemName.AsHaxeString());
                        GiveItemToPlayer(itemName);
                        RuneManager.ActivateMinimapTracking(itemName);
                        LogItem(itemName);
                        return true;
                    case "BossRune":
                        string? unlockedName = HandleBossRune();
                        if(unlockedName != null)
                        {
                            ITEM_META_MANAGER.addPermanentItem(unlockedName.AsHaxeString());
                            LogItem(unlockedName);
                        }
                        return false;

                }//todo: other kinds
                if (itemName.Length >= 5 && itemName[..5] == "Trap_")
                {
                    if(ShouldDropItem(itemName))
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
                                    LevelTransition.Class.gotoSub.Invoke(levelMapChallenge, null);
                                }
                                break;
                            default:
                                Log.Warning("=== Not implemented yet ===");
                                break;
                        }
                    }
                    return false;
                }

                if(InDropableList(itemName))
                {
                    if(ShouldDropItem(itemName))
                    {
                        DropItemToPlayer(itemName);
                    }
                    return false;
                }

                if(IsLevelKey(itemName))
                {
                    LogItem("GenericKey");
                    return true;
                }

                if(itemName.Length >= 3 && itemName[..3] == "ASP")
                {
                    var progress = new ItemProgress(itemName.AsHaxeString());
                    ITEM_META_MANAGER.itemProgress.push(progress);
                    UnlockItem(itemName);
                    ITEM_META_MANAGER.getItemProgress(itemName.AsHaxeString()).unlocked = true;
                    if (IsUnlockedByDefault(itemName) && SAVED_DATA != null)
                    {
                        SAVED_DATA.AddBaseItemUnlocked(itemName);
                    }
                }
                else
                {
                    BlueprintManager.UnlockBlueprint(itemName);
                }
                
                try {
                    LogItem(itemName);
                }
                catch (Exception ex)
                {
                    Log.Error($"=== Item doesn't exist {ex} ===");
                    return false;
                }
                
                return true;
            }
            return false;
        }

        private static bool ShouldDropItem(string itemName)
        {
            if(SAVED_DATA != null)
            {
                if(!fillerItemGivenSinceLaunch.ContainsKey(itemName))
                {
                    fillerItemGivenSinceLaunch[itemName] = 0;
                }
                if(fillerItemGivenSinceLaunch[itemName] >= SAVED_DATA.HowManyFillerItemRecieved(itemName))
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
                if(ProgressionItemGivenSinceLaunch[itemName] >= SAVED_DATA.HowManyProgressionItemRecieved(itemName))
                {
                    string? newProgName = NewInCategory(itemName);
                    if (newProgName != null)
                    {
                        SAVED_DATA.SaveItemRecieved(newProgName);
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
                SAVED_DATA.SaveItemRecieved(newRuneName);
                return newRuneName;
            }
            return null;
        }

        private static string? NewRuneBossName()
        {
            if (SAVED_DATA != null)
            {
                if (bossRuneGivenSinceLaunch < SAVED_DATA.NumberOfBossRuneRecieved())
                {
                    bossRuneGivenSinceLaunch++;
                    return null;
                }
                else if (SAVED_DATA.NumberOfBossRuneRecieved() < 5)
                {
                    string? res = null;
                    if (SAVED_DATA.IsItemRecieved("BossRune4"))
                    {
                        res = "BossRune5";
                    }
                    else if (SAVED_DATA.IsItemRecieved("BossRune3"))
                    {
                        res = "BossRune4";
                    }
                    else if (SAVED_DATA.IsItemRecieved("BossRune2"))
                    {
                        res = "BossRune3";
                    }
                    else if (SAVED_DATA.IsItemRecieved("BossRune1"))
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

        public static void LogItem(string itemId)
        {
            if(USER != null && USER.game != null)
            {
                BlueprintManager.showBlueprintLog = true;
                USER.game.log.blueprint(itemId.AsHaxeString(), "Always".AsHaxeString(), false, false);
                BlueprintManager.showBlueprintLog = false;
            }
        }

        public static void UnlockItem(string itemId)
        {
            if(ITEM_META_MANAGER != null)
            {
                useOriginalUnlockItem = true;
                ITEM_META_MANAGER.unlockItem(itemId.AsHaxeString());
                useOriginalUnlockItem = false;
            }
        }

        public static bool OnUnlockItem(Hook_ItemMetaManager.orig_unlockItem orig, ItemMetaManager self, dc.String k)//utilisé pour les items comme la poelle 
        {
            //Log.Warning($"||| This method was called for {k} in on unlock |||");//to be removed when all unlocked item with this are found
            if(!useOriginalUnlockItem && ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics))
            {
                SendItemWithoutBlueprintCheck(k.ToString());
                return false;
            }
            return orig(self, k);
        }

        public static bool OnRevealItem(Hook_ItemMetaManager.orig_revealItem orig, ItemMetaManager self, dc.String k, bool showAsNew)
        {
            if(!useOriginalRevealItem && ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics))
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
                Log.Error("=== Error while sending Item check ===");
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
                if (heroJustDead && aspectsToIter <= 12)//the game use hasUnlockedItem to add aspects in its random give pool
                {
                    aspectsToIter++;
                    return SAVED_DATA.IsCheckSent(k.ToString());
                }

                if(removeCollectorBaseFilterAndLock && currentFilterFor != "")
                {
                    if(new[] {"Money1", "Recycling1", "MirrorUnlock", "ForgeRefine1"}.Any(currentFilterFor.Contains))
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

        public static bool IsUnlockedByDefault(string id)
        {
            switch (id)
            {
                case "DualDaggers":
                case "StunMace":
                case "DualBow":
                case "ThrowingKnife":
                case "LightningWhip":
                case "ThrowingTorch":
                case "Freeze":
                case "Shield":
                case "GreedShield":
                case "StandardTurret":
                case "RootTrap":
                case "FastGrenade":
                case "IceBomb":
                case "ExtraHeal":
                case "QuickSword":
                case "P_CDR_Kill":
                case "P_DmgKill":
                case "P_DmgRevenge":
                case "P_DeployedDmg":
                case "P_NoMobAround":
                case "P_CDR_Distance":
                case "P_CDR_Parry":
                case "P_DmgParry":
                case "P_HealOnKill":
                case "P_Yolo":
                case "P_CDR_Crit":
                case "ASP_Firestarter":
                case "ASP_ToxinLover":
                case "ASP_Shatter":
                case "PrisonerGOG":
                case "PrisonerFrench":
                case "PrisonerRetro":
                case "Snowman":
                case "SantaKLOS":
                case "BlackHoleViolet":
                case "VortexHelloDarkness":
                case "BlowTorch":
                    return true;
            }
            return false;
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
                        if (SAVED_DATA.IsItemRecieved("Flask4"))
                        {
                            res = null;
                        }
                        else if (SAVED_DATA.IsItemRecieved("Flask3"))
                        {
                            res = "Flask4";
                        }
                        else if (SAVED_DATA.IsItemRecieved("Flask2"))
                        {
                            res = "Flask3";
                        }
                        else if (SAVED_DATA.IsItemRecieved("Flask1"))
                        {
                            res = "Flask2";
                        }
                        else
                        {
                            res = "Flask1";
                        }
                        break;
                    case 'M':
                        if (SAVED_DATA.IsItemRecieved("Money5"))
                        {
                            res = null;
                        }
                        else if (SAVED_DATA.IsItemRecieved("Money4"))
                        {
                            res = "Money5";
                        }
                        else if (SAVED_DATA.IsItemRecieved("Money3"))
                        {
                            res = "Money4";
                        }
                        else if (SAVED_DATA.IsItemRecieved("Money2"))
                        {
                            res = "Money3";
                        }
                        else if (SAVED_DATA.IsItemRecieved("Money1"))
                        {
                            res = "Money2";
                        }
                        else
                        {
                            res = "Money1";
                        }
                        break;
                    case 'R':
                        if (SAVED_DATA.IsItemRecieved("Recycling2"))
                        {
                            res = null;
                        }
                        else if (SAVED_DATA.IsItemRecieved("Recycling1"))
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
    }
}