using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Packets;
using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ItemQueue;
using static DeadCellsArchipelago.HeroManager;
using static DeadCellsArchipelago.Translator;
using System.Collections.ObjectModel;
using Archipelago.MultiClient.Net.MessageLog.Messages;

namespace DeadCellsArchipelago
{
    public class ArchipelagoManager
    {
        private ArchipelagoSession? session;
        private DeathLinkService? deathLinkService;
        public bool isConnected;
        
        // Configurate connection
        private string serverUrl = "localhost:38281";
        private string slotName = "";
        private string? password = null;

        //options
        public int bscOption;
        public int deathLinkEnabled;
        public bool includeCosmetics;
        public bool disableDeathLinkForAspects;
        public bool respawnUpScroll;
        public bool riseOfTheGiant;
        public bool theBadSeed;
        public bool fatalFalls;
        public bool theQueenAndTheSea;
        public bool returnToCastlevania;
        
        public void Connect(string serverUrl, string slotName, string? password = null)
        {
            this.serverUrl = serverUrl;
            this.slotName = slotName;
            this.password = password;
            
            try
            {
                Log.Information($"=== Connecting to Archipelago: {serverUrl} (slot: {slotName}) ===");
                
                session = ArchipelagoSessionFactory.CreateSession(serverUrl);
                
                // Subscribe to events
                session.Items.ItemReceived += OnItemReceived;
                session.Locations.CheckedLocationsUpdated += OnLocationsChecked;
                session.Socket.ErrorReceived += OnError;
                session.Socket.SocketClosed += OnDisconnected;
                session.MessageLog.OnMessageReceived += OnMessageReceived;

                //session
                
                // Connect
                var result = session.TryConnectAndLogin(
                    "Dead Cells",
                    slotName,
                    ItemsHandlingFlags.AllItems,
                    new Version(6, 7, 0),
                    password: password
                );
                
                if (result is LoginSuccessful success)
                {
                    isConnected = true;
                    Log.Information($"=== Connected to Archipelago ! Slot #{success.Slot} ===");
                    
                    var slotData = success.SlotData;

                    bscOption = Convert.ToInt32(slotData["boss_cells"]);
                    deathLinkEnabled = Convert.ToInt32(slotData["death_link"]);
                    includeCosmetics = Convert.ToBoolean(slotData["include_cosmetics"]);
                    disableDeathLinkForAspects = Convert.ToBoolean(slotData["death_link_aspect"]);
                    respawnUpScroll = Convert.ToBoolean(slotData["respawn_up"]);
                    riseOfTheGiant = Convert.ToBoolean(slotData["dlc_rise_of_the_giant"]);
                    theBadSeed = Convert.ToBoolean(slotData["dlc_the_bad_seed"]);
                    fatalFalls = Convert.ToBoolean(slotData["dlc_fatal_falls"]);
                    theQueenAndTheSea = Convert.ToBoolean(slotData["dlc_the_queen_and_the_sea"]);
                    returnToCastlevania = Convert.ToBoolean(slotData["dlc_return_to_castlevania"]);

                    if (deathLinkEnabled >= 0)
                    {
                        deathLinkService = session.CreateDeathLinkService();
                        deathLinkService.EnableDeathLink();
                        deathLinkService.OnDeathLinkReceived += OnDeathLinkReceived;
                    }
                }
                else if (result is LoginFailure failure)
                {
                    isConnected = false;
                    Log.Error($"=== Failed to connect to Archipelago: {string.Join(", ", failure.Errors)} ===");
                }
            }
            catch (Exception ex)
            {
                isConnected = false;
                Log.Error($"=== Error connecting to Archipelago: {ex.Message} ===");
            }
        }

        public void Disconnect()
        {
            if (session != null)
            {
                session.Socket.DisconnectAsync();
                isConnected = false;
                Log.Information("=== Disconnecting from Archipelago ===");
            }
        }
        
        public void SendCheck(string locationName, string internalId, string message)
        {
            if (!isConnected || session == null)
            {
                Log.Warning($"=== Impossible to send check to {locationName}: not connected ===");
                return;
            }
            
            try
            {
                if (IdToNameKeyExist(locationName))
                {
                    locationName = GetName(locationName);
                }

                // Get localization id from name
                var locationId = session.Locations.GetLocationIdFromName("Dead Cells", locationName);
                
                if (locationId == -1)
                {
                    Log.Error($"=== Location not found: {locationName} ===");
                    return;
                }

                if (session.Locations.AllLocationsChecked.Contains(locationId))
                {
                    Log.Error($"=== Location already sent: {locationName} ===");
                    return;
                }

                session.Locations.CompleteLocationChecks(locationId);
                Log.Information($"=== Location sent: {locationName} (ID: {locationId}) ===");
                SaveChecks(internalId);
            }
            catch (Exception ex)
            {
                Log.Error($"=== Error while sending chacke: {ex.Message} ===");
            }
        }

