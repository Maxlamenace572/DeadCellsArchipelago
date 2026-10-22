using dc.h2d;
using Serilog;

using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class PopUpTopLine : FocusList
    {
        public Flow flow;
        public List<PopUpTopCell> cells;
        public string biomeId = "Other";

        public PopUpTopLine(double x, double y, dc.h2d.Object parent, int biomeLineIndex, int biomeCellIndex)
        {
            IsHorizontal = true;

            flow = new Flow(parent)
            {
                x = x
            };
            cells = new List<PopUpTopCell>();

            if (scrollerBiome == null) return;
            Dictionary<string, HashSet<string>> data = scrollerBiome.lines[biomeLineIndex].GetBiomeData(biomeCellIndex);
            biomeId = scrollerBiome.lines[biomeLineIndex].GetBiomeId(biomeCellIndex);

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
                    PopUpTopCell cell = new PopUpTopCell(flow, $"BSC {difficulty}", cellR, cellT, cells.Count);
                    totalCellsWidth += cell.width;
                    cells.Add(cell);
                }
            }
            else
            {
                PopUpTopCell cell1 = new PopUpTopCell(flow, "ASP", data["RAspect"], data["TAspect"].Count, cells.Count);
                totalCellsWidth += cell1.width;
                cells.Add(cell1);

                PopUpTopCell cell2 = new PopUpTopCell(flow, "Rift", data["RChallengeT"], data["TChallengeT"].Count, cells.Count);
                totalCellsWidth += cell2.width;
                cells.Add(cell2);

                PopUpTopCell cell3 = new PopUpTopCell(flow, "All", data["AllR"], data["AllT"].Count, cells.Count);
                totalCellsWidth += cell3.width;
                cells.Add(cell3);
            }

            listSizes[0] = cells.Count;

            flow.set_horizontalSpacing((int)((700 -totalCellsWidth) / (cells.Count-1)));

            flow.y = y;
            flow.posChanged = true;
        }

        public void SetVisible(bool visible)
        {
            flow.visible = visible;
        }

        public override void Highlight()
        {
            cells[currentIndex[0]].Highlight();
        }

        public override void StopHighlight()
        {
            cells[previousIndex[0]].StopHighlight();
        }

        public override void Act()
        {
            cells[currentIndex[0]].Act();
        }
    }
}