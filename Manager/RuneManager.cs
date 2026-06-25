using dc;
using dc.en;
using dc.en.inter;
using dc.h2d;
using dc.hl.types;
using dc.libs.heaps.slib;
using dc.tool;
using dc.ui;
using Hashlink.Virtuals;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class RuneManager
    {
        public static bool useOriginalHasPermanentItem { get; set;} = true;

        public static void OnApplyItemPickEffect(Hook_Hero.orig_applyItemPickEffect orig, Hero self, Entity from, InventItem i)
        {   //called each time the player take any item not blueprint
            //Log.Warning($"=== pick effect on {i._itemData.id} {i._itemData.name} ===");
            bool noStats = false;
            Random rnd = new Random();
            switch (i._itemData.id.ToString())
            {
                case "LadderKey":
                case "TeleportKey":
                case "ScoringKey":
                case "CustomKey":
                case "BreakableGroundKey":
                case "WallJumpKey":
                case "HomKey":
                case "ExploKey":
                    SendRuneCheck(i._itemData.id.ToString());
                    break;
                case "BossRune1":
                case "BossRune2":
                case "BossRune3":
                case "BossRune4":
                case "BossRune5":
                    SendBscCheck(i._itemData.id.ToString());
                    break;
                case "ShipwreckKey":
                    SendItemWithoutBlueprintCheck(i._itemData.id.ToString());
                    break;
                case "APGold":
                    int goldNumber = rnd.Next(8192, 131073);
                    self.addMoney(goldNumber, new Ref<bool>(ref noStats));
                    self.popText($"+{goldNumber}{{iconCoin@img}}".AsHaxeString(), dc.ui.Text.Class.COLORS.get("GO".AsHaxeString()));
                    break;
                case "APCells":
                    int cellsNumber = rnd.Next(8, 129);
                    self.addCells(cellsNumber, new Ref<bool>(ref noStats));
                    cellsNumber *= 4;

                    int frame = 0;
                    double XY = 0;
                    Tile cellTile = Assets.Class.gameElements.getTile("cell".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null); //@1233

                    var pop = self.popText($"+{cellsNumber}".AsHaxeString(), dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));

                    var addX = 0;
                    if (cellsNumber > 99)
                    {
                        addX = 5;
                    }
                    new Bitmap(cellTile, pop.text)
                    {
                        x = 30 + addX,
                        y = 10
                    };
                    break;
                default:
                    orig(self, from, i);
                    break;
            }
        }

        public static void ActivateMinimapTracking(string itemName)
        {
            if (USER != null)
            {
                if (itemName == "LadderKey")
                {
                    ArrayObj? array = USER.game.curLevel?.entitiesByClass?.get(35400); //35400 is the internal id for VineLadder
                    if(array != null)
                    {
                        for (int i = 0; i < array.length; i++)
                        {
                            VineLadder vineLadder = (VineLadder) array.getDyn(i);
                            vineLadder.minimapTracking();
                        }
                    }
                }
                else if (itemName == "TeleportKey")
                {
                    ArrayObj? array = USER.game.curLevel?.entitiesByClass?.get(23651); //23651 is the internal id for RedTeleporter
                    if(array != null)
                    {
                        for (int i = 0; i < array.length; i++)
                        {
                            RedTeleporter redTeleporter = (RedTeleporter) array.getDyn(i);
                            redTeleporter.minimapTracking();
                        }
                    }
                }
                else if (itemName == "BreakableGroundKey")
                {
                    ArrayObj? array = USER.game.curLevel?.entitiesByClass?.get(32866); //32866 is the internal id for BreakableGround
                    if(array != null)
                    {
                        for (int i = 0; i < array.length; i++)
                        {
                            BreakableGround breakableGround = (BreakableGround) array.getDyn(i);
                            breakableGround.minimapTracking();
                        }
                    }
                }
            }
        }

        public static void SendRuneCheck(string runeId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck(runeId, runeId, "Rune:");
            }
            else
            {
                SAVED_DATA?.SaveOfflineCheck(runeId, runeId);
            }
        }

        public static bool ReallyHasPermanentItem(Hook_ItemMetaManager.orig_hasPermanentItem orig, ItemMetaManager self, dc.String k)
        {
            /*if(k.ToString() != "WallJumpKey" && k.ToString() != "BackpackUnlock" && k.ToString() != "ExploKey")
            {
                Log.Error($"=== rune {k} {useOriginalHasPermanentItem} {SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString())}===");
            }*/
            if (useOriginalHasPermanentItem) //this flag should change to false only when generating rooms, to have rune arena
            {
                return orig(self, k);
            }
            return SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString()); //If we already have the rune check, don't generate the arena
        }

        public static void SendBscCheck(string bscId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck(bscId, bscId, "BSC:");
            }
            else
            {
                SAVED_DATA?.SaveOfflineCheck(bscId, bscId);
            }
        }

        public static void OnNextScene(Hook_Throne.orig_nextScene orig, Throne self, Hero by)
        { //for HomKey
            useOriginalHasPermanentItem = false;
            orig(self, by);
            useOriginalHasPermanentItem = true;
        }

        public static bool OnAddPermanentItem(Hook_ItemMetaManager.orig_addPermanentItem orig, ItemMetaManager self, dc.String k)
        { //for HomKey
            if(useOriginalHasPermanentItem)
            {
                return orig(self, k);
            }
            SendRuneCheck(k.ToString());
            return false;
        }

        public static void OnRewardPopup(Hook__RewardPopup.orig___constructor__ orig, RewardPopup arg1, virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_ item, HlAction onValidate, Ref<bool> isMetaItem)
        {
            if (item.id.ToString() == "BossRushUnlock")
            {
                SendRuneCheck("BossRushUnlock");
            } else
            {
                orig(arg1, item, onValidate, isMetaItem);
            }
        }
    }
}