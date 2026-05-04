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
using dc.hl;
using dc.ui;
using ModCore.Utilities;

using static DeadCellsArchipelago.Translator;
using static DeadCellsArchipelago.PokeManager;
using static DeadCellsArchipelago.HeroManager;
using dc.level.lore;
using dc.tool.mod.script;
using System.Reflection;
using Hashlink.Proxy;
using HaxeProxy.Runtime.Internals;

namespace DeadCellsArchipelago {
    public static class RoomManager
    {
        public static LevelMap? levelMapNotChallenge = null;
        public static LevelMap? levelMapChallenge = null;

        public static void InitializeRoomHooks()
        {
            Hook_PrisonCourtyard.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_PrisonRoof.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_Crypt.finalize += (orig, self) => { useOriginalHasPermanentItem=false;orig(self); useOriginalHasPermanentItem=true; };
            Hook_SewerShort.buildSecondaryRooms += (orig, self) => { useOriginalHasPermanentItem=false; orig(self); useOriginalHasPermanentItem=true; };
            Hook_AncientTemple.buildSecondaryRooms += (orig, self) => { useOriginalHasPermanentItem=false; orig(self); useOriginalHasPermanentItem=true; };
            Hook_Ossuary.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_Ossuary.buildSecondaryRooms += (orig, self) => { useOriginalHasPermanentItem=false; orig(self); useOriginalHasPermanentItem=true; };
            dc.level.@struct.Hook_Throne.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res; };
            Hook_QueenArena.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
            Hook_DookuArena.buildMainRooms += (orig, self) => { useOriginalHasPermanentItem=false; var res=orig(self); useOriginalHasPermanentItem=true; return res;};
        }

        public static void OnTriggeredDoorActivate(Hook_TriggeredDoor.orig_onActivate orig, TriggeredDoor self, Hero by, bool lp)
        {
            if(USER != null && USER.game.curLevel.map.getRoomAt(self.cx, self.cy) != null)
            {   //allow the player to open the mutation door in collector's transition
                Log.Warning($"=== porte en {USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate} ===");
                if (USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "PerkShop" || USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "DookuArenaPerkShop")
                {
                    self.openFast(self.cx - by.cx >= 0 ? 1 : -1, null);
                    return;
                }
                if (USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "OssBoss")
                {
                    self.openFast(self.cx - by.cx >= 0 ? 1 : -1, null);
                    return;
                }
            }
            orig(self, by, lp);
        }

        public static void OnDoorCloseFast(Hook_Door.orig_closeFast orig, Door self, HlAction cb)
        {   //without this, the mutation door in collector's transition will close automatically
            if(USER != null && USER.game.curLevel != null)
            {
                if (USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "PerkShop" || USER.game.curLevel.map.getRoomAt(self.cx, self.cy).rTemplate.ToString() == "DookuArenaPerkShop")
                {
                    return;
                }
            }
            orig(self, cb);
        }

        //when the level is generating, we do the checks biomes and add a void challenge for the trap
        public static ArrayObj OnGenerate(Hook_LevelGen.orig_generate orig, LevelGen self, User user, int seed, virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_ ldat, Ref<bool> resetCount)
        {
            if(ldat.id.ToString() == "PrisonStart")
            {
                if(SAVED_DATA != null && SAVED_DATA.currentLevelId != "PrisonStart" && !resetOnNextPrisonStart)
                {
                    PrepareBiomeCheck(SAVED_DATA.currentLevelId, " Exit", ldat.id.ToString());
                }
                if (resetOnNextPrisonStart)
                {
                    ResetDataNewRun();
                    resetOnNextPrisonStart = false;
                }
                PrepareBiomeCheck(ldat.id.ToString(), " Enter", ldat.id.ToString());
            }
            if(new[] {"Ossuary", "QueenArena", "Bank", "DeathArena"}.Any(ldat.id.ToString().Contains))
            {
                ResetFrontPokebomb();
                PrepareBiomeCheck(ldat.id.ToString(), " Enter", ldat.id.ToString());
                if(SAVED_DATA != null) SAVED_DATA.numberOfPokebombUse ++;
            }

            var level = Data.Class.level.byId.get("Challenge".AsHaxeString());
            var levelProxy = ((HashlinkObj)level).AsHaxe();
            virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_ levelVirtual = levelProxy.ToVirtual<virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_>();
            
            ArrayObj levelMaps = orig(self, user, seed, levelVirtual, resetCount);
            foreach (var item in levelMaps) {
                levelMapChallenge = item;
                break;
            }
            
            return orig(self, user, seed, ldat, resetCount).concat(levelMaps);
        }

