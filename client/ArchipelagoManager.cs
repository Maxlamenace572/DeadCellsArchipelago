using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Packets;
using Serilog;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.ItemQueue;
using static DeadCellsArchipelago.Translator;
using static DeadCellsArchipelago.BlueprintManager;
using System.Collections.ObjectModel;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using System.Net.WebSockets;

namespace DeadCellsArchipelago
{
    public class ArchipelagoManager
    {
        private ArchipelagoSession? session;
        public DeathLinkManager? deathLinkManager;
        public DamageLinkManager? damageLinkManager;
        public HealthLinkManager? healthLinkManager;
        public TrapLinkManager? trapLinkManager;
        public EnergyLinkManager? energyLinkManager;
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
        public string? version;
        public string deathLinkGroup = "";
        public bool deathTrap;
        public bool deathTrapLink;
        public bool damageLink;
        public string damageLinkGroup = "";
        public bool healthLink;
        public string healthLinkGroup = "";
        public bool healthCurseLink;
        public bool trapLink;
        public string trapLinkGroup = "";
        
        public void Connect(string serverUrl, string slotName, string? password = null)
        {
            this.serverUrl = serverUrl;
            this.slotName = slotName;
            this.password = password;
            
            try
            {
                Log.Information($"[AP] Connecting to Archipelago: {serverUrl} (slot: {slotName})");
                
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
                    new Version(6, 7, 1),
                    password: password
                );
                
                if (result is LoginSuccessful success)
                {
                    isConnected = true;
                    Log.Information($"[AP] Connected to Archipelago ! Slot {success.Slot}");
                    
                    var slotData = success.SlotData;

                    if (slotData.ContainsKey("boss_cells")) bscOption = Convert.ToInt32(slotData["boss_cells"]);
                    if (slotData.ContainsKey("death_link")) deathLinkEnabled = Convert.ToInt32(slotData["death_link"]);
                    if (slotData.ContainsKey("include_cosmetics")) includeCosmetics = Convert.ToBoolean(slotData["include_cosmetics"]);
                    if (slotData.ContainsKey("death_link_aspect")) disableDeathLinkForAspects = Convert.ToBoolean(slotData["death_link_aspect"]);
                    if (slotData.ContainsKey("respawn_up")) respawnUpScroll = Convert.ToBoolean(slotData["respawn_up"]);
                    if (slotData.ContainsKey("dlc_rise_of_the_giant")) riseOfTheGiant = Convert.ToBoolean(slotData["dlc_rise_of_the_giant"]);
                    if (slotData.ContainsKey("dlc_the_bad_seed")) theBadSeed = Convert.ToBoolean(slotData["dlc_the_bad_seed"]);
                    if (slotData.ContainsKey("dlc_fatal_falls")) fatalFalls = Convert.ToBoolean(slotData["dlc_fatal_falls"]);
                    if (slotData.ContainsKey("dlc_the_queen_and_the_sea")) theQueenAndTheSea = Convert.ToBoolean(slotData["dlc_the_queen_and_the_sea"]);
                    if (slotData.ContainsKey("dlc_return_to_castlevania")) returnToCastlevania = Convert.ToBoolean(slotData["dlc_return_to_castlevania"]);

                    if (slotData.ContainsKey("apworld_version")) version = Convert.ToString(slotData["apworld_version"]) ?? "-0.1.1";

                    if (slotData.ContainsKey("death_link_group")) deathLinkGroup = Convert.ToString(slotData["death_link_group"]) ?? "";
                    if (slotData.ContainsKey("death_trap")) deathTrap = Convert.ToBoolean(slotData["death_trap"]);
                    if (slotData.ContainsKey("death_trap_link")) deathTrapLink = Convert.ToBoolean(slotData["death_trap_link"]);
                    if (slotData.ContainsKey("damage_link")) damageLink = Convert.ToBoolean(slotData["damage_link"]);
                    if (slotData.ContainsKey("damage_link_group")) damageLinkGroup = Convert.ToString(slotData["damage_link_group"]) ?? "";
                    if (slotData.ContainsKey("health_link")) healthLink = Convert.ToBoolean(slotData["health_link"]);
                    if (slotData.ContainsKey("health_link_group")) healthLinkGroup = Convert.ToString(slotData["health_link_group"]) ?? "";
                    if (slotData.ContainsKey("health_curse_link")) healthCurseLink = Convert.ToBoolean(slotData["health_curse_link"]);
                    if (slotData.ContainsKey("trap_link")) trapLink = Convert.ToBoolean(slotData["trap_link"]);
                    if (slotData.ContainsKey("trap_link_group")) trapLinkGroup = Convert.ToString(slotData["trap_link_group"]) ?? "";

                    energyLinkManager = new EnergyLinkManager(session);
                    if (deathLinkEnabled >= 0) deathLinkManager = new DeathLinkManager(session, deathLinkGroup, disableDeathLinkForAspects, deathTrap, deathTrapLink);
                    if (damageLink) damageLinkManager = new DamageLinkManager(session, damageLinkGroup);
                    if (healthLink) healthLinkManager = new HealthLinkManager(session, healthLinkGroup, healthCurseLink);
                    if (trapLink) trapLinkManager = new TrapLinkManager(session, trapLinkGroup);
                }
                else if (result is LoginFailure failure)
                {
                    isConnected = false;
                    Log.Error($"[AP] Failed to connect to Archipelago: {string.Join(", ", failure.Errors)}");
                }
            }
            catch (Exception ex)
            {
                isConnected = false;
                Log.Error($"[AP] Error connecting to Archipelago: {ex.Message}");
            }
        }

