using dc.h2d.col;
using dc.ui;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class PopUpTracker
    {
        public dc.h2d.Object parent;
        public UIBox bgBox;
        public UIBox outerBox;
        public SkillScroller<ItemLine>? scrollerItems;
        public PopUpTopLine? topLine;
        public int biomeLineIndex;
        public int biomeCellIndex;

        public PopUpTracker(dc.h2d.Object parent)
        {
            this.parent = parent;

            bgBox = new UIBox("boxMain".AsHaxeString(), 720*screenScale, 610*screenScale, 0, 0)
            {
                scaleX = 3,
                scaleY = 3
            };
            Bounds boundsBgBox = bgBox.getSize(new Bounds());
            bgBox.x =  (1920 - boundsBgBox.xMax)/2;
            bgBox.y =  (1080 - boundsBgBox.yMax)/2;
            bgBox.posChanged = true;
            bgBox.colorizeSG(660257);

            outerBox = new UIBox("boxInfo".AsHaxeString(), 720*screenScale, 610*screenScale, 0, 0)
            {
                x = bgBox.x,
                y = bgBox.y,
                scaleX = 3,
                scaleY = 3
            };
            
            parent.addChild(bgBox);
            parent.addChild(outerBox);
        }

        public void SetVisible(bool visible)
        {
            bgBox.visible = visible;
            outerBox.visible = visible;
            scrollerItems?.SetVisible(visible);
            topLine?.SetVisible(visible);
        }

        public void AddFillerMenu()
        {
            scrollerItems = new SkillScroller<ItemLine>(bgBox.x+10, bgBox.y+100, parent, 500, false);
            scrollerItems.Refresh(10);

            topLine = new PopUpTopLine(bgBox.x+10, bgBox.y+5, parent, biomeLineIndex, biomeCellIndex);
            scrollerItems.SetVisible(true);
        }

        public void UpdateTopContent()
        {
            topLine?.flow.remove();
            topLine = new PopUpTopLine(bgBox.x+10, bgBox.y+5, parent, biomeLineIndex, biomeCellIndex);
        }

        public void UpdateScrollContent(HashSet<string> itemIds)
        {
            if(scrollerItems == null) return;
            scrollerItems.RemoveAllContent();
            scrollerItems.SetContentItemLine(itemIds.ToList(), 2237002);
            scrollerItems.flow?.y = 0;
            scrollerItems.flow?.posChanged = true;
        }
    }
}