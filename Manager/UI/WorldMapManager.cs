using dc.ui;
using Hashlink.Virtuals;
using Serilog;
using static DeadCellsArchipelago.TrackerData;

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
    }
}