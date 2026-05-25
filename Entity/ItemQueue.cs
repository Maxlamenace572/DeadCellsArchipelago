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

            if (itemName.Length >= 9 && itemName[^9..] == " Defeated")
            {
                pendingItems.RemoveAt(0);
                return;
            }

            string itemId = itemName;
            if (itemId.Length >= 7 && itemId[^7..] == " Unlock")
            {
                itemId = itemId[..^7];
            }

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

        public static void ClearQueue()
        {
            pendingItems = [];
        }
    }
}