        public void Disconnect()
        {
            if (session != null)
            {
                session.Socket.DisconnectAsync();
                isConnected = false;
                Log.Information("[AP] Disconnecting from Archipelago");
            }
        }
        
        public void SendCheck(string locationName, string internalId, string message)
        {
            if (!isConnected || session == null)
            {
                SAVED_DATA?.SaveOfflineCheck(internalId, locationName);
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
                    Log.Error($"[AP] Location not found: {locationName}");
                    return;
                }

                if (session.Locations.AllLocationsChecked.Contains(locationId))
                {
                    Log.Error($"[AP] Location already sent: {locationName}");
                    return;
                }

                session.Locations.CompleteLocationChecks(locationId);
                Log.Information($"[AP] Location sent: {locationName} (ID: {locationId})");
                SaveChecks(internalId);
            }
            catch (Exception ex)
            {
                Log.Error($"[AP] Error while sending check: {ex.Message}");
            }
        }

        public void SyncAll()
        {
            ClearQueues();
            SyncReceivedItems();
            SyncReceivedLocations();
            SyncOfflineChecks();
        }

        public void SyncOfflineChecks()
        {
            if (SAVED_DATA == null) return;

            foreach(KeyValuePair<string, string> check in SAVED_DATA.OfflineChecks)
            {
                SendCheck(check.Key, check.Value, "");
                SAVED_DATA.OfflineChecks.Remove(check.Key);
                if (USER != null) SAVED_DATA.RemoveFromOfflineChecksJson(check.Key, USER.userId);
            }
        }

        private void SyncReceivedItems()
        {
            if (session == null) return;
            
            var receivedItems = session.Items.AllItemsReceived;
            
            Log.Information($"[AP] Synchronisation: {receivedItems.Count} items on server");
            
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
            Log.Information($"[AP] Synchronisation ended with {countDifferent} new items");
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
            
            Log.Information($"[AP] Synchronisation: {checkedLocations.Count} locations on server");
            
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
            Log.Information($"[AP] Synchronisation ended with {countDifferent} new location");
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
            Log.Error($"[AP] Archipelago Error: {message}");
            if (ex is WebSocketException)
            {
                Log.Warning($"[AP] Disconnecting...");
                isConnected = false;
                logError = true;
                logDesc = "Disconnected from server";
            }
        }
        
        private void OnDisconnected(string reason)
        {
            isConnected = false;
            Log.Warning($"[AP] Disconnected from Archipelago: {reason}");
        }

        private void SaveChecks(string internalId)
        {
            if (SAVED_DATA == null) return;

            SAVED_DATA.SaveCheckSent(internalId);
            if(USER != null)
            {
                SAVED_DATA.AppendToSentChecksJson(internalId, USER.userId);
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

        private void OnMessageReceived(LogMessage message)
        {
            if (message is ItemSendLogMessage)
            {
                if (message is ItemCheatLogMessage || message is HintItemSendLogMessage) return;

                ItemSendLogMessage itemMessage = (ItemSendLogMessage) message;
                if (itemMessage.IsSenderTheActivePlayer && !itemMessage.IsReceiverTheActivePlayer)
                {
                    AddLogToQueue($"{itemMessage.Item.ItemName} to {itemMessage.Receiver}");
                }
            }
        }
    }
}