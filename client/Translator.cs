using System.Text.Json;

namespace DeadCellsArchipelago
{
    public static class Translator
    {
        public static Dictionary<string, string> IdToApName = new Dictionary<string, string>();
        public static Dictionary<string, string> ApNameToId = new Dictionary<string, string>();


        public static Dictionary<string, string> LoadModApTranslation()
        {
                var json = File.ReadAllText(GetModApTradFilePath());
                var result = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
                return result ?? throw new InvalidDataException("error on the JSON translator");
        }

        public static Dictionary<string, string> Invert(Dictionary<string, string> source)
        {
            var inverted = new Dictionary<string, string>(source.Count);

            foreach (var (key, value) in source)
            {
                if (!inverted.TryAdd(value, key))
                    throw new InvalidOperationException(
                        $"error on \"{value}\", it appear multiple times.");
            }

            return inverted;
        }

        public static string GetModApTradFilePath()
        {
            return Path.Combine(AppContext.BaseDirectory, "..", "..", "mods", "DeadCellsArchipelago", "gameId-apName.json");
        }

        public static bool IdToNameKeyExist(string id)
        {
            return IdToApName.ContainsKey(id);
        }

        public static bool NameToIdKeyExist(string name)
        {
            return ApNameToId.ContainsKey(name);
        }

        public static string GetName(string id)
        {
            return IdToApName[id];
        }

        public static string GetId(string name)
        {
            if (name.Length >= 6)
            {
                if (name[^6..] == " Enter")
                {
                    return $"{ApNameToId[name[..^6]]} Enter";
                } else if (name[^5..] == " Exit")
                {
                    return $"{ApNameToId[name[..^5]]} Exit";
                }
            }
            return ApNameToId[name];
        }

        public static bool FullNameToIdKeyExist(string name)
        {
            if (name.Length >= 6)
            {
                if (name[^6..] == " Enter")
                {
                    name = name[..^6];
                } else if (name[^5..] == " Exit")
                {
                    name = name[..^5];
                }
            }
            return ApNameToId.ContainsKey(name);
        }
    }
}