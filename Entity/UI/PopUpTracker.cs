using dc.h2d.col;
using dc.ui;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.MainMenuManager;
using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.PauseMenuManager;
using static DeadCellsArchipelago.WorldMapManager;
using static DeadCellsArchipelago.Translator;

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
        public TextButton? popUpWarpButton = null;
        public TextButton? cancelWarpButton = null;
        public TextField researchBar;
        public bool showButton;
        HashSet<string> itemIds = [];

        public PopUpTracker(dc.h2d.Object parent)
        {
            this.parent = parent;

            bgBox = new UIBox("boxMain".AsHaxeString(), 720*screenScale, 660*screenScale, 0, 0)
            {
                scaleX = 3,
                scaleY = 3
            };
            Bounds boundsBgBox = bgBox.getSize(new Bounds());
            bgBox.x =  (1920 - boundsBgBox.xMax)/2;
            bgBox.y =  (1080 - boundsBgBox.yMax)/2;
            bgBox.posChanged = true;
            bgBox.colorizeSG((int) APColor.DeepBlue);

            outerBox = new UIBox("boxInfo".AsHaxeString(), 720*screenScale, 660*screenScale, 0, 0)
            {
                x = bgBox.x,
                y = bgBox.y,
                scaleX = 3,
                scaleY = 3
            };
            
            parent.addChild(bgBox);
            parent.addChild(outerBox);

            researchBar = new TextField(parent, 0, bgBox.y + 100, true, false, "", (int)APColor.Blue, 650)
            {
                textChanged = () =>
                {
                    ResearchScrollContent(researchBar!.GetFieldValue());
                }
            };

            popUpWarpButton = new TextButton(parent, bgBox.x, bgBox.y-70, false, false, "Warp", true);
            cancelWarpButton = new TextButton(parent, popUpWarpButton.x+popUpWarpButton.GetWidth()+10, popUpWarpButton.y, false, false, "Cancel", false)
            {
                act = () => {warpToBiome = null;}
            };
            cancelWarpButton.SetColors((int) APColor.Red, (int) APColor.LightRed, null);
        }

        public void SetVisible(bool visible)
        {
            bgBox.visible = visible;
            outerBox.visible = visible;
            scrollerItems?.SetVisible(visible);
            topLine?.SetVisible(visible);
            researchBar.SetVisible(visible);
            popUpWarpButton?.SetVisible(visible && showButton);
            cancelWarpButton?.SetVisible(visible && showButton && warpToBiome != null);
            if (!visible) ResetResearch();
        }

        public void AddFillerMenu()
        {
            scrollerItems = new SkillScroller<ItemLine>(bgBox.x+10, bgBox.y+150, parent, 500, true);
            scrollerItems.Refresh(10);

            topLine = new PopUpTopLine(bgBox.x+10, bgBox.y+5, parent, biomeLineIndex, biomeCellIndex);
            scrollerItems.SetVisible(true);
        }

        public void UpdateTopContent()
        {
            topLine?.flow.remove();
            topLine = new PopUpTopLine(bgBox.x+10, bgBox.y+5, parent, biomeLineIndex, biomeCellIndex);
        }

        public void UpdateWarpButton()
        {
            if (topLine!.biomeId == SAVED_DATA!.currentLevelId && topLine!.biomeId != "PrisonStart")
            {
                showButton = true;
                popUpWarpButton!.ChangeText("Reload");
                cancelWarpButton!.ChangePos(popUpWarpButton.x+popUpWarpButton.GetWidth()+10, null);
                popUpWarpButton!.act = () => {
                    warpToBiome = topLine!.biomeId;
                    isReload = true;
                };
                popUpWarpButton!.SetEnabled(true);
            }
            else if (new[] {"Other", "Bank", "PrisonStart"}.Any(topLine!.biomeId.Contains)) showButton = false;
            else if ((SAVED_DATA!.IsCheckSent($"{topLine!.biomeId} Enter") && IsLevelAfterCurrent(topLine!.biomeId)) || GLOBAL_DATA!.debugWarp)
            {
                showButton = true;
                popUpWarpButton!.ChangeText("Warp");
                cancelWarpButton!.ChangePos(popUpWarpButton.x+popUpWarpButton.GetWidth()+10, null);
                popUpWarpButton!.act = () => {warpToBiome = topLine!.biomeId;};
                popUpWarpButton!.SetEnabled(true);
            }
            else 
            {
                showButton = true;
                popUpWarpButton!.ChangeText("Warp");
                cancelWarpButton!.ChangePos(popUpWarpButton.x+popUpWarpButton.GetWidth()+10, null);
                popUpWarpButton!.SetEnabled(false);
            }
        }

        public void UpdateScrollContent(HashSet<string> itemIds)
        {
            if(scrollerItems == null) return;
            this.itemIds = itemIds;
            scrollerItems.RemoveAllContent();
            scrollerItems.SetContentItemLine(itemIds.ToList(), (int) APColor.Blue);
            scrollerItems.flow?.y = 0;
            scrollerItems.flow?.posChanged = true;

            if (researchBar.GetFieldValue() != "") ResearchScrollContent(researchBar.GetFieldValue());
        }

        public void ResearchScrollContent(string research)
        {
            if(scrollerItems == null) return;
            
            HashSet<string> matchingIds = [];
            if (research == "")
            {
                matchingIds = itemIds;
            }
            else
            {
                foreach (string itemId in itemIds)
                {
                    string itemName = itemId;
                    if (IdToNameKeyExist(itemName))
                    {
                        itemName = GetName(itemName);
                    }

                    if (itemName.ToUpper().Contains(research.ToUpper()))
                    {
                        matchingIds.Add(itemId);
                    }
                }
            }
            scrollerItems.RemoveAllContent();
            scrollerItems.SetContentItemLine(matchingIds.ToList(), (int) APColor.Blue);
            scrollerItems.flow?.y = 0;
            scrollerItems.flow?.posChanged = true;
        }

        public void ResetResearch()
        {
            researchBar.SetFieldValue("");
            itemIds = [];
        }
    }
}