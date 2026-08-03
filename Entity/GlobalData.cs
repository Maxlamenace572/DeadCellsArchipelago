using static DeadCellsArchipelago.ModAssetManager;
using static DeadCellsArchipelago.ItemManager;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace DeadCellsArchipelago {
    public class GlobalData
    {
        public int bscLevelToWin = 4;
        public bool includeCosmetics = false;
        public bool respawnUpScroll = false;
        public bool riseOfTheGiant = false;
        public bool theBadSeed = false;
        public bool fatalFalls = false;
        public bool theQueenAndTheSea = false;
        public bool returnToCastlevania = false;
        public Dictionary<string, int> ProgressionItem { get; set; } = [];
        public Dictionary<string, int> BossHeadKilled { get; set; } = [];
        public Dictionary<int, int> ProgressionForge { get; set; } = [];
        public int currentCells = 0;

        public void InitValues(int bsc, bool cosmetics, bool rus, bool rotg, bool tbs, bool ff, bool tqats, bool rtc)
        {
            bscLevelToWin = bsc;
            includeCosmetics = cosmetics;
            respawnUpScroll = rus;
            riseOfTheGiant = rotg;
            theBadSeed = tbs;
            fatalFalls = ff;
            theQueenAndTheSea = tqats;
            returnToCastlevania = rtc;
        }

        public void SaveGlobalSaveJson()
        {
            if (SAVED_DATA == null) return;
            var savePath = GetGlobalSaveFilePath(SAVED_DATA.archipelagoSeed);
            var saveJson = JsonConvert.SerializeObject(GLOBAL_DATA, Formatting.Indented);
            File.WriteAllText(savePath, saveJson);
        }
    }
}