using dc;
using dc.h2d;
using dc.h2d.col;
using dc.ui;
using dc.ui.hud;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using Serilog;

namespace DeadCellsArchipelago {
    public class ItemLine : Line
    {
        public Skill skill;
        public dc.ui.Text text;
        public string itemId;

        public ItemLine(double x, double y, string itemId)
            : base(700, 100, x, y)
        {
            bool ctrlShow = false;
            double scaleSkill = 1.0/3;
            skill = new Skill(0, bgBox, new Ref<bool>(ref ctrlShow), new Ref<bool>(ref ctrlShow))
            {
                x = 2,
                y = 1.5,
                scaleX = scaleSkill,
                scaleY = scaleSkill
            };
            skill.setItemIcon(itemId.AsHaxeString());
            skill.btn.visible = false;

            double scaleText = 1.0/3;
            text = new dc.ui.Text(null, true, false, new Ref<double>(ref scaleText), null, null);
            text.set_text($" {Data.Class.item.byId.get(itemId.AsHaxeString()).name}".AsHaxeString());
            this.itemId = itemId;
        }

        public override void AddParent(dc.h2d.Object parent)
        {
            base.AddParent(parent);
            bgBox.addChildAt(skill, bgBox.layerCount);
            bgBox.addChildAt(text, bgBox.layerCount-1);

            Bounds boundsSkill = skill.getSize(new Bounds());
            text.x = boundsSkill.xMax + skill.x;
            text.y = (boundsSkill.yMax - (text.get_textHeight()*text.scaleX))/2 +skill.y;
        }

        public void Highlight()
        {
            text.set_textColor(16776960);
        }

        public void StopHighlight()
        {
            text.set_textColor(16777215);
        }
    }
}