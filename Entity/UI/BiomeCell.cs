using dc;
using dc.h2d;
using dc.h2d.col;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ImageManager;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class BiomeCell
    {
        public Bitmap bitmap;
        public dc.ui.Text text;
        public Bitmap highlight;
        public Bitmap fade;
        public Bitmap bLock;
        public string biomeId;
        public Dictionary<string, HashSet<string>> data;

        public BiomeCell(double x, double y, dc.h2d.Object? parent, string biomeId, Dictionary<string, HashSet<string>> data)
        {
            this.biomeId = biomeId;
            this.data = data;

            if (biomeId == "Other")
            {
                Tile levelTile = Assets.Class.levelLogos.getLevelLogo("Lighthouse".AsHaxeString());
                bitmap = new Bitmap(levelTile, parent)
                {
                    x = x,
                    y = y
                };
                int f = 0;
                double xy = 0;
                Tile hideTile = Assets.Class.ui.getTile("walterWhite".AsHaxeString(), new Ref<int>(ref f), new Ref<double>(ref xy), new Ref<double>(ref xy), null);
                new Bitmap(hideTile, bitmap)
                {
                    scaleX = 320,
                    scaleY = 180,
                    color = ColorVectorRGBA(10, 19, 33, 1)
                };
                
                Tile logoTile = Assets.Class.ui.getTile("logoDeadCellsSmall".AsHaxeString(), new Ref<int>(ref f), new Ref<double>(ref xy), new Ref<double>(ref xy), null);
                var bLogo = new Bitmap(logoTile, bitmap)
                {
                    color = ColorVectorRGBA(255, 255, 255, 5)
                };
                Bounds boundsB = bitmap.getSize(new Bounds());
                Bounds boundsLogo = bLogo.getSize(new Bounds());
                bLogo.x = boundsB.xMax - boundsLogo.xMax;
                bLogo.y = boundsB.yMax - boundsLogo.yMax;
            }
            else
            {
                Tile levelTile = Assets.Class.levelLogos.getLevelLogo(biomeId.AsHaxeString());
                bitmap = new Bitmap(levelTile, parent)
                {
                    x = x,
                    y = y
                };
            }


            Bounds boundsLevel = bitmap.getSize(new Bounds());

            double scaleText = 1;
            text = new dc.ui.Text(bitmap, true, false, new Ref<double>(ref scaleText), null, null)
            {
                scaleX = 1,
                scaleY = 1
            };

            string keyT;
            string keyR;

            if (biomeId == "Other")
            {
                keyT = $"AllT";
                keyR = $"AllR";
            }
            else
            {
                keyT = $"T{biomeId}T";
                keyR = $"R{biomeId}T";
            }

            text.set_text($"{data[keyT].Count-data[keyR].Count}/{data[keyT].Count} ".AsHaxeString());
            if(data[keyR].Count == 0) text.set_textColor(16776960);
            text.x = boundsLevel.xMax - text.get_textWidth() -10;
            text.y = 10;
            int frame = 0;
            double XY = 0;
            Tile fadeTile = Assets.Class.ui.getTile("walterWhite".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
            fade = new Bitmap(fadeTile, bitmap)
            {
                visible = false,
                scaleX = 320,
                scaleY = 180,
                color = ColorVectorRGBA(0, 0, 0, 0.75)
            };
            

            Tile lockTile = Assets.Class.ui.getTile("locked".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
            bLock = new Bitmap(lockTile, bitmap)
            {
                visible = false,
                scaleX = 2,
                scaleY = 2
            };
            Bounds boundsLock = bLock.getSize(new Bounds());
            bLock.x = (boundsLevel.xMax - boundsLock.xMax)/2;
            bLock.y = (boundsLevel.yMax - boundsLock.yMax)/2;
            bLock.posChanged = true;
            
            
            Tile highlightTile = Assets.Class.ui.getTile("worldMapFrameDefault".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);
            highlight = new Bitmap(highlightTile, bitmap)
            {
                x = -76,
                y = -31,
                visible = false,
                scaleX = 3.81,
                scaleY = 3.6
            };

            
        }

        public void Highlight()
        {
            highlight.visible = true;
        }

        public void StopHighlight()
        {
            highlight.visible = false;
        }

        public void Locked()
        {
            if (biomeId != "Other")
            {
                fade.visible = true;
                bLock.visible = true;
            }
        }

        public void SetPopUpTracker()
        {
            if(popUpTracker == null) return;
            showPopUp = true;
            
            UpdateTopPopUp();

            popUpTracker.scrollerItems?.RemoveAllContent();
            popUpTracker.scrollerItems?.flow?.y = 0;
            popUpTracker.scrollerItems?.flow?.posChanged = true;
        }
    }
}