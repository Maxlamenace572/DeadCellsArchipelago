
using dc;
using dc.h2d;
using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public static class ModAssetManager
    {
        public static Tile archipelagoLogoTile = LoadTileFromPng(GetResPath("logo.png"));
        public static Tile VoidBackground1080Tile = LoadTileFromPng(GetResPath("VoidHD.png"));

        public static string GetSaveFilePath(int slot)
        {
            string saveDir = Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data");
            
            Directory.CreateDirectory(saveDir);
            return Path.Combine(saveDir, $"APSlot_{Main.Class.ME.options.curSlot}.json");
            //return System.IO.Path.Combine(saveDir, $"archipelagoUserId_{slot}.json");
        }
    }
}