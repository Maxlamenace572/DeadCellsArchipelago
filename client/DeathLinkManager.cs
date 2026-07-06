using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json.Linq;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.HeroManager;

namespace DeadCellsArchipelago
{
    public class DeathLinkManager
    {
        private readonly IArchipelagoSession session;
        private string DeathKey = "DeathLink";
        private bool disableDeathLinkForAspects;

        public DeathLinkManager(IArchipelagoSession session, string group, bool disableDeathLinkForAspects)
        {
            DeathKey += group;
            this.session = session;
            this.disableDeathLinkForAspects = disableDeathLinkForAspects;
            session.Socket.PacketReceived += OnPacketReceived;
            session.ConnectionInfo.UpdateConnectionOptions([.. session.ConnectionInfo.Tags, DeathKey]);
        }

        public void SendDeathLink(string message = "")
        {
            if (!disableDeathLinkForAspects || (disableDeathLinkForAspects && SAVED_DATA != null && SAVED_DATA.CountSentAspect() == 13))
            {
                if(message == "")
                {
                    message = $"{session.Players.ActivePlayer.Name} died in Dead Cells";
                }
                BouncePacket bouncePacket = new()
                {
                    Tags = [DeathKey],
                    Data = new Dictionary<string, JToken>
                    {
                        ["time"] = JToken.FromObject(DateTimeOffset.UtcNow.ToUnixTimeSeconds()),
                        ["source"] = JToken.FromObject(session.Players.ActivePlayer.Name),
                        ["cause"] = JToken.FromObject(message)
                    }
                };

                session.Socket.SendPacketAsync(bouncePacket);
            }
        }

        private void OnPacketReceived(ArchipelagoPacketBase packet)
        {
            if (packet is not BouncedPacket bounced || !bounced.Tags.Contains(DeathKey) || !bounced.Data.TryGetValue("source", out var source)) return;
            
            userWithSkillIssue = Convert.ToString(source)!;
            if (userWithSkillIssue != session.Players.ActivePlayer.Name) deathLinkReceived = true;
        }
    }
}