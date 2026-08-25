using dc.h2d;
using Serilog;

using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class BiomeLine : Line
    {
        public List<BiomeCell> cells = [];
        public Flow flow;

        public BiomeLine(double x, double y, string level1, string level2, string level3, Dictionary<string, HashSet<string>> data)
            : base(0, 0, x, y, 0)
        {
            flow = new Flow(null)
            {
                x = x,
                y = y
            };
            flow.set_horizontalSpacing(50);

            cells.Add(new BiomeCell(0, 0, flow, level1, GetRelatedData(data, level1)));
            cells.Add(new BiomeCell(0, 0, flow, level2, GetRelatedData(data, level2)));
            cells.Add(new BiomeCell(0, 0, flow, level3, GetRelatedData(data, level3)));
        }

        public override void AddParent(dc.h2d.Object parent)
        {
            parent.addChild(flow);
        }

        public void Highlight(int index)
        {
            cells[index].Highlight();
        }

        public void StopHighlight(int index)
        {
            cells[index].StopHighlight();
        }

        public void Locked(int index)
        {
            cells[index].Locked();
        }

        public void SetPopUpTracker(int index)
        {
            cells[index].SetPopUpTracker();
            popUpTracker?.biomeCellIndex = index;
        }

        public Dictionary<string, HashSet<string>> GetBiomeData(int index)
        {
            return cells[index].data;
        }

        public string GetBiomeId(int index)
        {
            return cells[index].biomeId;
        }

        public Dictionary<string, HashSet<string>> GetRelatedData(Dictionary<string, HashSet<string>> data, string biomeId)
        {
            Dictionary<string, HashSet<string>> res = [];

            if (biomeId == "Other")
            {
                res["AllT"] = data["AllT"];
                res["AllR"] = data["AllR"];
                res["TChallengeT"] = data["TChallengeT"];
                res["RChallengeT"] = data["RChallengeT"];
                res["TAspect"] = data["TAspect"];
                res["RAspect"] = data["RAspect"];
                return res;
            }

            List<string> start = ["T", "R"];
            foreach (string kindS in start)
            {
                List<string> end = ["0", "1", "2", "3", "4", "5", "T"];
                foreach (string kindE in end)
                {
                    string key = $"{kindS}{biomeId}{kindE}";
                    if (data.ContainsKey(key))
                    {
                        res[key] = data[key];
                    }
                }
            }
            return res;
        }

        public void SetIcons(int index, List<List<string>> lines)
        {
            cells[index].SetIcons(lines);
        }
    }
}