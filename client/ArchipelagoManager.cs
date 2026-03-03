using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using ModCore.Utilities;
using Serilog;
using System.Collections.Generic;
using System.Linq;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago
{
    public class ArchipelagoManager
    {
        private ArchipelagoSession? _session;
        private bool _isConnected;
        
        // Configurate connection
        private string _serverUrl = "localhost:38281";  // By default
        private string _slotName = "";
        private string? _password = null;
        private bool _mockMode = false;

        public void EnableMockMode() //used only for tests
        {
            _mockMode = true;
            _isConnected = true;
            Log.Information("=== Mode mock Archipelago activated ===");
        }
        
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
                    new Version(0, 1, 0),   // Mod version
                    password: _password
                );
                
                if (result is LoginSuccessful success)
                {
                    _isConnected = true;
                    Log.Information($"=== Connected to Archipelago ! Slot #{success.Slot} ===");
                    
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
        
        public void SendCheck(string locationName, string message)
        {
            if (_mockMode) //log check when we are on test mod
            {
                Log.Information($"=== [MOCK] Check sent: {message} {locationName} ===");
                
                // Simulate a blueprint send from server
                Log.Information($"=== [MOCK] Simulate item send ===");
                GiveItemFromArchipelago("Flask1");
                GiveItemFromArchipelago("BlobbyFlame");
                GiveItemFromArchipelago("LadderKey");//LadderKey//TeleportKey//BreakableGroundKey
                SaveChecks(locationName);
                return;
            }

            
            if (!_isConnected || _session == null)
            {
                Log.Warning($"=== Impossible to send check to {locationName}: not connected ===");
                return;
            }
            
            try
            {
                // Get localization id from name
                var locationId = _session.Locations.GetLocationIdFromName("Dead Cells", locationName);
                
                _session.Locations.CompleteLocationChecks(locationId);
                Log.Information($"=== Check sent: {locationName} (ID: {locationId}) ===");
                SaveChecks(locationName);
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
            
            Log.Information($"=== Synchronisation: {receivedItems.Count} items reçus ===");
            
            foreach (var item in receivedItems)
            {
                ProcessReceivedItem(item);
            }
        }
        
        private void OnItemReceived(ReceivedItemsHelper helper)
        {
            var item = helper.PeekItem();
            ProcessReceivedItem(item);
            helper.DequeueItem();
        }
        
        private void ProcessReceivedItem(ItemInfo item) //TODO: finish this method when the client works
        {
            if (_session == null) return;
            
            var itemName = item.ItemName;
            Log.Information($"=== Item reçu d'Archipelago: {itemName} ===");
            
            // Donner l'item au joueur selon son type
            if (itemName.StartsWith("Blueprint: "))
            {
                var blueprintId = itemName.Replace("Blueprint: ", "");
                BlueprintManager.UnlockBlueprint(blueprintId);
            }
            else if (itemName.StartsWith("Scroll: "))
            {
                // TODO: gérer les parchemins
            }
            // Ajoute d'autres types d'items ici
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

        private void SaveChecks(string locationName)
        {
            if (SAVED_DATA != null)
            {
                SAVED_DATA.SaveCheckSent(locationName);
            } else
            {
                Log.Error("=== Couldn't save check ===");
            }
        }
    }
}