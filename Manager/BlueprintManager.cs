using dc;
using dc.en;
using dc.hl.types;
using dc.level;
using dc.tool;
using dc.ui;
using Hashlink.Marshaling;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class BlueprintManager
    {
        public static bool showBlueprintLog = false;
        public static bool useOriginalHasRevealItem = false;

        //Called when the hero get a blueprint, picked in game or by UnlockBlueprint.
        public static bool OnBlueprintPicked(Hook_Hero.orig_pickBlueprint orig, Hero self, dc.String k)
        {
            //the blueprint is comming from the game, so we need to send a archipelago check
            if(ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics))
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
            if(ARCHIPELAGO != null && (!InCosmeticList(k.ToString()) || ARCHIPELAGO.includeCosmetics) && !useOriginalHasRevealItem)
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
                Log.Error("=== Error while sending blueprint check ===");
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
    }
}