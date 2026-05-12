using dc.h2d;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public class SkillScroller<T> where T : Line
    {
        public dc.h2d.Object parent;
        public double posX;
        public double posY;
        public Flow? flow;
        public Mask? mask;
        public List<T> lines;
        public int tempHeight = 109;
        public double lastMousePosY;
        public int lastHighlight = -1;
        public bool empty = true;
        public int maskHeight;


        public SkillScroller(double x, double y, dc.h2d.Object parent, int maskHeight)
        {
            posX = x;
            posY = y;
            this.parent = parent;
            lines = new List<T>();
            this.maskHeight = maskHeight;
        }

        public void Refresh()
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
                flow.set_verticalSpacing(10);
                flow.set_overflow(true);
                flow.set_enableInteractive(true);

                flow.interactive.onWheel = (e) => {
                    double res = flow.y;
                    int scrollMultiplier = 60;
                    if (e.wheelDelta > 0)
                    {
                        res = Math.Max(flow.y - e.wheelDelta * scrollMultiplier, -(flow.get_outerHeight()-400));
                    }
                    else
                    {
                        res = Math.Min(flow.y - e.wheelDelta * scrollMultiplier, 0);
                    }
                    lastMousePosY += flow.y - res;
                    UpdateHighlight(false);

                    flow.y = res;
                    flow.posChanged = true;

                };
                flow.interactive.onMove = (e) => {
                    lastMousePosY = e.relY;
                    UpdateHighlight(false);
                };
                flow.interactive.onOut = (e) =>
                {
                    UpdateHighlight(true);
                };
                flow.interactive.onClick = (e) =>
                {
                    if (lastHighlight != -1)
                    {
                        if (typeof(T) == typeof(ItemLine))
                        {
                            DropItemToPlayer(((ItemLine)(Line) lines[lastHighlight]).itemId);
                        }
                    }
                };
            }
        }

        public void SetContentItemLine(List<string> newList)
        {
            if (flow == null || mask == null) return;
            if (typeof(T) == typeof(ItemLine))
            {
                int index = 0;
                foreach (string id in newList) {
                    lines.Add((T)(Line) new ItemLine(0, 0, id));
                    lines[index].AddParent(flow);
                    if(mask.width < lines[index].bgBox.wid)
                    {
                        mask.width = lines[index].bgBox.wid;
                    }
                    index ++;
                }
            }
            mask.updateMask();
        }

        public void UpdateHighlight(bool onOut)
        {
            if (typeof(T) == typeof(ItemLine))
            {
                if (!onOut)
                {
                    if(lastHighlight != -1)
                    {
                        ((ItemLine)(Line) lines[lastHighlight]).StopHighlight();
                    }
                    ((ItemLine)(Line) lines[(int) lastMousePosY / tempHeight]).Highlight();
                    lastHighlight = (int) lastMousePosY / tempHeight;
                }
                else
                {
                    ((ItemLine)(Line) lines[lastHighlight]).StopHighlight();
                    lastHighlight = -1;
                }
            }
        }

        public void SetVisible(bool visible)
        {
            mask?.visible = visible;
        }
    }
}