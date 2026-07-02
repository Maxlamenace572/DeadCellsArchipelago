using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json.Linq;

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

        public DamageLinkManager(IArchipelagoSession session, string? group)
        {
            if (group != null) DamageKey += group;
            this.session = session;
            session.Socket.PacketReceived += OnPacketReceived;
        }

        public void OnPlayerDamaged(float percentHpLost)
        {
            accumulatedPercentage += percentHpLost;
            int damagePoints = (int)accumulatedPercentage * DamagePointsPerHp;
            accumulatedPercentage %= 1;
            if (damagePoints <= 0) return;

            Dictionary<string, JToken> bounceData = new()
            {
                ["time"] = DateTimeOffset.UtcNow.ToUnixTimeSeconds(),
                ["source"] = session.Players.ActivePlayer.Name,
                ["damage_points"] = damagePoints
            };

            BouncePacket packet = new()
            {
                Tags = [DamageKey],
                Data = bounceData
            };

            session.Socket.SendPacket(packet);
        }

        private void OnPacketReceived(ArchipelagoPacketBase packet)
        {
            if (packet is not BouncedPacket bounced) return;
            if (!bounced.Tags.Contains(DamageKey)) return;
            
            if (!bounced.Data.TryGetValue("damage_points", out var dmgValue)) return;

            int receivedPoints = Convert.ToInt32(dmgValue);
            lock (damageLock)
            {
                accumulatedDamagePoint += receivedPoints;

                if (accumulatedDamagePoint >= DamagePointsPerHp)
                {
                    int percentageLost = (int)(accumulatedDamagePoint / DamagePointsPerHp);
                    accumulatedDamagePoint %= DamagePointsPerHp;
                    ApplyDamageToPlayer(percentageLost);
                }
            }
        }

        private void ApplyDamageToPlayer(int percentageLost)
        {
            // TODO: hook vers Dead Cells pour infliger des dégâts
            // ex: GameHooks.HurtPlayer(damageAmount);
        }
    }
}