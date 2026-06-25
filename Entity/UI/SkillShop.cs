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
    public class SkillShop
    {
        public double x;
        public double y;
        public SkillShopSlot buttonWeapon1 = new SkillShopSlot();
        public SkillShopSlot buttonWeapon2 = new SkillShopSlot();
        public SkillShopSlot buttonSkill1 = new SkillShopSlot();
        public SkillShopSlot buttonSkill2 = new SkillShopSlot();

        public SkillShop(double x, double y)
        {
            this.x = x;
            this.y = y;
        }

        public void AddIncolorWeapons(dc.h2d.Object parent, DefaultPause self, bool invert)
        {
            if(!invert)
            {
                buttonWeapon1.InitButton(parent, x, y, () => HERO?.inventory.getEquippedWeaponOn(0), self.weaLeft);
                buttonWeapon2.InitButton(parent, x+150, y, () => HERO?.inventory.getEquippedWeaponOn(1), self.weaRight);
            }
            else
            {
                buttonWeapon1.InitButton(parent, x, y, () => HERO?.inventory.getEquippedWeaponOn(1), self.weaLeft);
                buttonWeapon2.InitButton(parent, x+150, y, () => HERO?.inventory.getEquippedWeaponOn(0), self.weaRight);
            }
             
        }

        public void AddIncolorSkills(dc.h2d.Object parent, DefaultPause self, bool invert)
        {
            if(!invert)
            {
                buttonSkill1.InitButton(parent, x+150, y+150, () => HERO?.inventory.getActiveOn(0), self.skillRight);
                buttonSkill2.InitButton(parent, x, y+150, () => HERO?.inventory.getActiveOn(1), self.skillLeft);
            }
            else
            {
                buttonSkill1.InitButton(parent, x+150, y+150, () => HERO?.inventory.getActiveOn(1), self.skillRight);
                buttonSkill2.InitButton(parent, x, y+150, () => HERO?.inventory.getActiveOn(0), self.skillLeft);
            }
        }

        public void SwapWeaponsApMenu(Hook_Inventory.orig_swapWeapons orig, Inventory self)
        {
            buttonWeapon1.Reset();
            buttonWeapon2.Reset();
            if (defaultPause != null && screenBitmap != null) AddIncolorWeapons(screenBitmap, defaultPause, true);
            orig(self);
        }

        public void SwapSkillsApMenu(Hook_Inventory.orig_swapSkills orig, Inventory self)
        {
            buttonSkill1.Reset();
            buttonSkill2.Reset();
            if (defaultPause != null && screenBitmap != null) AddIncolorSkills(screenBitmap, defaultPause, true);
            orig(self);
        }

        public void Reset()
        {
            buttonWeapon1.Reset();
            buttonWeapon2.Reset();
            buttonSkill1.Reset();
            buttonSkill2.Reset();
        }

        public void SetVisible(bool visible)
        {
            buttonWeapon1.SetVisible(visible);
            buttonWeapon2.SetVisible(visible);
            buttonSkill1.SetVisible(visible);
            buttonSkill2.SetVisible(visible);
        }

        public void Highlight(int indexX, int indexY)
        {
            switch (indexX)
            {
                case 0:
                    if(indexY == 0) buttonWeapon1.Highlight();
                    if(indexY == 1) buttonSkill2.Highlight();
                    break;
                case 1:
                    if(indexY == 0) buttonWeapon2.Highlight();
                    if(indexY == 1) buttonSkill1.Highlight();
                    break;
            }
        }

        public void StopHighlight(int indexX, int indexY)
        {
            switch (indexX)
            {
                case 0:
                    if(indexY == 0) buttonWeapon1.StopHighlight();
                    if(indexY == 1) buttonSkill2.StopHighlight();
                    break;
                case 1:
                    if(indexY == 0) buttonWeapon2.StopHighlight();
                    if(indexY == 1) buttonSkill1.StopHighlight();
                    break;
            }
        }

        public void BuyColorless(int indexX, int indexY)
        {
            switch (indexX)
            {
                case 0:
                    if(indexY == 0) buttonWeapon1.BuyColorless();
                    if(indexY == 1) buttonSkill2.BuyColorless();
                    break;
                case 1:
                    if(indexY == 0) buttonWeapon2.BuyColorless();
                    if(indexY == 1) buttonSkill1.BuyColorless();
                    break;
            }
        }
    }
}