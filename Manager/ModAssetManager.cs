
using dc;
using dc.h2d;
using dc.tool;
using Serilog;
using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public static class ModAssetManager
    {
        public static Tile archipelagoLogoTile = LoadTileFromPng(GetResPath("logo.png"));
        public static Tile VoidBackground1080Tile = LoadTileFromPng(GetResPath("VoidHD.png"));

        public static void InitializeModAssetHooks()
        {
            Log.Information("[AP] Loading Mod Asset Hooks...");

            Hook__Save.copy += OnCopy;
            Hook__Save.delete += OnDelete;

            Log.Information("[AP] Mod Asset Hooks loaded");
        }

        public static string GetSaveFilePath(int slot)
        {
            string saveDir = System.IO.Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data");
            
            Directory.CreateDirectory(saveDir);
            return System.IO.Path.Combine(saveDir, $"APSlot_{slot}.json");
            //return System.IO.Path.Combine(saveDir, $"archipelagoUserId_{slot}.json");
        }

        private static void OnCopy(Hook__Save.orig_copy orig, int slotFrom, int slotTo)
        {
            var savePathFrom = GetSaveFilePath(slotFrom);
            if (System.IO.File.Exists(savePathFrom))
            {
                var json = System.IO.File.ReadAllText(savePathFrom);
                var savePathTo = GetSaveFilePath(slotTo);
                System.IO.File.WriteAllText(savePathTo, json);
            }
            orig(slotFrom, slotTo);
        }

        private static void OnDelete(Hook__Save.orig_delete orig, int? slot)
        {
            var savePath = GetSaveFilePath((int) slot!);
            if (System.IO.File.Exists(savePath)) System.IO.File.Delete(savePath);
            orig(slot);
        }
    }
}