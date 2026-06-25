using dc;
using dc.h2d;
using dc.h2d.col;
using dc.haxe;
using dc.tool;
using dc.ui;
using dc.ui.hud;
using dc.ui.pause;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class SkillShopSlot
    {
        public Skill? skill;
        public dc.ui.Text? label;
        public Bitmap? cellBitmap;
        public Interactive? inter;
        public InventItem? internII;
        public dc.h2d.Object? parent;
        public NewItemDesc? desc;

        public void InitButton(dc.h2d.Object parent, double x, double y, Func<InventItem?> getItem, NewItemDesc desc)
        {
            if (skill != null) return;
            this.parent = parent;
            this.desc = desc;

            bool ctrlShow = false;
            double scaleSkill = 1.0/screenScale;
            skill = new Skill(0, parent, new Ref<bool>(ref ctrlShow), new Ref<bool>(ref ctrlShow))
            {
                x = x,
                y = y,
                scaleX = scaleSkill,
                scaleY = scaleSkill
            };

            InventItem? ii = getItem();
            skill.btn.visible = false;

            if (ii != null)
            {
                skill.useItem(ii);
                skill.btn.visible = false;
                foreach (Bitmap ammoIcon in skill.ammoIcons)
                    ammoIcon.visible = false;

                if (!HasAffix(ii, "Colorless"))
                {
                    SetPrice(parent, shopPrice);

                    Skill capturedSkill = skill;
                    internII = ii;
                    Bounds boundsSkill = skill.getSize(new Bounds());
                    inter = new Interactive(boundsSkill.xMax*screenScale, boundsSkill.yMax*screenScale, skill, null)
                    {
                        onClick = (e) =>
                        {
                            BuyColorless();
                        },
                        onMove = (e) =>
                        {
                            Highlight();
                        },
                        onOut = (e) =>
                        {
                            StopHighlight();
                        }
                    };
                }
                else
                {
                    SetNoPrice(parent);
                }
            }
            else
            {
                SetNoPrice(parent);
            }
        }

        public static bool HasAffix(InventItem ii, string affixToCheck)
        {
            foreach(dc.String affix in ii.affixes)
            {
                if (affix.ToString() == affixToCheck)
                {
                    return true;
                }
            }
            return false;
        }

        public void SetVisible(bool visible)
        {
            skill?.visible = visible;
            label?.visible = visible;
            cellBitmap?.visible = visible;
        }

        public void Reset()
        {
            skill = null;
            label = null;
            cellBitmap = null;
        }

        internal void SetNoPrice(dc.h2d.Object parent)
        {
            if(skill == null) return;
            cellBitmap?.remove();
            label?.remove();

            Bounds boundsSkill = skill.getSize(new Bounds());
            double scale = 1;
            label = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null)
            {
                y = boundsSkill.yMax + skill.y,
                    scaleX = 1,
                    scaleY = 1
            };
            label.set_text("-".AsHaxeString());
            label.x = ((boundsSkill.xMax - label.get_textWidth()) /2) + skill.x;
            label.set_textColor(16777215);
        }

        internal void SetPrice(dc.h2d.Object parent, int number)
        {
            if(skill == null) return;

            Bounds boundsSkill = skill.getSize(new Bounds());
            double scale = 1;
            label = new dc.ui.Text(parent, false, false, new Ref<double>(ref scale), null, null)
            {
                scaleX = 1,
                scaleY = 1
            };
            label.set_text($" {number}".AsHaxeString());
            label.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));


            int frame = 0;
            double XY = 0;
            var cellTile = Assets.Class.gameElements.getTile("cell".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);

            cellBitmap = new Bitmap(cellTile, parent)
            {
                y = boundsSkill.yMax + skill.y + 10,
                x = (boundsSkill.xMax -(22 + label.get_textWidth())) /2 + skill.x
            };
            
            Bounds boundsCell = cellBitmap.getSize(new Bounds());

            label.y = (boundsCell.yMax - label.get_textHeight()) /2 + cellBitmap.y;
            label.x = boundsCell.xMax + cellBitmap.x;
        }

        public void Highlight()
        {
            if (label == null) return;
            if (label.text.ToString() == "-") label.set_textColor(16776960);
            else if (label.textColor != 16711680) label.set_textColor(47103);
        }

        public void StopHighlight()
        {
            if (label == null) return;
            if (label.text.ToString() == "-") label.set_textColor(16777215);
            else label?.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));
        }

        public void BuyColorless()
        {
            if (HERO == null || skill == null || internII == null || parent == null || desc == null) return;
            if (HasAffix(internII, "Colorless")) return;

            if (HERO.cells >= shopPrice)
            {
                bool noStats = false;
                HERO.substractCells(shopPrice, new Ref<bool>(ref noStats));
                if (cellsNumber != null)
                    cellsNumber.set_text($" {HERO.cells}".AsHaxeString());

                internII.affixes.pushDyn("Colorless".AsHaxeString());
                bool updateHUD = true;
                bool durings = false;
                HERO.onEquipedItemsChange(new Ref<bool>(ref updateHUD), new Ref<bool>(ref durings), new Ref<bool>(ref durings));
                desc.setItem(internII);

                skill.useItem(internII);
                skill.btn.visible = false;
                foreach (Bitmap ammoIcon in skill.ammoIcons)
                    ammoIcon.visible = false;

                SetNoPrice(parent);
                skill.removeChild(inter);
            }
            else
            {
                label?.set_textColor(16711680);
            }
        }
    }
}