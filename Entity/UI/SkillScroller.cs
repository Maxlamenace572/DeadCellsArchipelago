using dc.h2d;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.RoomManager;
using static DeadCellsArchipelago.TrackerData;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class SkillScroller<T> where T : Line
    {
        public dc.h2d.Object parent;
        public double posX;
        public double posY;
        public Flow? flow;
        public Mask? mask;
        public List<T> lines;
        public int tempHeight;
        public int tempWidth;
        public double lastMousePosY;
        public double lastMousePosX;
        public int lastHighlight = -1;
        public int lastHighlightCell = -1;
        public bool empty = true;
        public int maskHeight;
        public bool interactiveLines;


        public SkillScroller(double x, double y, dc.h2d.Object parent, int maskHeight, bool interactiveLines)
        {
            posX = x;
            posY = y;
            this.parent = parent;
            this.interactiveLines = interactiveLines;
            lines = new List<T>();
            this.maskHeight = maskHeight;
        }

        public void Refresh(int verticalSpacing)
        {
            if(flow == null) {
                mask = new Mask(0, maskHeight, parent)
                {
                    x = posX,
                    y = posY
                };
                flow = new Flow(mask)
                {
                    y = 0
                };
                flow.set_isVertical(true);
                flow.set_multiline(true);
                flow.set_verticalSpacing(verticalSpacing);
                tempHeight = verticalSpacing;
                tempWidth = 50;
                flow.set_overflow(true);
                flow.set_enableInteractive(true);

                flow.interactive.onWheel = (e) => {
                    double res = flow.y;
                    int scrollMultiplier = 100;
                    if (flow.get_outerHeight() > maskHeight)
                    {
                        if (e.wheelDelta > 0)
                        {
                            res = Math.Max(flow.y - e.wheelDelta * scrollMultiplier, -(flow.get_outerHeight()-maskHeight));
                        }
                        else
                        {
                            res = Math.Min(flow.y - e.wheelDelta * scrollMultiplier, 0);
                        }
                    }

                    if(interactiveLines)
                    {
                        lastMousePosY += flow.y - res;
                        UpdateHighlight(false);
                    }

                    flow.y = res;
                    flow.posChanged = true;

                };
                flow.interactive.onMove = (e) => {
                    if(interactiveLines)
                    {
                        lastMousePosY = e.relY;
                        lastMousePosX = e.relX;
                        UpdateHighlight(false);
                    }
                };
                flow.interactive.onOut = (e) =>
                {
                    if(interactiveLines)
                    {
                        UpdateHighlight(true);
                    }
                };
                flow.interactive.onClick = (e) =>
                {
                    if (lastHighlight != -1 && interactiveLines)
                    {
                        if (typeof(T) == typeof(ItemLine))
                        {
                            ((ItemLine)(Line) lines[lastHighlight]).GiveItem();
                        }
                        else if (lastHighlightCell != -1 && typeof(T) == typeof(BiomeLine))
                        {
                            popUpTracker?.biomeLineIndex = lastHighlight;
                            popUpTracker?.biomeCellIndex = lastHighlightCell;
                            ((BiomeLine)(Line) lines[lastHighlight]).SetPopUpTracker(lastHighlightCell);
                        }
                    }
                };
            }
        }

        public void SetContentItemLine(List<string> newList, int color)
        {
            if (flow == null || mask == null) return;
            if (typeof(T) == typeof(ItemLine))
            {
                int index = 0;
                foreach (string id in newList) {
                    lines.Add((T)(Line) new ItemLine(0, 0, id, null, color));
                    lines[index].AddParent(flow);
                    if(mask.width < lines[index].bgBox.wid)
                    {
                        mask.width = lines[index].bgBox.wid;
                    }
                    index ++;
                }
                if (tempHeight <  99) tempHeight += 100 -1;
            }
            mask.updateMask();
        }

        public void SetContentItemLine(Dictionary<string, int> rest, int color)
        {
            if (flow == null || mask == null) return;
            if (typeof(T) == typeof(ItemLine))
            {
                int index = 0;
                foreach (KeyValuePair<string, int> id in rest) {
                    lines.Add((T)(Line) new ItemLine(0, 0, id.Key, id.Value, color));
                    lines[index].AddParent(flow);
                    if(mask.width < lines[index].bgBox.wid)
                    {
                        mask.width = lines[index].bgBox.wid;
                    }
                    index ++;
                }
                tempHeight += 100 -1;
            }
            mask.updateMask();
        }

        public void SetContentBiomeLine()
        {
            if (flow == null || mask == null) return;
            if (typeof(T) == typeof(BiomeLine))
            {
                List<string> allBiomesIds = GetBiomesId();
                int index = 0;
                Dictionary<string, HashSet<string>> data = StartCalculate();
                for(int i = 0; i < allBiomesIds.Count; i+=3) {
                    lines.Add((T)(Line) new BiomeLine(0, 0, allBiomesIds[i], allBiomesIds[i+1], allBiomesIds[i+2], data));
                    lines[index].AddParent(flow);

                    for(int u = 0; u < 3; u++) {
                        if (!CanTakeExit(allBiomesIds[i+u]))
                        {
                            ((BiomeLine)(Line)lines[index]).Locked(u);
                        }
                    }

                    if(mask.width < ((BiomeLine)(Line) lines[index]).flow.get_outerWidth())
                    {
                        mask.width = ((BiomeLine)(Line) lines[index]).flow.get_outerWidth();
                    }
                    index ++;
                }
                tempHeight += 180;
                tempWidth += 320;
            }
            mask.updateMask();
        }

        public void SetContentLogLine(List<string> logs, int color)
        {
            if (flow == null || mask == null) return;
            if (typeof(T) == typeof(LogLine))
            {
                int index = 0;
                foreach (string log in logs) {
                    lines.Add((T)(Line) new LogLine(0, 0, log, color));
                    lines[index].AddParent(flow);
                    if(mask.width < lines[index].bgBox.wid)
                    {
                        mask.width = lines[index].bgBox.wid;
                    }
                    index ++;
                }
                tempHeight += 50 -2;
            }
            mask.updateMask();
        }

        public void UpdateHighlight(bool onOut)
        {
            if (typeof(T) == typeof(ItemLine))
            {
                if (!onOut)
                {
                    if (lastHighlight != -1)
                    {
                        ((ItemLine)(Line) lines[lastHighlight]).StopHighlight();
                    }
                    if (((int) lastMousePosY / tempHeight) >= 0 && ((int) lastMousePosY / tempHeight) < lines.Count)
                    {
                        ((ItemLine)(Line) lines[(int) lastMousePosY / tempHeight]).Highlight();
                        lastHighlight = (int) lastMousePosY / tempHeight;
                    }
                }
                else
                {
                    if (lastHighlight != -1)
                    {
                        ((ItemLine)(Line) lines[lastHighlight]).StopHighlight();
                        lastHighlight = -1;
                    }
                }
            }
            else if (typeof(T) == typeof(BiomeLine))
            {
                if (!onOut)
                {
                    if(lastHighlight != -1)
                    {
                        ((BiomeLine)(Line) lines[lastHighlight]).StopHighlight(lastHighlightCell);
                    }
                    ((BiomeLine)(Line) lines[(int) lastMousePosY / tempHeight]).Highlight((int) lastMousePosX / tempWidth);
                    lastHighlight = (int) lastMousePosY / tempHeight;
                    lastHighlightCell = (int) lastMousePosX / tempWidth;
                }
                else
                {
                    if (lastHighlight != -1)
                    {
                        ((BiomeLine)(Line) lines[lastHighlight]).StopHighlight(lastHighlightCell);
                        lastHighlight = -1;
                        lastHighlightCell = -1;
                    }
                }
            }
        }

        public void SetVisible(bool visible)
        {
            mask?.visible = visible;
        }

        public void RemoveAllContent()
        {
            if (flow == null) return;
            foreach (Line line in lines)
            {
                line.bgBox.remove();
            }
            lines = new List<T>();
        }

        public List<string> GetBiomesId()
        {
            return [
                "Other", "PrisonStart", "PrisonCourtyard", "SewerShort", "PurpleGarden", "Greenhouse",
                "PrisonDepths", "PrisonCorrupt", "PrisonRoof", "Ossuary", "SewerDepths", "DookuCastle",
                "Swamp", "Bridge", "BeholderPit", "DeathArena", "SwampHeart", "StiltVillage",
                "AncientTemple", "Tumulus", "Cemetery", "ClockTower", "Crypt", "Cliff",
                "Cavern", "TopClockTower", "GardenerStage", "Giant", "Castle", "DookuCastleHard",
                "Shipwreck", "Distillery", "Throne", "DookuArena", "Lighthouse", "QueenArena",
                "Astrolab", "Observatory", "Bank"
            ];
        }

        public void SetScrollAtEnd()
        {
            flow?.y = -(flow.get_outerHeight()-maskHeight);
            flow?.posChanged = true;
        }

        public void SetScrollAtStart()
        {
            flow?.y = 0;
            flow?.posChanged = true;
        }

        public void SetScrollDownAtIndex()
        {
            if (flow == null) return;
            if (flow.y + lastHighlight * tempHeight + (tempHeight - flow.verticalSpacing) > maskHeight)
            {
                flow.y = -(lastHighlight * tempHeight) + (maskHeight - (tempHeight - flow.verticalSpacing));
                flow.posChanged = true;
            }
        }

        public void SetScrollUpAtIndex()
        {
            if (flow == null) return;
            if (flow.y + lastHighlight * tempHeight < 0)
            {
                flow.y = -(lastHighlight * tempHeight);
                flow.posChanged = true;
            }
        }
    }
}