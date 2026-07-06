using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json.Linq;
using static DeadCellsArchipelago.HeroManager;

namespace DeadCellsArchipelago
{
    public class DamageLinkManager
    {
        private readonly IArchipelagoSession session;
        private string DamageKey = "SharedDamage";
        private float accumulatedDamagePoint;
        private float accumulatedPercentage;
        private readonly object damageLock = new object();
        private const int DamagePointsPerHp = 16; //16 pt <=> 1%

        public DamageLinkManager(IArchipelagoSession session, string group)
        {
            DamageKey += group;
            this.session = session;
            session.Socket.PacketReceived += OnPacketReceived;
            session.ConnectionInfo.UpdateConnectionOptions([.. session.ConnectionInfo.Tags, DamageKey]);
        }

        public void OnPlayerDamaged(float percentHpLost)
        {
            accumulatedPercentage += percentHpLost;
            int damagePoints = (int)accumulatedPercentage * DamagePointsPerHp;
            accumulatedPercentage %= 1;
            if (damagePoints <= 0) return;

            BouncePacket packet = new()
            {
                Tags = [DamageKey],
                Data = new Dictionary<string, JToken>
                {
                    ["time"] = DateTimeOffset.UtcNow.ToUnixTimeSeconds(),
                    ["source"] = session.Players.ActivePlayer.Name,
                    ["damage_points"] = damagePoints
                }
            };

            session.Socket.SendPacket(packet);
        }

        private void OnPacketReceived(ArchipelagoPacketBase packet)
        {
            if (packet is not BouncedPacket bounced || !bounced.Tags.Contains(DamageKey) || !bounced.Data.TryGetValue("damage_points", out var dmgValue)) return;

            int receivedPoints = Convert.ToInt32(dmgValue);
            lock (damageLock)
            {
                accumulatedDamagePoint += receivedPoints;

                if (accumulatedDamagePoint >= DamagePointsPerHp)
                {
                    int percentageLost = (int)(accumulatedDamagePoint / DamagePointsPerHp);
                    accumulatedDamagePoint %= DamagePointsPerHp;
                    RemovePercentHealth(percentageLost);
                }
            }
        }
    }
}