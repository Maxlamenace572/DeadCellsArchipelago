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
            if(IsQueueEmpty()) { return; }
            if(SAVED_DATA == null) { return; }

            var itemName = pendingItems[0];

            if (NameToIdKeyExist(itemName))
            {
                itemName = GetId(itemName);
            }

            if(!SAVED_DATA.IsItemRecieved(itemName))
            {
                useOriginalRevealItem = true;
                if (GiveItemFromArchipelago(itemName))
                {
                    SAVED_DATA.SaveItemRecieved(itemName);
                }
                useOriginalRevealItem = false;
            }
            else
            {
                Log.Error($"=== Item {itemName} already given ===");
            }
            pendingItems.RemoveAt(0);
        }

        public static bool IsQueueEmpty()
        {
            return pendingItems.Count == 0;
        }
    }
}