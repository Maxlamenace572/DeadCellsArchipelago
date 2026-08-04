
using dc;
using dc.h2d;
using dc.tool;
using dc.ui;
using Newtonsoft.Json;
using Serilog;
using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.ItemManager;

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
            Hook_HUD.postUpdate += OnPostUpdateHUD;

            Log.Information("[AP] Mod Asset Hooks loaded");
        }

        public static string GetSaveFilePath(int slot)
        {
            string saveDir = System.IO.Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data");
            
            Directory.CreateDirectory(saveDir);
            return System.IO.Path.Combine(saveDir, $"APSlot_{slot}.json");
        }

        public static string GetGlobalSaveFilePath(string seed)
        {
            string saveDir = System.IO.Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "data");
            
            Directory.CreateDirectory(saveDir);
            return System.IO.Path.Combine(saveDir, $"APSeed_{seed}.json");
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

        public static void LoadGlobalData()
        {
            if (SAVED_DATA == null) return;
            var savePath = GetGlobalSaveFilePath(SAVED_DATA.archipelagoSeed);
            if (System.IO.File.Exists(savePath))
            {
                var json = System.IO.File.ReadAllText(savePath);
                GLOBAL_DATA = JsonConvert.DeserializeObject<GlobalData>(json) ?? new();
            }
            else
            {
                if (ARCHIPELAGO == null) return;
                GLOBAL_DATA = new GlobalData();
                GLOBAL_DATA.InitValues(
                    ARCHIPELAGO.bscOption,
                    ARCHIPELAGO.includeCosmetics,
                    ARCHIPELAGO.respawnUpScroll,
                    ARCHIPELAGO.riseOfTheGiant,
                    ARCHIPELAGO.theBadSeed,
                    ARCHIPELAGO.fatalFalls,
                    ARCHIPELAGO.theQueenAndTheSea,
                    ARCHIPELAGO.returnToCastlevania,
                    ARCHIPELAGO.flawlessScroll);

                var json = JsonConvert.SerializeObject(GLOBAL_DATA, Formatting.Indented);
                System.IO.File.WriteAllText(savePath, json);
            }
        }

        private static void OnPostUpdateHUD(Hook_HUD.orig_postUpdate orig, HUD self)
        {
            orig(self);
            self.bmpMod.set_visible(false);
        }
    }
}