        public void SyncAll()
        {
            ClearQueues();
            SyncReceivedItems();
            SyncReceivedLocations();
        }
        
        private void SyncReceivedItems()
        {
            if (session == null) return;
            
            var receivedItems = session.Items.AllItemsReceived;
            
            Log.Information($"=== Synchronisation: {receivedItems.Count} items on server ===");
            
            var countDifferent = 0;
            foreach (var item in receivedItems)
            {
                if (SAVED_DATA != null && SAVED_DATA.IsItemReceived(item.ItemName))
                {
                    continue;
                }
                AddItemToQueue(item.ItemName);
                countDifferent++;
            }
            Log.Information($"=== Synchronisation ended with {countDifferent} new items ===");
        }
        
        private void OnItemReceived(ReceivedItemsHelper helper)
        {
            var item = helper.PeekItem();
            AddItemToQueue(item.ItemName);
            helper.DequeueItem();
        }

        private void SyncReceivedLocations()
        {
            if (session == null || SAVED_DATA == null) return;
            
            var checkedLocations = session.Locations.AllLocationsChecked;
            
            Log.Information($"=== Synchronisation: {checkedLocations.Count} locations on server ===");
            
            var countDifferent = 0;
            foreach (var locationId in checkedLocations)
            {
                string locationName = session.Locations.GetLocationNameFromId(locationId);

                string locationGameId = locationName;
                if (FullNameToIdKeyExist(locationGameId))
                {
                    locationGameId = GetId(locationGameId);
                }

                if (!SAVED_DATA.IsCheckSent(locationGameId))
                {
                    SaveChecks(locationGameId);
                    countDifferent++;
                }
            }
            Log.Information($"=== Synchronisation ended with {countDifferent} new location ===");
        }

        private void OnLocationsChecked(ReadOnlyCollection<long> newCheckedLocations)
        {
            if (session == null || SAVED_DATA == null ) return;

            foreach(long locationId in newCheckedLocations)
            {
                string locationGameId = session.Locations.GetLocationNameFromId(locationId);;
                if (FullNameToIdKeyExist(locationGameId)) locationGameId = GetId(locationGameId);

                if (!SAVED_DATA.IsCheckSent(locationGameId)) SaveChecks(locationGameId);
            }
        }
        
        private void OnError(Exception ex, string message)
        {
            Log.Error($"=== Archipelago Error: {message} - {ex.Message} ===");
        }
        
        private void OnDisconnected(string reason)
        {
            isConnected = false;
            Log.Warning($"=== Disconnected from Archipelago: {reason} ===");
        }

        private void SaveChecks(string internalId)
        {
            if (SAVED_DATA != null)
            {
                SAVED_DATA.SaveCheckSent(internalId);
                if(USER != null)
                {
                    SAVED_DATA.AppendToSentChecksJson(internalId, USER.userId);
                }
            }
            else
            {
                Log.Error("=== Couldn't save check ===");
            }
        }

        public void SendVictory()
        {
            if (session == null) return;
            
            var statusUpdate = new StatusUpdatePacket
            {
                Status = ArchipelagoClientState.ClientGoal
            };
            session.Socket.SendPacket(statusUpdate);
        }

        private void OnDeathLinkReceived(DeathLink deathLink)
        {
            userWithSkillIssue = deathLink.Source;
            deathLinkReceived = true;
        }

        public void SendDeathLink(string message = "")
        {
            if (!disableDeathLinkForAspects || disableDeathLinkForAspects && SAVED_DATA != null && SAVED_DATA.CountSentAspect() == 13)
            {
                if(message == "")
                {
                    message = $"{slotName} died in Dead Cells";
                }
                if(deathLinkService != null && session != null) {
                    deathLinkService.SendDeathLink(new DeathLink(slotName, message));
                }
            }
        }

        private void OnMessageReceived(LogMessage message)
        {
            if (message is ItemSendLogMessage)
            {
                if (message is ItemCheatLogMessage || message is HintItemSendLogMessage) return;

                ItemSendLogMessage itemMessage = (ItemSendLogMessage) message;
                if (itemMessage.IsSenderTheActivePlayer && !itemMessage.IsReceiverTheActivePlayer)
                {
                    Log.Warning($"{itemMessage.Item.ItemName} to {itemMessage.Receiver}");
                    AddLogToQueue($"{itemMessage.Item.ItemName} to {itemMessage.Receiver}");
                }
            }
        }
    }
}