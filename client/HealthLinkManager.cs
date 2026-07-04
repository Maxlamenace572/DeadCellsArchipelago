using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Newtonsoft.Json.Linq;

using static DeadCellsArchipelago.LinkQueue;

namespace DeadCellsArchipelago
{
    public class HealthLinkManager
    {
        private string HealthKey = "HealthLink";
        private readonly IArchipelagoSession session;

        public HealthLinkManager(IArchipelagoSession session, string team)
        {
            this.session = session;
            HealthKey += session.Players.ActivePlayer.Team;
            
            JObject values = new()
            {
                ["currentHealth"] = 100,
                ["maxHealth"] = 100

            };
            session.DataStorage[Scope.Game, HealthKey].Initialize(values);

            session.DataStorage[Scope.Game, HealthKey].OnValueChanged += OnValueChanged;
        }

        public void UpdateHealthStorage(int currentHealth, int maxHealth)
        {
            JObject values = new()
            {
                ["currentHealth"] = JToken.FromObject(currentHealth),
                ["maxHealth"] = JToken.FromObject(maxHealth)
            };
            session.DataStorage[Scope.Game, HealthKey] = values;
        }

        private void OnValueChanged(JToken originalValue, JToken newValue, Dictionary<string, JToken> additionalArguments)
        {
            AddHealthLinkToQueue([newValue["currentHealth"]!.Value<int>(), newValue["maxHealth"]!.Value<int>()]);
        }

        public List<int> GetHealthStorage()
        {
            JToken values = session.DataStorage[Scope.Game, HealthKey];
            return [values["currentHealth"]!.Value<int>(), values["maxHealth"]!.Value<int>()];
        }
    }
}