
using dc.en;
using dc.en.inter;
using dc.tool;
using ModCore.Utilities;
using Serilog;
using static dc.tool.InventItemKind;
using System.Text.Json;

namespace DeadCellsArchipelago {
    public static class ItemManager
    {
        public static Hero? HERO { get; set; }

        //Drop the item with the id @itemName to the player position
        //Warning: all items can be dropped, but if it has no pick up implementation, it will crash the game when you take it.
        //Same for using Weapon or Actives without the said uses implemented.
        public static void GiveItemToPlayer(string itemName)
        {
            if (HERO != null) {
                try
                {
                    InventItem? inventItem = CreateInventItemById(itemName);

                    if (inventItem != null) {
                        Log.Information($"=== Item {itemName} Created ===");
                        bool inArmoryValue = false;
                        ItemDrop itemDrop = new ItemDrop(
                            HERO._level,
                            HERO.cx,
                            HERO.cy,
                            inventItem,
                            true,
                            new HaxeProxy.Runtime.Ref<bool>(ref inArmoryValue)
                        );

                        itemDrop.init();
                        itemDrop.onDropAsLoot();
                        itemDrop.dx = HERO.dx;
                        
                        Log.Information("=== Item Successfully Dropped ! ===");
                    } else
                    {
                        Log.Error($"=== Item {itemName} could not be created ===");
                    }
                }
                catch (Exception ex)
                {
                    Log.Error($"=== Error: {ex.Message} ===");
                    Log.Error($"Stack trace: {ex.StackTrace}");
                }
            }
            else
            {
                Log.Error("=== Cannot log inventory, hero is null ===");
            }
        }

        private static InventItem? CreateInventItemById(string itemName)
        {
            string json = System.IO.File.ReadAllText("./coremod/mods/DeadCellsArchipelago/itemsId-Category.json"); //the json should be placed next to the modinfo.json

            Dictionary<string, string>? items = JsonSerializer.Deserialize<Dictionary<string, string>>(json);

            if (items == null)
            {
                Log.Error($"=== Could not get the json list of items ===");
                return null;
            }

            if (items.TryGetValue(itemName, out string? category))
            {
                Console.WriteLine($"=== Item {itemName} exists with category {category} ===");
            }
            else
            {
                Log.Error($"=== Item with id : {itemName} doesn't exist ===");
                return null;
            }

            InventItem? inventItem = null;

            switch (category)
            {
                case "DeployedTrap":
                case "Grenade":
                case "SideKick":
                case "Power":
                    Log.Information("0");
                    inventItem = new InventItem(new InventItemKind.Active(itemName.AsHaxeString()));
                    break;

                case "Melee":
                case "Ranged":
                case "Shield":
                    Log.Information("1");
                    inventItem = new InventItem(new InventItemKind.Weapon(itemName.AsHaxeString()));
                    break;

                case "Talisman":
                    Log.Information("2");
                    inventItem = new InventItem(new Talisman(itemName.AsHaxeString()));
                    break;

                case "BagItem":
                    Log.Information("3");
                    inventItem = new InventItem(new BagItem(itemName.AsHaxeString()));
                    break;

                case "Meta":
                    Log.Information("4");
                    inventItem = new InventItem(new Meta(itemName.AsHaxeString()));
                    break;

                case "Consumable":
                    Log.Information("5");
                    inventItem = new InventItem(new Consumable(itemName.AsHaxeString()));
                    break;

                case "PreciousLoot":
                    Log.Information("6");
                    inventItem = new InventItem(new PreciousLoot(itemName.AsHaxeString()));
                    break;

                case "Perk":
                    Log.Information("7");
                    inventItem = new InventItem(new Perk(itemName.AsHaxeString()));
                    break;

                case "Skin":
                    Log.Information("8");
                    inventItem = new InventItem(new Skin(itemName.AsHaxeString()));
                    break;

                case "Head":
                    Log.Information("9");
                    inventItem = new InventItem(new Head(itemName.AsHaxeString()));
                    break;

                case "Aspect":
                    Log.Information("10");
                    inventItem = new InventItem(new Aspect(itemName.AsHaxeString()));
                    break;

                case "BossRushStatueUnlock":
                    Log.Information("11");
                    inventItem = new InventItem(new BossRushStatueUnlock(itemName.AsHaxeString()));
                    break;
            }

            return inventItem;
        }

        public static void LogInventory()
        {
            if(HERO != null) {
                Log.Information("=== Read all inventory ===");
                if (HERO.inventory.items.length > 0)
                {
                    var hasNext = true;
                    var i = 0;
                    var item = HERO.inventory.items.getDyn(i);
                    while (hasNext)
                    {
                        Log.Information($"{i} : {item?.kind}");
                        i++;
                        item = HERO.inventory.items.getDyn(i);
                        if(item == null)
                        {
                            hasNext = false;
                        }
                    }
                }
                Log.Information("=== Inventory end ===");
            }
            else
            {
                Log.Error("=== Cannot log inventory, hero is null ===");
            }
        }
    }
}