using dc;
using dc.en;
using dc.hl.types;
using dc.level;
using dc.tool;
using dc.ui;
using dc.ui.icon;
using Hashlink.Marshaling;
using Hashlink.Virtuals;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ModAssetManager;
using dc.h2d;
using HaxeProxy.Runtime;

namespace DeadCellsArchipelago {
    public static class BlueprintManager
    {
        public static bool showBlueprintLog = false;
        public static bool useOriginalHasRevealItem = false;
        public static bool changeLogDesc = false;
        public static string logDesc = "";
        public static bool changeLogIcon = false;

        //Called when the hero get a blueprint, picked in game or by UnlockBlueprint.
        public static bool OnBlueprintPicked(Hook_Hero.orig_pickBlueprint orig, Hero self, dc.String k)
        {
            //the blueprint is comming from the game, so we need to send a archipelago check
            if(!InCosmeticList(k.ToString()) || (ARCHIPELAGO != null && ARCHIPELAGO.includeCosmetics))
            {
                SendBlueprintCheck(k.ToString());
                return true;
            }
            return orig(self, k);
        }

        //Instantly unlock the blueprint
        public static void UnlockBlueprint(string blueprintId)
        {
            //Log.Information($" {HERO == null}  {ITEM_META_MANAGER == null} ===");
            if (HERO != null && USER != null)
            {
                try
                {
                    useOriginalHasRevealItem = true;
                    USER.itemMeta.revealItem(blueprintId.AsHaxeString(), true);
                    useOriginalHasRevealItem = false;
                    Log.Information($"=== Blueprint unlocked:  {blueprintId} ===");

                }
                catch (Exception ex)
                {
                    Log.Error($"=== Error while giving blueprint: {ex.Message} ===");
                }
            }
        }

        //hasRevealedItem allow or not the blueprint to spawn
        public static bool ReallyHasBlueprint(Hook_ItemMetaManager.orig_hasRevealedItem orig, ItemMetaManager self, dc.String k)
        {
            if((!InCosmeticList(k.ToString()) || (ARCHIPELAGO != null && ARCHIPELAGO.includeCosmetics)) && !useOriginalHasRevealItem)
            {
                return SAVED_DATA != null && SAVED_DATA.IsCheckSent(k.ToString()); //Drop the blueprint only when he is not in the saved checklist
            }
            return orig(self, k);
        }

        public static void SendBlueprintCheck(string blueprintId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck(blueprintId, blueprintId, "Blueprint:");
            }
            else
            {
                SAVED_DATA?.SaveOfflineCheck(blueprintId, blueprintId);
            }
        }

        public static void BlueprintUILog(Hook_LogManager.orig_blueprint orig, LogManager self, dc.String k, dc.String baseRarity, bool isRevealed, bool isScoring)
        {
            if (showBlueprintLog)
            {
                orig(self, k, baseRarity, isRevealed, false);
            }
            if (ARCHIPELAGO != null && !ARCHIPELAGO.includeCosmetics && InCosmeticList(k.ToString()))
            {
                orig(self, k, baseRarity, isRevealed, false);
            }
        }

        public static void HeadUILog(Hook_LogManager.orig_head orig, LogManager self, dc.String headKind)
        {
            if (ARCHIPELAGO != null && !ARCHIPELAGO.includeCosmetics)
            {
                orig(self, headKind);
            }
        }

        public static void FixNotSpawningBlueprint(Hook_LootGen.orig_addBlueprintAt orig, LootGen self, LevelMap map, int cx, int cy, dc.String k, bool freeItemAsAlt, bool noAlt)
        {
            //I don't know why but without this hook, blueprints like the two in half life lore room won't spawn without DualBow
            orig(self, map, cx, cy, k, freeItemAsAlt, noAlt);
        }

        public static ArrayObj OnGetDailyRewards(Hook_User.orig_getDailyRewards orig, User self)
        {
            ArrayObj res = new ArrayObj()
            {
                array = new(HashlinkMarshal.Module.KnownTypes.String, 0),
                length = 0
            };
            if (SAVED_DATA == null) return res;

            if (!SAVED_DATA.IsCheckSent("SpeedBlade")) res.push("SpeedBlade".AsHaxeString());
            else if (!SAVED_DATA.IsCheckSent("DamageAura")) res.push("DamageAura".AsHaxeString());
            else if (!SAVED_DATA.IsCheckSent("DashSword")) res.push("DashSword".AsHaxeString());
            return res;
        }
        
        public static dc.String OnGetBlueprintLocalizedName(Hook__ItemTools.orig_getBlueprintLocalizedName orig, virtual_ambiantDesc_castCD_cellCost_commonProps_dlc_droppable_gameplayDesc_group_icon_id_legendAffixes_moneyCost_name_props_synergy_tags_tier1_tier2_ item)
        {
            //Change log description
            if (changeLogDesc)
            {
                changeLogDesc = false;
                return logDesc.AsHaxeString();
            }
            return orig(item);
        }

        public static Icon OnCreateItemIcon(Hook__Icon.orig_createItemIcon orig, dc.String itemKind, dc.h2d.Object parent)
        {
            if (changeLogIcon)
            {
                changeLogIcon = false;
                Tile logoTile = archipelagoLogoTile.clone();
                Icon res = new Icon(logoTile, parent);
                res.scaleToSize(40, 40);
                double center = 0.5;
                res.setCenterRatio(new Ref<double>(ref center), new Ref<double>(ref center));
                return res;
            }
            return orig(itemKind, parent);
        }
    }
}