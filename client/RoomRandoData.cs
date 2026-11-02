using Newtonsoft.Json.Linq;

namespace DeadCellsArchipelago
{
    public class RoomRandoData
    {
        public string Mode = "off";
        public Dictionary<string, string> Map = [];
        public List<RRDoor> Doors  = [];

        public void LoadData(JToken token)
        {
            Mode = token["mode"]?.Value<string>()!;
            Map = token["map"]?.ToObject<Dictionary<string, string>>()!;
            foreach (JToken door in token["doors"] ?? new JArray())
                Doors.Add(new RRDoor {
                    From = door["from"]!.Value<string>()!,
                    Original = door["original"]!.Value<string>()!,
                    To = door["to"]!.Value<string>()!,
                });
        }
    }

    public class RRDoor
    {
        public string From = "";
        public string Original = "";
        public string To = "";
    }

    public class BiomeTransitions
    {
        public Dictionary<string, string> TransitionBiome { get; set; } = [];
        public Dictionary<string, string> BiomeTransition { get; set; } = [];
        public HashSet<string> MultiTransition { get; set; } = [];
    }
}