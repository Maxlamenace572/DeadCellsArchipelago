using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json.Linq;
using static DeadCellsArchipelago.LinkQueue;

namespace DeadCellsArchipelago
{
    public class TrapLinkManager
    {
        private readonly IArchipelagoSession session;
        private string TrapKey = "DCTrapLink";

        public TrapLinkManager(IArchipelagoSession session, string group)
        {
            TrapKey += group;
            this.session = session;
            session.Socket.PacketReceived += OnPacketReceived;
            session.ConnectionInfo.UpdateConnectionOptions([.. session.ConnectionInfo.Tags, TrapKey]);
        }

        public void SendTrapLink(string trapId)
        {
            BouncePacket bouncePacket = new()
            {
                Tags = [TrapKey],
                Data = new Dictionary<string, JToken>
                {
                    ["trap_id"] = JToken.FromObject(trapId),
                    ["source"] = JToken.FromObject(session.Players.ActivePlayer.Name)
                }
            };

            session.Socket.SendPacketAsync(bouncePacket);
        }

        private void OnPacketReceived(ArchipelagoPacketBase packet)
        {
            if (packet is not BouncedPacket bounced || !bounced.Tags.Contains(TrapKey) || !bounced.Data.TryGetValue("source", out var source)) return;
            
            string userSendingTrap = Convert.ToString(source)!;
            if (userSendingTrap == session.Players.ActivePlayer.Name || !bounced.Data.TryGetValue("trap_id", out var trapId)) return;

            string trapIdString = Convert.ToString(trapId)!;
            AddTrapLinkToQueue(trapIdString, false);
        }
    }
}