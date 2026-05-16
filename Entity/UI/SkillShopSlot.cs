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

        public void InitButton(DefaultPause self, double x, double y, Func<InventItem?> getItem, NewItemDesc desc)
        {
            int price = shopPrice;
            if (skill != null) return;

            bool ctrlShow = false;
            skill = new Skill(0, self.bg, new Ref<bool>(ref ctrlShow), new Ref<bool>(ref ctrlShow))
            {
                x = x,
                y = y
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
                    SetPrice(self, price);

                    Skill capturedSkill = skill;
                    Bounds boundsSkill = skill.getSize(new Bounds());
                    inter = new Interactive(boundsSkill.xMax, boundsSkill.yMax, skill, null)
                    {
                        onClick = (e) =>
                        {
                            if (HERO == null) return;
                            if (HasAffix(ii, "Colorless")) return;

                            if (HERO.cells >= price)
                            {
                                bool noStats = false;
                                HERO.substractCells(price, new Ref<bool>(ref noStats));
                                if (cellsNumber != null)
                                    cellsNumber.set_text($" {HERO.cells}".AsHaxeString());

                                ii.affixes.pushDyn("Colorless".AsHaxeString());
                                bool updateHUD = true;
                                bool durings = false;
                                HERO.onEquipedItemsChange(new Ref<bool>(ref updateHUD), new Ref<bool>(ref durings), new Ref<bool>(ref durings));
                                desc.setItem(ii);

                                capturedSkill.useItem(ii);
                                capturedSkill.btn.visible = false;
                                foreach (Bitmap ammoIcon in capturedSkill.ammoIcons)
                                    ammoIcon.visible = false;

                                SetNoPrice(self);
                                skill.removeChild(inter);
                            }
                            else
                            {
                                label?.set_textColor(16711680);
                            }
                        },
                        onMove = (e) =>
                        {
                            if (label != null && label.textColor != 16711680)
                                label.set_textColor(47103);
                        },
                        onOut = (e) =>
                        {
                            label?.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));
                        }
                    };
                }
                else
                {
                    SetNoPrice(self);
                }
            }
            else
            {
                SetNoPrice(self);
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

        internal void SetNoPrice(DefaultPause self)
        {
            if(skill == null) return;
            cellBitmap?.remove();
            label?.remove();

            Bounds boundsSkill = skill.getSize(new Bounds());
            double scale = 1;
            label = new dc.ui.Text(self.bg, false, false, new Ref<double>(ref scale), null, null)
            {
                y = boundsSkill.yMax + skill.y
            };
            label.set_text("-".AsHaxeString());
            label.x = ((boundsSkill.xMax - label.get_textWidth()) /2) + skill.x;
            label.set_textColor(16777215);
        }

        internal void SetPrice(DefaultPause self, int number)
        {
            if(skill == null) return;

            Bounds boundsSkill = skill.getSize(new Bounds());
            double scale = 1;
            label = new dc.ui.Text(self.bg, false, false, new Ref<double>(ref scale), null, null);
            label.set_text($" {number}".AsHaxeString());
            label.set_textColor(dc.ui.Text.Class.COLORS.get("CE".AsHaxeString()));


            int frame = 0;
            double XY = 0;
            var cellTile = Assets.Class.gameElements.getTile("cell".AsHaxeString(), new Ref<int>(ref frame), new Ref<double>(ref XY), new Ref<double>(ref XY), null);

            cellBitmap = new Bitmap(cellTile, self.bg)
            {
                y = boundsSkill.yMax + skill.y + 10,
                x = (boundsSkill.xMax -(22 + label.get_textWidth())) /2 + skill.x
            };
            
            Bounds boundsCell = cellBitmap.getSize(new Bounds());

            label.y = (boundsCell.yMax - label.get_textHeight()) /2 + cellBitmap.y;
            label.x = boundsCell.xMax + cellBitmap.x;
        }
    }
}