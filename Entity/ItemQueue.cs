using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.Translator;

namespace DeadCellsArchipelago
{
    public static class ItemQueue
    {
        private static List<string> pendingItems = [];

        public static void AddItemToQueue(string itemName)
        {
            Log.Information($"=== Item reçu d'Archipelago: {itemName} ===");
            pendingItems.Add(itemName);
        }

        public static void GiveItemInQueue()
        {
            if(IsQueueEmpty() || SAVED_DATA == null) return;

            string itemName = pendingItems[0];

            string itemId = itemName;
            if (NameToIdKeyExist(itemId))
            {
                itemId = GetId(itemId);
            }

            if(!SAVED_DATA.IsItemReceived(itemId))
            {
                useOriginalRevealItem = true;
                if (GiveItemFromArchipelago(itemId, itemName))
                {
                    SAVED_DATA.SaveItemReceived(itemId);
                }
                useOriginalRevealItem = false;
            }
            pendingItems.RemoveAt(0);
        }

        public static bool IsQueueEmpty()
        {
            return pendingItems.Count == 0;
        }
    }
}