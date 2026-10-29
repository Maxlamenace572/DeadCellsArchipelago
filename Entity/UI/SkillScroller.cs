using dc.h2d;
using Serilog;

using static DeadCellsArchipelago.RoomManager;
using static DeadCellsArchipelago.TrackerData;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class SkillScroller<T> : FocusList where T : Line
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
        public int maskHeight;
        public bool interactiveLines;
        bool cursorHighLight;

        public SkillScroller(double x, double y, dc.h2d.Object parent, int maskHeight, bool interactiveLines, bool vert, bool hori)
        {
            posX = x;
            posY = y;
            this.parent = parent;
            this.interactiveLines = interactiveLines;
            lines = new List<T>();
            this.maskHeight = maskHeight;
            IsVertical = vert;
            IsHorizontal = hori;
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

                    lastMousePosY += flow.y - res;
                    UpdateCursorFocusScroller();

                    flow.y = res;
                    flow.posChanged = true;

                };
                flow.interactive.onMove = (e) => {
                    lastMousePosY = e.relY;
                    lastMousePosX = e.relX;
                    UpdateCursorFocusScroller();
                };
                flow.interactive.onClick = (e) =>
                {
                    Act();
                };
            }
        }

        public void UpdateCursorFocusScroller()
        {
            cursorHighLight = true;
            if (typeof(T) == typeof(ItemLine) || typeof(T) == typeof(LogLine))
            {
                previousIndex[1] = currentIndex[1];
                currentIndex[1] = (int) lastMousePosY / tempHeight;
                focusManager!.ChangeFocusCursor(this);
            }
            else if (typeof(T) == typeof(BiomeLine))
            {
                previousIndex = (int[]) currentIndex.Clone();
                currentIndex[0] = (int) lastMousePosX / tempWidth;
                currentIndex[1] = (int) lastMousePosY / tempHeight;
                focusManager!.ChangeFocusCursor(this);
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
                    if(mask.width < lines[index].w)
                    {
                        mask.width = (int) lines[index].w;
                    }
                    index ++;
                }
                listSizes = [0, lines.Count];
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
                    if(mask.width < lines[index].w)
                    {
                        mask.width = (int) lines[index].w;
                    }
                    index ++;
                }
                listSizes = [0, lines.Count];
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
                Dictionary<string, Biome> biomes = CalculateRegionData();
                Dictionary<string, HashSet<string>> data = StartCalculate(biomes);
                for(int i = 0; i < allBiomesIds.Count; i+=3) {
                    lines.Add((T)(Line) new BiomeLine(0, 0, allBiomesIds[i], allBiomesIds[i+1], allBiomesIds[i+2], data));
                    lines[index].AddParent(flow);

                    for(int u = 0; u < 3; u++) {
                        if (!CanTakeExit(allBiomesIds[i+u]))
                        {
                            ((BiomeLine)(Line)lines[index]).Locked(u);
                        }
                        if (allBiomesIds[i + u] != "Other" && !biomes[allBiomesIds[i + u]].accessible)
                        {
                            ((BiomeLine)(Line)lines[index]).SetIcons(u, biomes[allBiomesIds[i + u]].RemainingRequirements);
                        }
                    }

                    if(mask.width < ((BiomeLine)(Line) lines[index]).flow.get_outerWidth())
                    {
                        mask.width = ((BiomeLine)(Line) lines[index]).flow.get_outerWidth();
                    }
                    index ++;
                }
                listSizes = [3, lines.Count];
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
                    if(mask.width < lines[index].w)
                    {
                        mask.width = (int) lines[index].w;
                    }
                    index ++;
                }
                listSizes = [0, lines.Count];
                resetIndex = [0, lines.Count-1];
                currentIndex = (int[]) resetIndex.Clone();
                tempHeight += 50 -2;
            }
            mask.updateMask();
        }

        public override void Highlight()
        {
            if (typeof(T) == typeof(ItemLine))
            {
                ((ItemLine)(Line) lines[currentIndex[1]]).Highlight();
            }
            else if (typeof(T) == typeof(LogLine))
            {
                ((LogLine)(Line) lines[currentIndex[1]]).Highlight();
            }
            else if (typeof(T) == typeof(BiomeLine))
            {
                ((BiomeLine)(Line) lines[currentIndex[1]]).Highlight(currentIndex[0]);
            }

            if (previousIndex[1] < currentIndex[1])
                SetScrollDownAtIndex();
            else if (previousIndex[1] > currentIndex[1])
                SetScrollUpAtIndex();
            cursorHighLight = false;
        }

        public override void StopHighlight()
        {
            if (typeof(T) == typeof(ItemLine) && previousIndex[1] < lines.Count)
            {
                ((ItemLine)(Line) lines[previousIndex[1]]).StopHighlight();
            }
            else if (typeof(T) == typeof(LogLine))
            {
                ((LogLine)(Line) lines[previousIndex[1]]).StopHighlight();
            }
            else if (typeof(T) == typeof(BiomeLine))
            {
                ((BiomeLine)(Line) lines[previousIndex[1]]).StopHighlight(previousIndex[0]);
            }
        }

        public override void Act()
        {
            if (interactiveLines)
            {
                if (typeof(T) == typeof(ItemLine))
                {
                    ItemLine iL = (ItemLine)(Line) lines[currentIndex[1]];
                    if (iL.nb != null)
                        iL.GiveItem();
                    else
                        iL.ShowItemDescription();
                }
                else if (typeof(T) == typeof(BiomeLine))
                {
                    popUpTracker?.biomeLineIndex = currentIndex[1];
                    popUpTracker?.biomeCellIndex = currentIndex[0];
                    ((BiomeLine)(Line) lines[currentIndex[1]]).SetPopUpTracker(currentIndex[0]);
                    focusManager!.popUp = 1;
                    previousIndex = (int[]) currentIndex.Clone();
                    focusManager!.ChangePopUpFocus(popUpTracker!.topLine!);
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
            listSizes = [0, 0];
            currentIndex = [0, 0];
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
            if (flow.y + currentIndex[1] * tempHeight + (tempHeight - flow.verticalSpacing) > maskHeight)
            {
                double temp = flow.y;
                flow.y = -(currentIndex[1] * tempHeight) + (maskHeight - (tempHeight - flow.verticalSpacing));
                if (!cursorHighLight) lastMousePosY += temp - flow.y;
                flow.posChanged = true;
            }
        }

        public void SetScrollUpAtIndex()
        {
            if (flow == null) return;
            if (flow.y + currentIndex[1] * tempHeight < 0)
            {
                double temp = flow.y;
                flow.y = -(currentIndex[1] * tempHeight);
                if (!cursorHighLight) lastMousePosY += temp - flow.y;
                flow.posChanged = true;
            }
        }
    }
}