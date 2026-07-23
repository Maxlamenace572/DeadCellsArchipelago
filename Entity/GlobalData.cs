namespace DeadCellsArchipelago {
    public class GlobalData
    {
        public int bscLevelToWin = 4;
        public bool includeCosmetics = false;
        public bool riseOfTheGiant = false;
        public bool theBadSeed = false;
        public bool fatalFalls = false;
        public bool theQueenAndTheSea = false;
        public bool returnToCastlevania = false;

        public void InitValues(int bsc, bool cosmetics, bool rotg, bool tbs, bool ff, bool tqats, bool rtc)
        {
            bscLevelToWin = bsc;
            includeCosmetics = cosmetics;
            riseOfTheGiant = rotg;
            theBadSeed = tbs;
            fatalFalls = ff;
            theQueenAndTheSea = tqats;
            returnToCastlevania = rtc;
        }
    }
}