using dc;
using dc.h2d;
using dc.h2d.col;
using dc.ui;
using dc.ui.icon;
using Text = dc.ui.Text;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.MainMenuManager;

namespace DeadCellsArchipelago {
    public class PopUpItemDesc
    {
        public dc.h2d.Object parent;
        public UIBox bgBox;
        public UIBox outerBox;
        Flow? globalDescFlow;
        Flow? centerDescFlow;

        public PopUpItemDesc(dc.h2d.Object parent)
        {
            this.parent = parent;

            bgBox = new UIBox("boxMain".AsHaxeString(), 500*screenScale, 700*screenScale, 0, 0)
            {
                scaleX = 3,
                scaleY = 3,
                x = 50,
                posChanged = true
            };
            Bounds boundsBgBox = bgBox.getSize(new Bounds());
            bgBox.y = (1080 - boundsBgBox.yMax)/2;
            bgBox.colorizeSG((int) APColor.DeepBlue);

            outerBox = new UIBox("boxInfo".AsHaxeString(), 500*screenScale, 700*screenScale, 0, 0)
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
            globalDescFlow?.visible = visible;
            centerDescFlow?.visible = visible;
        }

        public void AddContentMenu(ItemData itD)
        {
            if (globalDescFlow != null)
            {
                globalDescFlow.remove();
            }

            if (centerDescFlow != null)
            {
                centerDescFlow.remove();
            }

            globalDescFlow = new Flow(parent)
            {
                x = bgBox.x + 10,
                y = bgBox.y + 5,
                posChanged = true
            };
            globalDescFlow.set_isVertical(true);
            globalDescFlow.set_multiline(true);
            globalDescFlow.set_verticalSpacing(30);

            centerDescFlow = new Flow(parent)
            {
                y = globalDescFlow.y
            };
            
            centerDescFlow.set_isVertical(true);
            centerDescFlow.set_multiline(true);
            centerDescFlow.set_verticalSpacing(30);
            centerDescFlow.set_horizontalAlign(new FlowAlign.Middle());

            Flow flow0 = new Flow(globalDescFlow);
            flow0.set_horizontalSpacing(4);
            flow0.set_verticalSpacing(4);
            flow0.set_verticalAlign(new FlowAlign.Middle());
            flow0.set_isVertical(true);
            
            Flow biomeFlow = new Flow(flow0);
            biomeFlow.set_verticalAlign(new FlowAlign.Middle());
            double scale = 3/textPixelScale;
            Text biomeText = new Text(biomeFlow, false, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            biomeText.set_text("Biomes: ".AsHaxeString());

            Flow centerFlow0 = new Flow(centerDescFlow);
            centerFlow0.set_horizontalSpacing(4);
            centerFlow0.set_verticalSpacing(4);
            centerFlow0.set_verticalAlign(new FlowAlign.Middle());
            centerFlow0.set_horizontalAlign(new FlowAlign.Middle());
            centerFlow0.set_isVertical(true);

            new Bitmap(Assets.Class.levelLogos.getLevelLogo("PrisonStart".AsHaxeString()), centerFlow0)
            {
                scaleX=0.2,
                scaleY=0.2,
                alpha=0
            };

            Flow lineBiomeFlow = new Flow(centerFlow0);

            int u = 0;
            foreach (string biome in itD.biomes)
            {
                if (u%7 == 0)
                {
                    lineBiomeFlow = new Flow(centerFlow0);
                    lineBiomeFlow.set_horizontalSpacing(4);
                    lineBiomeFlow.set_verticalAlign(new FlowAlign.Middle());
                }

                if (biome == "Challenge") continue;
                new Bitmap(Assets.Class.levelLogos.getLevelLogo(biome.AsHaxeString()), lineBiomeFlow)
                {
                    scaleX=0.2,
                    scaleY=0.2
                };
                u++;
            }

            new Bitmap(Assets.Class.levelLogos.getLevelLogo("PrisonStart".AsHaxeString()), biomeFlow)
            {
                scaleX=0.2,
                scaleY=0.2,
                alpha=0
            };
            for (int i=0; i <= (u-1)/7; i++)
            {
                new Bitmap(Assets.Class.levelLogos.getLevelLogo("PrisonStart".AsHaxeString()), flow0)
                {
                    scaleX=0.2,
                    scaleY=0.2,
                    alpha=0
                };
            }


            Flow flow1 = new Flow(globalDescFlow);
            flow1.set_horizontalSpacing(4);
            flow1.set_verticalAlign(new FlowAlign.Middle());

            Text minBsc = new Text(flow1, false, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = textBaseScale * scale,
                scaleY = textBaseScale * scale
            };
            minBsc.set_text("Min BSC: ".AsHaxeString());

            Flow centerFlow1 = new Flow(centerDescFlow);
            centerFlow1.set_horizontalSpacing(4);
            centerFlow1.set_verticalAlign(new FlowAlign.Middle());

            for (int i = 0; i < itD.min_bc; i++) Icon.Class.createItemIcon("BossRune1".AsHaxeString(), centerFlow1);
            if (itD.min_bc == 0)
            {
                Icon bri = Icon.Class.createItemIcon("BossRune1".AsHaxeString(), centerFlow1);
                bri.alpha=0;
            }


            Flow flow2 = new Flow(globalDescFlow);
            flow2.set_horizontalSpacing(4);
            flow2.set_verticalAlign(new FlowAlign.Middle());
            
            Icon icon = Icon.Class.createMobIcon("Zombie".AsHaxeString(), flow2);
            icon.scaleX=3;
            icon.scaleY=3;
            icon.alpha=0;

            Flow centerflow2 = new Flow(centerDescFlow);
            centerflow2.set_horizontalSpacing(4);
            centerflow2.set_verticalAlign(new FlowAlign.Middle());

            if (itD.mobs.Any())
            {
                foreach (string mob in itD.mobs)
                {
                    Icon mobIcon = Icon.Class.createMobIcon(mob.AsHaxeString(), centerflow2);
                    mobIcon.scaleX=3;
                    mobIcon.scaleY=3;
                }
            }

            if (itD.requirements.Any())
            {
                Flow flow3 = new Flow(globalDescFlow);
                flow3.set_isVertical(true);
                flow3.set_verticalSpacing(4);
                flow3.set_verticalAlign(new FlowAlign.Middle());

                Text req = new Text(flow3, false, false, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                req.set_text("Require:".AsHaxeString());
            
                foreach (List<string> items in itD.requirements)
                {
                    Flow lineReqFlow = new Flow(flow3);
                    lineReqFlow.set_horizontalSpacing(4);
                    lineReqFlow.set_verticalAlign(new FlowAlign.Middle());
                    foreach (string item in items)
                    {
                        if (item.Length >= 5 && item[..5] == "Boss_")
                        {
                            Icon mobIcon = Icon.Class.createMobIcon(item[5..].AsHaxeString(), lineReqFlow);
                            mobIcon.scaleX=0.5;
                            mobIcon.scaleY=0.5;
                        }
                        else if (item.Length >= 7 && item[^7..] == " Unlock")
                        {
                            new Bitmap(Assets.Class.levelLogos.getLevelLogo(item[..^7].AsHaxeString()), lineReqFlow)
                            {
                                scaleX=0.2,
                                scaleY=0.2
                            };
                        }
                        else
                        {
                            Icon.Class.createItemIcon(item.AsHaxeString(), lineReqFlow);
                        }
                    }
                }
            }


            if (itD.description != null)
            {
                Text desc = new Text(globalDescFlow, false, false, new Ref<double>(ref scale), null, null)
                {
                    scaleX = textBaseScale * scale,
                    scaleY = textBaseScale * scale
                };
                desc.set_text(itD.description.AsHaxeString());
                desc.set_maxWidth(480);
            }


            Bounds boundsF = centerDescFlow.getSize(new Bounds());
            centerDescFlow.x = bgBox.x + ((500 - boundsF.xMax) /2);
            centerDescFlow.posChanged = true;
        }
    }
}