        public static void SendBiomeCheck(string locationId)
        {
            if (ARCHIPELAGO != null)
            {
                ARCHIPELAGO.SendCheck(locationId, locationId, "Biome:");
            }
            else
            {
                Log.Error("=== Error while sending Rune check ===");
            }
        }

        public static void OnActiviteExit(Hook_Exit.orig_onActivate orig, Exit self, Hero by, bool lp)
        {
            ResetFrontPokebomb();
            if(SAVED_DATA != null && USER != null && !IsMultipleExitsTransition(self.destLevel.ToString()) && !CanTakeExit(self.getDestBasedOnNextLevels().ToString()))
            {
                string msg = $"You need the key for {self.getDestName()} !";
                bool sound = true;
                USER.game.modalPause(new Ref<bool>(ref sound));
                new Confirmation(null, msg.AsHaxeString(), () => CloseModal(), () => CloseModal(), "Close".AsHaxeString(), "".AsHaxeString(), null);
            }
            else
            {
                if (self.destLevel.ToString()[..2] == "T_")
                {
                    bool noStats = false;
                    by.addCells(10, new Ref<bool>(ref noStats));
                    if(SAVED_DATA != null) PrepareBiomeCheck(SAVED_DATA.currentLevelId, " Exit", self.destLevel.ToString());
                }
                else
                {
                    PrepareBiomeCheck(self.destLevel.ToString(), " Enter", self.destLevel.ToString());
                    if(SAVED_DATA != null) SAVED_DATA.numberOfPokebombUse ++;
                }
                orig(self, by, lp);
            }
        }

        public static void OnActivatePortal(Hook_Portal.orig_onActivate orig, Portal self, Hero by, bool lp)
        {
            if (SAVED_DATA != null)
            {
                if (self.isExit)
                {
                    if(SAVED_DATA.isDoingChallenge) PrepareBiomeCheck("Challenge", " Exit", SAVED_DATA.currentLevelId);
                    if(trapChallenge)
                    {
                        self.popText($"It's a trap, I can't escape through there.".AsHaxeString(), 16777215);
                        return;
                    }
                }
                else
                {
                    PrepareBiomeCheck("Challenge", " Enter", SAVED_DATA.currentLevelId);
                }
            }
            orig(self, by, lp);
        }

        public static void OnActivateTreasureChest(Hook_TreasureChest.orig_onActivate orig, TreasureChest self, Hero by, bool lp)
        {
            if(trapChallenge)
            {
                self.popText($"It's a trap, I can't open this chest.".AsHaxeString(), 16777215);
                return;
            }
            orig(self, by, lp);
        }

        public static void OnClosePortal(Hook_Portal.orig_close orig, Portal self)
        {
            if(SAVED_DATA != null)
            {
                SAVED_DATA.isDoingChallenge = !SAVED_DATA.isDoingChallenge;
            }
            orig(self);
        }

        private static void PrepareBiomeCheck(string locationName, string kind, string destinationId)
        {
            if(SAVED_DATA != null)
            {
                if (IdToNameKeyExist(locationName))
                {
                    locationName = GetName(locationName);
                }

                if(!SAVED_DATA.IsCheckSent(locationName + kind))
                {
                    SendBiomeCheck(locationName + kind);
                }
                SAVED_DATA.currentLevelId = destinationId;
            }
        }

        public static void CloseModal()
        {
            USER?.game.resume();
        }

        public static bool CanTakeExit(string biomeId)
        {
            if(SAVED_DATA != null)
            {
                return !ExistKey(biomeId) || SAVED_DATA.IsItemRecieved(biomeId);
            }
            return false;
        }

        public static bool IsMultipleExitsTransition(string levelId)
        {
            switch (levelId)
            {
                case "T_AfterDeathArena":
                case "T_AfterTumulus":
                case "T_Castle":
                case "T_AfterSwamp":
                case "T_AfterBridge":
                case "T_Bank":
                    return true;
            }
            return false;
        }

        public static bool ExistKey(string biomeId)
        {
            return IdToNameKeyExist(biomeId) && !Free(biomeId);
        }

        public static bool Free(string biomeId)
        {
            switch (biomeId)
            {
                case "PrisonStart":
                case "PrisonCourtyard":
                case "SewerShort":
                case "PrisonRoof":
                case "Bridge":
                case "DookuCastleHard":
                    return true;
            }
            return false;
        }
    }
}