
using dc;
using dc.en;
using dc.en.inter;
using dc.hl.types;
using dc.pr;
using dc.tool;
using dc.ui.hud;
using ModCore.Utilities;
using Serilog;
using static dc.tool.InventItemKind;

namespace DeadCellsArchipelago {
    public static class ItemManager
    {
        public static Hero? HERO { get; set; }
        public static ArchipelagoSaveData? SAVED_DATA { get; set; }
        public static ArchipelagoManager? ARCHIPELAGO { get; set; }
        public static ItemMetaManager? ITEM_META_MANAGER { get; set; }
        public static User? USER { get; set; }
        public static bool useOriginalUnlockItem { get; set; } = false;
        public static bool heroJustDead = false;
        public static int aspectsToIter = 0;

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
                            new HaxeProxy.Runtime.Ref<bool>(ref inArmoryValue)
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

        private static InventItem? CreateInventItemById(string itemName)
        {
            var group = -1;

            foreach (var item in Data.Class.item.all)
            {
                if(item.id.ToString() == itemName)
                {
                    group = item.group;
                    break;
                }
            }
            if (group == -1)
            {
                Log.Error($"=== Item with id : {itemName} doesn't exist ===");
                return null;
            }

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
            //todo: lock base weapon, not just stop revealing them (but maybe not here, this function is checked each run/load)
        }

        //the boolean returned here is for saving or not the item in local data
        public static bool GiveItemFromArchipelago(string itemName)
        {
            if (ITEM_META_MANAGER != null) {
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
                    case "BossRune1":
                    case "BossRune2":
                    case "BossRune3":
                    case "BossRune4":
                    case "BossRune5":
                        ITEM_META_MANAGER.addPermanentItem(itemName.AsHaxeString());
                        LogItem(itemName);
                        return true;

                }//todo: other kinds
                if (itemName.Length >= 5 && itemName[..5] == "Trap_")
                {
                    switch (itemName)
                    {
                        case "Trap_Curse":
                            if(HERO != null)
                            {
                                bool hidePopup = false;
                                bool useAltSound = false;
                                HERO.curse(50, "Archipelago trap".AsHaxeString(), new HaxeProxy.Runtime.Ref<bool>(ref hidePopup), new HaxeProxy.Runtime.Ref<bool>(ref useAltSound));
                            }
                            break;
                    }
                    Log.Warning("=== if nothing append, I forgot to implement it ===");
                    return false;
                }
                else if(itemName.Length >= 3 && itemName[..3] == "ASP")
                {
                    if (IsUnlockedByDefault(itemName))
                    {
                        var progress = new ItemProgress(itemName.AsHaxeString());
                        ITEM_META_MANAGER.itemProgress.push(progress);
                    }
                    UnlockItem(itemName);
                    ITEM_META_MANAGER.getItemProgress(itemName.AsHaxeString()).unlocked = true;
                    if (IsUnlockedByDefault(itemName) && SAVED_DATA != null)
                    {
                        SAVED_DATA.AddBaseItemUnlocked(itemName);
                    }
                } else
                {
                    BlueprintManager.UnlockBlueprint(itemName);
                }
                LogItem(itemName);
                return true;
            }
            return false;
        }

        public static void LogItem(string itemId)
        {
            if(USER != null)
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
            //Log.Warning($"=== This method was called for {k} in on unlock ===");//to be removed when all unlocked item with this are found
            if(!useOriginalUnlockItem)
            {
                SendItemWithoutBlueprintCheck(k.ToString());
                return false;
            }
            return orig(self, k);
        }

        public static void SendItemWithoutBlueprintCheck(string itemId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck("Item_" + itemId, itemId, "Item:");//todo
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
    }
}