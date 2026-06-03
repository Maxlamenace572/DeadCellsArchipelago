using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.Translator;
using static DeadCellsArchipelago.BlueprintManager;
using dc;
using ModCore.Utilities;

namespace DeadCellsArchipelago
{
    public static class ItemQueue
    {
        private static List<string> pendingItems = [];
        private static List<string> pendingLogs = [];

        public static void AddItemToQueue(string itemName)
        {
            Log.Information($"=== Item received from Archipelago: {itemName} ===");
            pendingItems.Add(itemName);
        }

        public static void AddLogToQueue(string itemName)
        {
            pendingLogs.Add(itemName);
        }

        public static void GiveItemInQueue()
        {
            if(IsItemQueueEmpty() || SAVED_DATA == null) return;

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

        public static void ShowLogInQueue()
        {
            if(IsLogQueueEmpty()) return;

            changeLogIcon = true;
            changeLogDesc = true;
            logDesc = pendingLogs[0];

            dc.String classicTitle = Lang.Class.t.texts.get("Schéma obtenu :".AsHaxeString());
            Lang.Class.t.texts.set("Schéma obtenu :".AsHaxeString(), "Item sent:");
            LogItem("GenericKey");
            Lang.Class.t.texts.set("Schéma obtenu :".AsHaxeString(), classicTitle);

            pendingLogs.RemoveAt(0);
        }

        public static bool IsItemQueueEmpty()
        {
            return pendingItems.Count == 0;
        }

        public static bool IsLogQueueEmpty()
        {
            return pendingLogs.Count == 0;
        }

        public static void ClearQueues()
        {
            pendingItems = [];
            pendingLogs = [];
        }
    }
}