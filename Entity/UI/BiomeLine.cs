using dc.h2d;
using Serilog;

using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class BiomeLine : Line
    {
        public BiomeCell cell1;
        public BiomeCell cell2;
        public BiomeCell cell3;
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

            cell1 = new BiomeCell(0, 0, flow, level1, GetRelatedData(data, level1));
            cell2 = new BiomeCell(0, 0, flow, level2, GetRelatedData(data, level2));
            cell3 = new BiomeCell(0, 0, flow, level3, GetRelatedData(data, level3));
        }

        public override void AddParent(dc.h2d.Object parent)
        {
            parent.addChild(flow);
        }

        public void Highlight(int index)
        {
            switch (index)
            {
                case 0:
                    cell1.Highlight();
                    break;
                case 1:
                    cell2.Highlight();
                    break;
                case 2:
                    cell3.Highlight();
                    break;
            }
        }

        public void StopHighlight(int index)
        {
            switch (index)
            {
                case 0:
                    cell1.StopHighlight();
                    break;
                case 1:
                    cell2.StopHighlight();
                    break;
                case 2:
                    cell3.StopHighlight();
                    break;
            }
        }

        public void Locked(int index)
        {
            switch (index)
            {
                case 0:
                    cell1.Locked();
                    break;
                case 1:
                    cell2.Locked();
                    break;
                case 2:
                    cell3.Locked();
                    break;
            }
        }

        public void SetPopUpTracker(int index)
        {
            switch (index)
            {
                case 0:
                    cell1.SetPopUpTracker();
                    break;
                case 1:
                    cell2.SetPopUpTracker();
                    break;
                case 2:
                    cell3.SetPopUpTracker();
                    break;
            }
            popUpTracker?.biomeCellIndex = index;
        }

        public Dictionary<string, HashSet<string>> GetBiomeData(int index)
        {
            switch (index)
            {
                case 0:
                    return cell1.data;
                case 1:
                    return cell2.data;
                case 2:
                    return cell3.data;
            }
            return [];
        }

        public string GetBiomeId(int index)
        {
            switch (index)
            {
                case 0:
                    return cell1.biomeId;
                case 1:
                    return cell2.biomeId;
                case 2:
                    return cell3.biomeId;
            }
            return "";
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
            switch (index)
            {
                case 0:
                    cell1.SetIcons(lines);
                    break;
                case 1:
                    cell2.SetIcons(lines);
                    break;
                case 2:
                    cell3.SetIcons(lines);
                    break;
            }
        }
    }
}