using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Packets;
using dc.haxe;
using Newtonsoft.Json.Linq;

using static DeadCellsArchipelago.LinkQueue;

namespace DeadCellsArchipelago
{
    public class HealthLinkManager
    {
        private string HealthKey = "HealthLink";
        private readonly IArchipelagoSession session;
        public bool shareCurses;

        public HealthLinkManager(IArchipelagoSession session, string group, bool shareCurses)
        {
            HealthKey += group;
            this.session = session;
            this.shareCurses = shareCurses;
            
            JObject values = new()
            {
                ["currentHealth"] = JToken.FromObject(100),
                ["maxHealth"] = JToken.FromObject(100),
                ["dead"] = JToken.FromObject(false),
                ["player"] = JToken.FromObject("")
            };
            session.DataStorage[Scope.Game, HealthKey].Initialize(values);

            values = new()
            {
                ["currentCurses"] = 0,
                ["player"] = ""
            };
            session.DataStorage[Scope.Game, HealthKey + "Curses"].Initialize(values);

            session.DataStorage[Scope.Game, HealthKey].OnValueChanged += OnHealthValueChanged;
            if (shareCurses) session.DataStorage[Scope.Game, HealthKey + "Curses"].OnValueChanged += OnCurseValueChanged;
        }

        public void UpdateHealthStorage(int currentHealth, int maxHealth)
        {
            if (currentHealth > 0)
            {
                JObject values = new()
                {
                    ["currentHealth"] = JToken.FromObject(currentHealth),
                    ["maxHealth"] = JToken.FromObject(maxHealth),
                    ["dead"] = JToken.FromObject(false),
                    ["player"] = JToken.FromObject(session.Players.ActivePlayer.Name),
                };
                session.DataStorage[Scope.Game, HealthKey] = values;
            }
            else
            {
                JObject values = new()
                {
                    ["currentHealth"] = JToken.FromObject(100),
                    ["maxHealth"] = JToken.FromObject(100),
                    ["dead"] = JToken.FromObject(true),
                    ["player"] = JToken.FromObject(session.Players.ActivePlayer.Name),
                };
                session.DataStorage[Scope.Game, HealthKey] = values;

                values = new()
                {
                    ["currentCurses"] = JToken.FromObject(0),
                    ["player"] = JToken.FromObject(session.Players.ActivePlayer.Name),
                };
                session.DataStorage[Scope.Game, HealthKey + "Curses"] = values;
            }
        }

        public void UpdateCurseStorage(int currentCurse)
        {
            if (!shareCurses) return;

            JObject values = new()
            {
                ["currentCurses"] = JToken.FromObject(currentCurse),
                ["player"] = JToken.FromObject(session.Players.ActivePlayer.Name),
            };
            session.DataStorage[Scope.Game, HealthKey + "Curses"] = values;
        }

        private void OnHealthValueChanged(JToken originalValue, JToken newValue, Dictionary<string, JToken> additionalArguments)
        {
            if (newValue["player"]!.Value<string>() == session.Players.ActivePlayer.Name) return;
            healthLinkDeath = newValue["dead"]!.Value<bool>();
            AddHealthLinkToQueue([newValue["currentHealth"]!.Value<int>(), newValue["maxHealth"]!.Value<int>()]);
        }

        private void OnCurseValueChanged(JToken originalValue, JToken newValue, Dictionary<string, JToken> additionalArguments)
        {
            if (newValue["player"]!.Value<string>() == session.Players.ActivePlayer.Name) return;
            AddHealthCurseLinkToQueue(newValue["currentCurses"]!.Value<int>());
        }

        public List<int> GetHealthStorage()
        {
            JToken values = session.DataStorage[Scope.Game, HealthKey].GetAsync().Result;
            return [values["currentHealth"]!.Value<int>(), values["maxHealth"]!.Value<int>()];
        }

        public int GetHealthCurseStorage()
        {
            JToken values = session.DataStorage[Scope.Game, HealthKey + "Curses"].GetAsync().Result;
            return values["currentCurses"]!.Value<int>();
        }
    }
}