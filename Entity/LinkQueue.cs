using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.HeroManager;

namespace DeadCellsArchipelago
{
    public static class LinkQueue
    {
        private static List<List<int>> pendingHealthLink = [];

        public static void AddHealthLinkToQueue(List<int> healthLinkValues)
        {
            Log.Information($"=== Health Link received from Archipelago: {healthLinkValues[0]} {healthLinkValues[1]} ===");
            pendingHealthLink.Add(healthLinkValues);
        }


        public static void DoHealthLinkInQueue()
        {
            if(IsHealthLinkQueueEmpty() || HERO == null) return;

            List<int> healthLinkValues = pendingHealthLink[0];

            UpdateHeroHealthLink(healthLinkValues[0], healthLinkValues[1]);

            pendingHealthLink.RemoveAt(0);
        }

        public static bool IsHealthLinkQueueEmpty()
        {
            return pendingHealthLink.Count == 0;
        }
    }
}