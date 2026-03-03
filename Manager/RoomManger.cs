using dc.level.@struct;
using static DeadCellsArchipelago.RuneManager;

using static DeadCellsArchipelago.ItemManager;
using dc.en.inter.door;
using dc.en;
using dc.en.inter;
using HaxeProxy.Runtime;
using Serilog;
using dc.hl.types;
using dc.level;
using dc;
using Hashlink.Virtuals;

namespace DeadCellsArchipelago {
    public static class RoomManager
    {
        private static string? lastLevel { get; set; }
        public static void InitializeRoomHooks()
        {
            Hook_PrisonCourtyard.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_PrisonRoof.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_Crypt.finalize += (orig, self) => { useOriginalHasPermanentItem=false;orig(self); useOriginalHasPermanentItem=true; };
            Hook_SewerShort.buildSecondaryRooms += (orig, self) => { useOriginalHasPermanentItem=false; orig(self); useOriginalHasPermanentItem=true; };
            Hook_AncientTemple.buildSecondaryRooms += (orig, self) => { useOriginalHasPermanentItem=false; orig(self); useOriginalHasPermanentItem=true; };
            Hook_Ossuary.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_Ossuary.buildSecondaryRooms += (orig, self) => { useOriginalHasPermanentItem=false; orig(self); useOriginalHasPermanentItem=true; };
        }

        public static void OnTriggeredDoorActivate(Hook_TriggeredDoor.orig_onActivate orig, TriggeredDoor self, Hero by, bool lp)
        {
            if(USER != null)
            {   //allow the player to open the mutation door in collector's transition
                if (USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "PerkShop")
                {
                    self.openFast(self.cx - by.cx >= 0 ? 1 : -1, null);
                    return;
                }
            }
            orig(self, by, lp);
        }

        public static void OnDoorCloseFast(Hook_Door.orig_closeFast orig, Door self, HlAction cb)
        {   //without this, the mutation door in collector's transition will close automatically
            if(USER != null)
            {
                if (USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "PerkShop")
                {
                    return;
                }
            }
            orig(self, cb);
        }

        //when the level is generating, we do the checks biomes
        public static ArrayObj OnGenerate(Hook_LevelGen.orig_generate orig, LevelGen self, User user, int seed, virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_ ldat, Ref<bool> resetCount)
        {
            Log.Warning($"=== start last level {lastLevel} ===");
            if(lastLevel != null && SAVED_DATA != null && SAVED_DATA.IsCheckSent($"Ending_{ldat.id}"))
            {
                   SendBiomeCheck(ldat.id.ToString(), "Ending");
                   Log.Warning("=== send end ===");
            }

            if(ldat.id.ToString().Substring(0, 2) != "T_")
            {
                if(SAVED_DATA != null && SAVED_DATA.IsCheckSent($"Ending_{ldat.id}"))
                {
                    SendBiomeCheck(ldat.id.ToString(), "Starting");
                    Log.Warning("=== send start ===");
                }
                lastLevel = ldat.id.ToString();
                Log.Warning($"=== last level {lastLevel} ===");
            }
            return orig(self, user, seed, ldat, resetCount);
        }

        public static void OnHeroDie(Hook_Hero.orig_onDie orig, Hero self)
        {
            lastLevel = null;
            Log.Warning("=== It's a death ==="); //test for reset and complete run (I want to do it on reset but not on complete), and what happend when he quit
            orig(self);
        }

        public static void SendBiomeCheck(string biomeId, string biomeStatus)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck($"{biomeStatus}_{biomeId}", "Biome:");
            }
            else
            {
                Log.Error("=== Error while sending Rune check ===");
            }
        }
    }
}