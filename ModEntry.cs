using dc;
using dc.en;
using dc.en.inter;
using dc.en.mob.boss;
using dc.en.mob.boss.death;
using dc.level.disp;
using dc.pr;
using dc.tool;
using dc.tool.weap;
using ModCore.Mods;
using ModCore.Modules;
using ModCore.Utilities;
using Serilog;
using static dc.tool.InventItemKind;

namespace DeadCellsArchipelago;
//E:\SteamLibrary\steamapps\common\Dead Cells\coremod\core\host\startup
public class ModEntry(ModInfo info) : ModBase(info)
{
    private Hero? _hero;
    public override void Initialize()
    {
        
        Log.Information("=== Archipelago Mod is loading... ===");
        
        Log.Information("=== Loading Boss Hooks... ===");
        // Hooking boss death events
        Hook_Behemoth.onDie += (orig, self) => { orig(self); OnBossKilled("The Concierge"); };
        Hook_Beholder.onDie += (orig, self) => { orig(self); OnBossKilled("Conjunctivius"); };
        Hook_MamaTick.onDie += (orig, self) => { orig(self); OnBossKilled("Mama Tick"); };
        Hook_Death.onDie += (orig, self) => { orig(self); OnBossKilled("Death"); }; //need to be tested

        Hook_TimeKeeper.onDie += (orig, self) => { orig(self); OnBossKilled("The Time Keeper"); };
        Hook_Giant.onDie += (orig, self) => { orig(self); OnBossKilled("The Giant"); };
        Hook_GardenerBoss.onDie += (orig, self) => { orig(self); OnBossKilled("Scarecrow"); };

        Hook_KingsHand.onDie += (orig, self) => { orig(self); OnBossKilled("The Hand of the King"); };
        Hook_Fx.servantChaseDefeat += (orig, self, e) => { orig(self, e); OnBossKilled("The Servants"); }; //need to be tested
        Hook_Dooku.onDie += (orig, self) => { orig(self); OnBossKilled("Dracula"); }; //might not use it, dracula first form

        Hook_Queen.onDie += (orig, self) => { orig(self); OnBossKilled("The Queen"); };
        Hook_DookuBeast.onDie += (orig, self) => { orig(self); OnBossKilled("Dracula - Final Form"); };
        Hook_Collector.onDie += (orig, self) => { orig(self); OnBossKilled("The Collector"); };
        
        Log.Information("=== Boss Hooks loaded ! ===");

        Hook_Hero.init += OnHeroInit;

        Log.Information("=== Archipelago Mod loaded ! ===");
    }
    
    private void OnBossKilled(string bossName)
    {
        Log.Information($"=== {bossName} killed! TODO: send check to Archipelago ===");
        // TODO: send check to Archipelago

        // Test give item to player if concierge
        if(bossName == "The Concierge")
        {
            for (int i = 0; i < 20; i++)
            {
                GiveConsumableToPlayer("AnyUp");
            }
        }
    }


    private void OnHeroInit(Hook_Hero.orig_init orig, Hero self)
    {
        orig(self);
        _hero = self;
        
        Log.Information($"=== Hero initialized ! ===");

        LogInventory();
        GiveWeaponToPlayer("StartSword");
        GiveWeaponToPlayer("AdminWeapon");
        GiveConsumableToPlayer("AnyUp");
        LogInventory();
        GiveConsumableToPlayer("BrutalityStuff");
        GiveConsumableToPlayer("BSUp");
        GiveConsumableToPlayer("AllUp");
    }

    private void GiveWeaponToPlayer(string weaponName)
    {
        if (_hero != null)
        {
            try
            {
                InventItem weaponItem = new InventItem(new InventItemKind.Weapon(weaponName.AsHaxeString()));
                Log.Information($"=== Weapon {weaponName} Created ===");

                bool inArmoryValue = false;
                ItemDrop itemDrop = new ItemDrop(
                    _hero._level,
                    _hero.cx,
                    _hero.cy,
                    weaponItem,
                    true,
                    new HaxeProxy.Runtime.Ref<bool>(ref inArmoryValue)
                );

                itemDrop.init();
                itemDrop.onDropAsLoot();
                itemDrop.dx = _hero.dx;
                
                Log.Information("=== Weapon Successfully Dropped ! ===");
            }
            catch (Exception ex)
            {
                Log.Error($"=== Erreur: {ex.Message} ===");
                Log.Error($"Stack trace: {ex.StackTrace}");
            }
        }
    }

    private void GiveConsumableToPlayer(string consumableName)
    {
        if (_hero != null)
        {
            try
            {
                InventItem consumableItem = new InventItem(new Consumable(consumableName.AsHaxeString()));
                Log.Information($"=== Consumable {consumableName} Created ===");

                bool inArmoryValue = false;
                ItemDrop itemDrop = new ItemDrop(
                    _hero._level,
                    _hero.cx,
                    _hero.cy,
                    consumableItem,
                    true,
                    new HaxeProxy.Runtime.Ref<bool>(ref inArmoryValue)
                );

                itemDrop.init();
                itemDrop.onDropAsLoot();
                itemDrop.dx = _hero.dx;
                
                Log.Information("=== Consumable Successfully Dropped ! ===");
            }
            catch (Exception ex)
            {
                Log.Error($"=== Erreur: {ex.Message} ===");
                Log.Error($"Stack trace: {ex.StackTrace}");
            }
        }
    }

    private void LogInventory()
    {
        Log.Information("=== Read all inventory ===");
        if (_hero?.inventory.items.length > 0)
        {
            var hasNext = true;
            var i = 0;
            var item = _hero.inventory.items.getDyn(i);
            while (hasNext)
            {
                Log.Information($"{i} : {item?.kind}");
                i++;
                item = _hero.inventory.items.getDyn(i);
                if(item == null)
                {
                    hasNext = false;
                }
            }
        }
        Log.Information("=== Inventory end ===");
    }
}