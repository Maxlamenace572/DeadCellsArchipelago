
using dc.h2d;
using static DeadCellsArchipelago.ImageManager;

namespace DeadCellsArchipelago {
    public static class ModAssetManager
    {
        public static Tile archipelagoLogoTile = LoadTileFromPng(GetResPath("logo.png"));
        public static Tile VoidBackground1080Tile = LoadTileFromPng(GetResPath("VoidHD.png"));
    }
}