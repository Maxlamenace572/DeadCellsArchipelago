using dc;
using dc.pr;
using dc.ui;
using Hashlink.Virtuals;
using Serilog;
using static DeadCellsArchipelago.TrackerData;
using static DeadCellsArchipelago.ItemManager;
using ModCore.Utilities;
using Hashlink.Proxy;
using HaxeProxy.Runtime;

namespace DeadCellsArchipelago {
    public static class WorldMapManager
    {
        public static Dictionary<string, Biome> biomes = [];

        public static void InitializeWorldMapHooks()
        {
            Log.Information("[AP] Loading World Map Hooks...");

            Hook_WorldMap.drawLevelCards += OnDrawLevelCards;
            Hook_WorldMap.isLevelVisible += OnIsLevelVisible;

            Log.Information("[AP] World Map Hooks loaded");
        }

        private static virtual_height_width_ OnDrawLevelCards(Hook_WorldMap.orig_drawLevelCards orig, WorldMap self)
        {
            biomes = CalculateRegionData();
            return orig(self);
        }

        private static bool OnIsLevelVisible(Hook_WorldMap.orig_isLevelVisible orig, WorldMap self, dc.String id)
        {
            return (biomes.ContainsKey(id.ToString()) && biomes[id.ToString()].accessible) || orig(self, id);
        }

        public static bool IsLevelAfterCurrent(string biome)
        {
            var level = Data.Class.level.byId.get(biome.AsHaxeString());
            var levelProxy = ((HashlinkObj)level).AsHaxe();
            virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_ levelVirtual = levelProxy.ToVirtual<virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_>();
            return SAVED_DATA!.lastLevelDepthSeen < levelVirtual.mapDepth;
        }

        public static int GetLevelDepth(string biome)
        {
            var level = Data.Class.level.byId.get(biome.AsHaxeString());
            var levelProxy = ((HashlinkObj)level).AsHaxe();
            virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_ levelVirtual = levelProxy.ToVirtual<virtual_baseLootLevel_biome_bonusTripleScrollAfterBC_cellBonus_dlc_doubleUps_eliteRoomChance_eliteWanderChance_flagsProps_group_icon_id_index_loreDescriptions_mapDepth_minGold_mobDensity_mobs_name_nextLevels_parallax_props_quarterUpsBC3_quarterUpsBC4_specificLoots_specificSubBiome_transitionTo_tripleUps_worldDepth_>();
            return levelVirtual.mapDepth;
        }
    }
}