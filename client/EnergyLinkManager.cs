using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json.Linq;
using Serilog;

namespace DeadCellsArchipelago
{
    public class EnergyLinkManager
    {
        public string EnergyKey = "EnergyLink";
        private readonly IArchipelagoSession session;
        const long energyPerCell = 100000000;
        private Queue<long> pendingWithdrawals = new();
        private object withdrawLock = new();

        public EnergyLinkManager(IArchipelagoSession session, string team)
        {
            this.session = session;
            EnergyKey += team;
            session.Socket.PacketReceived += OnPacketReceived;
        }


        public void DepositCells(int cellCount)
        {
            long energyToAdd = cellCount * energyPerCell;

            var packet = new SetPacket
            {
                Key = EnergyKey,
                DefaultValue = 0,
                WantReply = false,
                Operations =
                [
                    new OperationSpecification
                    {
                        OperationType = OperationType.Add,
                        Value = energyToAdd
                    },
                    new OperationSpecification
                    {
                        OperationType = OperationType.Max,
                        Value = 0
                    }
                ]
            };

            session.Socket.SendPacket(packet);
        }

        public void WithdrawCells(int cellsRequested)
        {
            if (session == null) return;
            long energyRequested = cellsRequested * energyPerCell;

            lock (withdrawLock)
            {
                pendingWithdrawals.Enqueue(energyRequested);
            }

            var packet = new SetPacket
            {
                Key = EnergyKey,
                DefaultValue = 0,
                WantReply = true,
                Operations =
                [
                    new OperationSpecification
                    {
                        OperationType = OperationType.Add,
                        Value = -energyRequested
                    },
                    new OperationSpecification
                    {
                        OperationType = OperationType.Max,
                        Value = 0
                    }
                ]
            };

            session.Socket.SendPacket(packet);
        }

        private void OnPacketReceived(ArchipelagoPacketBase packet)
        {
            if (packet is SetReplyPacket reply && reply.Key == EnergyKey)
            {
                long energyRequested;
                lock (withdrawLock)
                {
                    if (pendingWithdrawals.Count == 0) return;
                    energyRequested = pendingWithdrawals.Dequeue();
                }
                long energyBefore = reply.OriginalValue.ToObject<long>();
                long energyAfter = reply.Value.ToObject<long>();
                long energyConsumed = energyBefore - energyAfter;

                long energyActuallyGot = Math.Min(energyConsumed, energyRequested);
                int cellsReceived = (int)(energyActuallyGot / energyPerCell);

                GiveCellsToPlayer(cellsReceived);
            }
        }

        private void GiveCellsToPlayer(int cellsReceived)
        {
            Log.Warning($"todo: {cellsReceived}");
        }

        public async void ShowStorageNumberCells()
        {
            if (session == null) return;
            JToken value = await session.DataStorage[EnergyKey].GetAsync();
            Log.Warning($"{value.ToObject<long>() / energyPerCell}");
        }
    }
}