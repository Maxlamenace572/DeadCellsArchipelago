using dc.h2d;
using dc.ui;
using Serilog;

using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class PopUpTopLine
    {
        public Flow flow;
        public List<PopUpTopCell> cells;

        public PopUpTopLine(double x, double y, dc.h2d.Object parent, int biomeLineIndex, int biomeCellIndex)
        {
            flow = new Flow(parent)
            {
                x = x
            };
            cells = new List<PopUpTopCell>();

            if (scrollerBiome == null) return;
            Dictionary<string, HashSet<string>> data = scrollerBiome.lines[biomeLineIndex].GetBiomeData(biomeCellIndex);
            string biomeId = scrollerBiome.lines[biomeLineIndex].GetBiomeId(biomeCellIndex);

            double totalCellsWidth = 0;
            if (biomeId != "Other")
            {
                List<string> start = ["T", "R"];
                for (int difficulty = 0; difficulty <= 5; difficulty++)
                {
                    int cellT = 0;
                    HashSet<string> cellR = [];
                    foreach (string kind in start)
                    {
                        string key = $"{kind}{biomeId}{difficulty}";
                        if (data.ContainsKey(key))
                        {
                            if (kind == "T")
                            {
                                cellT = data[key].Count;
                            }
                            else
                            {
                                cellR = data[key];
                            }
                        }
                    }
                    PopUpTopCell cell = new PopUpTopCell(flow, $"BSC {difficulty}", cellR, cellT);
                    totalCellsWidth += cell.interW;
                    cells.Add(cell);
                }
            }
            else
            {
                PopUpTopCell cell1 = new PopUpTopCell(flow, "ASP", data["RAspect"], data["TAspect"].Count);
                totalCellsWidth += cell1.interW;
                cells.Add(cell1);

                PopUpTopCell cell2 = new PopUpTopCell(flow, "Rift", data["RChallengeT"], data["TChallengeT"].Count);
                totalCellsWidth += cell2.interW;
                cells.Add(cell2);

                PopUpTopCell cell3 = new PopUpTopCell(flow, "All", data["AllR"], data["AllT"].Count);
                totalCellsWidth += cell3.interW;
                cells.Add(cell3);
            }

            flow.set_horizontalSpacing((int)((700 -totalCellsWidth) / (cells.Count-1)));

            flow.y = y;
            flow.posChanged = true;
        }

        public void SetVisible(bool visible)
        {
            flow.visible = visible;
        }

        public void Highlight(int index)
        {
            cells[index].Highlight();
        }

        public void StopHighlight(int index)
        {
            cells[index].StopHighlight();
        }
    }
}