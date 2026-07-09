using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.HeroManager;

namespace DeadCellsArchipelago
{
    public static class LinkQueue
    {
        private static List<List<int>> pendingHealthLink = [];
        private static List<int> pendingHealthCurseLink = [];
        public static bool healthLinkDeath = false;
        private static List<TrapData> pendingTrapCurseLink = [];

        public static void AddHealthLinkToQueue(List<int> healthLinkValues)
        {
            pendingHealthLink.Add(healthLinkValues);
        }

        public static void AddHealthCurseLinkToQueue(int curseValue)
        {
            pendingHealthCurseLink.Add(curseValue);
        }

        public static void AddTrapLinkToQueue(string itemName, bool canSendTrapLinkFromCall)
        {
            pendingTrapCurseLink.Add(new TrapData(itemName, canSendTrapLinkFromCall));
        }

        public static void DoHealthLinkInQueue()
        {
            if(IsHealthLinkQueueEmpty() || HERO == null) return;

            List<int> healthLinkValues = pendingHealthLink[0];
            UpdateHeroHealthLink(healthLinkValues[0], healthLinkValues[1]);
            pendingHealthLink.RemoveAt(0);
        }

        public static void DoHealthCurseLinkInQueue()
        {
            if(IsHealthCurseLinkQueueEmpty() || HERO == null) return;

            int curseValue = pendingHealthCurseLink[0];
            UpdateHeroHealthCurseLink(curseValue);
            pendingHealthCurseLink.RemoveAt(0);
        }

        public static void DoDeathHealthLink()
        {
            if(HERO == null) return;

            if (healthLinkDeath)
            {
                HERO.kill();
                healthLinkDeath = false;
            }
        }
        
        public static void DoTrapLinkInQueue()
        {
            if(IsTrapLinkQueueEmpty()) return;

            TrapData trap = pendingTrapCurseLink[0];
            GiveTrapItem(trap.itemName, trap.canSendTrapLinkFromCall);
            pendingTrapCurseLink.RemoveAt(0);
        }

        public static bool IsHealthLinkQueueEmpty()
        {
            return pendingHealthLink.Count == 0;
        }

        public static bool IsHealthCurseLinkQueueEmpty()
        {
            return pendingHealthCurseLink.Count == 0;
        }

        public static bool IsTrapLinkQueueEmpty()
        {
            return pendingTrapCurseLink.Count == 0;
        }

        public static void DoEveryLinks()
        {
            DoDeathHealthLink();
            DoHealthLinkInQueue();
            DoHealthCurseLinkInQueue();
            DoTrapLinkInQueue();
        }

        public static void LoadLinks()
        {
            if (HERO == null) return;
            if (ARCHIPELAGO != null && ARCHIPELAGO.healthLinkManager != null)
            {
                List<int> healthValues = ARCHIPELAGO.healthLinkManager.GetHealthStorage();
                UpdateHeroHealthLink(healthValues[0], healthValues[1]);

                if (ARCHIPELAGO.healthLinkManager.shareCurses) 
                {
                    int curses = ARCHIPELAGO.healthLinkManager.GetHealthCurseStorage();
                    UpdateHeroHealthCurseLink(curses);
                }
            }
        }
    }
}