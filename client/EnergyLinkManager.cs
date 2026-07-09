using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json.Linq;
using Serilog;

using static DeadCellsArchipelago.LinkQueue;

namespace DeadCellsArchipelago
{
    public class EnergyLinkManager
    {
        private string EnergyKey = "EnergyLink";
        private readonly IArchipelagoSession session;
        private const long energyPerCell = 100000000;
        private Queue<long> pendingWithdrawals = new();
        private object withdrawLock = new();
        public const double percentTax = 0.8; //lose 20% on deposit

        public EnergyLinkManager(IArchipelagoSession session)
        {
            this.session = session;
            EnergyKey += session.Players.ActivePlayer.Team;

            session.DataStorage[EnergyKey].Initialize(JToken.FromObject(0));

            session.Socket.PacketReceived += OnPacketReceived;
            session.DataStorage[EnergyKey].OnValueChanged += OnEnergyValueChanged;
        }


        public void DepositCells(int cellCount)
        {
            long energyToAdd = (long)(cellCount * percentTax) * energyPerCell;

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

                AddEnergyLinkToQueue(cellsReceived, 0);
            }
        }

        public int ShowStorageNumberCells()
        {
            if (session == null) return 0;
            JToken value = session.DataStorage[EnergyKey];
            return (int)(value.ToObject<long>() / energyPerCell);
        }

        private void OnEnergyValueChanged(JToken originalValue, JToken newValue, Dictionary<string, JToken> additionalArguments)
        {
            AddEnergyLinkToQueue((int)(newValue.ToObject<long>() / energyPerCell), 1);
        }
    }
}