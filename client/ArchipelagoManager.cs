using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Packets;
using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ItemQueue;
using static DeadCellsArchipelago.HeroManager;

namespace DeadCellsArchipelago
{
    public class ArchipelagoManager
    {
        private ArchipelagoSession? _session;
        private DeathLinkService? deathLinkService;
        private bool _isConnected;
        
        // Configurate connection
        private string _serverUrl = "localhost:38281";  // By default
        private string _slotName = "";
        private string? _password = null;

        //options
        public int bscOption;
        public int deathLinkEnabled;
        public bool includeCosmetics;
        
        public bool IsConnected => _isConnected;
        
        public void Connect(string serverUrl, string slotName, string? password = null)
        {
            _serverUrl = serverUrl;
            _slotName = slotName;
            _password = password;
            
            try
            {
                Log.Information($"=== Connecting to Archipelago: {_serverUrl} (slot: {_slotName}) ===");
                
                _session = ArchipelagoSessionFactory.CreateSession(_serverUrl);
                
                // Subscribe to events
                _session.Items.ItemReceived += OnItemReceived;
                _session.Socket.ErrorReceived += OnError;
                _session.Socket.SocketClosed += OnDisconnected;
                
                // Connect
                var result = _session.TryConnectAndLogin(
                    "Dead Cells",           // Game name
                    _slotName,              // Slot name
                    ItemsHandlingFlags.AllItems,
                    new Version(6, 7, 0),
                    password: _password
                );
                
                if (result is LoginSuccessful success)
                {
                    _isConnected = true;
                    Log.Information($"=== Connected to Archipelago ! Slot #{success.Slot} ===");
                    
                    var slotData = success.SlotData;

                    bscOption = Convert.ToInt32(slotData["boss_cells"]);
                    deathLinkEnabled = Convert.ToInt32(slotData["death_link"]);
                    includeCosmetics = Convert.ToBoolean(slotData["include_cosmetics"]);

                    if (deathLinkEnabled >= 0)
                    {
                        deathLinkService = _session.CreateDeathLinkService();
                        deathLinkService.EnableDeathLink();
                        deathLinkService.OnDeathLinkReceived += OnDeathLinkReceived;
                    }

                    // Get every items received
                    SyncReceivedItems();
                }
                else if (result is LoginFailure failure)
                {
                    _isConnected = false;
                    Log.Error($"=== Failed to connect to Archipelago: {string.Join(", ", failure.Errors)} ===");
                }
            }
            catch (Exception ex)
            {
                _isConnected = false;
                Log.Error($"=== Error connecting to Archipelago: {ex.Message} ===");
            }
        }
        
        public void Disconnect()
        {
            if (_session != null)
            {
                _session.Socket.DisconnectAsync();
                _isConnected = false;
                Log.Information("=== Deconnecting from Archipelago ===");
            }
        }
        
        public void SendCheck(string locationName, string internalId, string message)
        {
            if (!_isConnected || _session == null)
            {
                Log.Warning($"=== Impossible to send check to {locationName}: not connected ===");
                return;
            }
            
            try
            {
                // Get localization id from name
                var locationId = _session.Locations.GetLocationIdFromName("Dead Cells", locationName);
                
                if (locationId == -1)
                {
                    Log.Error($"=== Location not found: {locationName} ===");
                    return;
                }

                if (_session.Locations.AllLocationsChecked.Contains(locationId))
                {
                    Log.Error($"=== Location already sent: {locationName} ===");
                    return;
                }

                _session.Locations.CompleteLocationChecks(locationId);
                Log.Information($"=== Location sent: {locationName} (ID: {locationId}) ===");
                SaveChecks(internalId);
            }
            catch (Exception ex)
            {
                Log.Error($"=== Erreur envoi check: {ex.Message} ===");
            }
        }
        
        private void SyncReceivedItems()
        {
            if (_session == null) return;
            
            var receivedItems = _session.Items.AllItemsReceived;
            
            Log.Information($"=== Synchronisation: {receivedItems.Count} items on server ===");
            
            var countDifferent = 0;
            foreach (var item in receivedItems)
            {
                if (SAVED_DATA != null && SAVED_DATA.IsItemRecieved(item.ItemName))
                {
                    AddItemToQueue(item.ItemName);
                    countDifferent++;
                }
            }
            Log.Information($"=== Synchronisation ended with {countDifferent} new items ===");
        }
        
        private void OnItemReceived(ReceivedItemsHelper helper)
        {
            var item = helper.PeekItem();
            AddItemToQueue(item.ItemName);
            helper.DequeueItem();
        }
        
        private void OnError(Exception ex, string message)
        {
            Log.Error($"=== Erreur Archipelago: {message} - {ex.Message} ===");
        }
        
        private void OnDisconnected(string reason)
        {
            _isConnected = false;
            Log.Warning($"=== Déconnecté d'Archipelago: {reason} ===");
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
            if (_session == null) return;
            
            var statusUpdate = new StatusUpdatePacket
            {
                Status = ArchipelagoClientState.ClientGoal
            };
            _session.Socket.SendPacket(statusUpdate);
        }

        private void OnDeathLinkReceived(DeathLink deathLink)
        {
            userWithSkillIssue = deathLink.Source;
            deathLinkReceived = true;
        }

        public void SendDeathLink(string message = "")
        {
            if(message == "")
            {
                message = $"{_slotName} died in Dead Cells";
            }
            if(deathLinkService != null && _session != null) {
                deathLinkService.SendDeathLink(new DeathLink(_slotName, message));
            }
        }
    }
}