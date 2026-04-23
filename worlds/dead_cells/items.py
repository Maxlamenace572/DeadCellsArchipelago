"""
Dead Cells - Archipelago World
items.py

Defines all items in the Dead Cells randomizer, their AP classifications,
DLC requirements, and helper functions for item pool construction.
"""

from typing import Dict, Optional, Set
from BaseClasses import ItemClassification
from .base_classes import DeadCellsItem


# ──────────────────────────────────────────────
# Base item ID (all item IDs = BASE_ID + offset)
# ──────────────────────────────────────────────
BASE_ID = 0xDEAD_0000  # 3_740_827_648


# ──────────────────────────────────────────────
# DLC identifiers (match option flag names)
# ──────────────────────────────────────────────
DLC_BASE            = ""
DLC_RISE_OF_GIANT   = "RiseOfTheGiant"
DLC_BAD_SEED        = "TheBadSeed"
DLC_FATAL_FALLS     = "FatalFalls"
DLC_QUEEN_AND_SEA   = "TheQueenAndTheSea"
DLC_PURPLE          = "Purple"  # Return to Castlevania

ALL_DLCS = {
    DLC_RISE_OF_GIANT,
    DLC_BAD_SEED,
    DLC_FATAL_FALLS,
    DLC_QUEEN_AND_SEA,
    DLC_PURPLE,
}


# ──────────────────────────────────────────────
# Item classification helpers
# ──────────────────────────────────────────────
PROG  = ItemClassification.progression
USFL  = ItemClassification.useful
FILR  = ItemClassification.filler
TRAP  = ItemClassification.trap


# ──────────────────────────────────────────────
# Item data table
# Format: "ItemID": (offset, classification, dlc)
#
# Offsets are grouped by category for readability:
#   0000-00FF  Runes (progression)
#   0100-01FF  Upgrades / Meta unlocks (useful)
#   0200-02FF  Melee weapons
#   0300-03FF  Ranged weapons
#   0400-04FF  Shields
#   0500-05FF  Powers
#   0600-06FF  Grenades
#   0700-07FF  Deployed Traps
#   0800-08FF  Perks
#   0900-09FF  Aspects
#   1000-10FF  Consumables / Filler
#   1100-11FF  Precious Loot / Filler
#   1200-13FF  Skins
#   1400-14FF  Head cosmetics
#   1500-15FF  AP Trap items
# ──────────────────────────────────────────────
ITEM_TABLE: Dict[str, tuple] = {

    # ── Runes (Progression) ───────────────────────────────────────────
    "Vine Rune":            (0x0000, PROG, DLC_BASE),
    "Teleportation Rune":   (0x0001, PROG, DLC_BASE),
    "Challenger's Rune":    (0x0002, PROG, DLC_BASE),
    "Customization Rune":   (0x0003, PROG, DLC_BASE),
    "Ram Rune":             (0x0004, PROG, DLC_BASE),
    "Spider Rune":          (0x0005, PROG, DLC_BASE),
    "Homunculus Rune":      (0x0006, PROG, DLC_BASE),
    "Explorer's Rune":      (0x0007, PROG, DLC_BASE),
    "Lighthouse Key":       (0x0010, PROG, DLC_BASE),
    "Progressive Stem Cell":(0x0008, PROG, DLC_BASE),
  

    # ── Meta Upgrades (Useful) ────────────────────────────────────────
    "Progressive Flask":    (0x0100, PROG, DLC_BASE),
    "Backpack":             (0x0104, PROG, DLC_BASE),
    "Advanced Forge 1":     (0x0105, USFL, DLC_BASE),
    "Recycling Tubes":      (0x0106, USFL, DLC_BASE),
    "Hunter's Mirror":      (0x0107, USFL, DLC_BASE),
    "Specialist's Showroom":(0x0108, PROG, DLC_BASE),
    "Restock":              (0x0109, USFL, DLC_BASE),
    "Merchandise Categories":(0x010A, USFL, DLC_BASE),
    "Progressive Recycling":(0x010B, USFL, DLC_BASE),
    "Random Starter Bow":   (0x010D, USFL, DLC_BASE),
    "Random Starter Shield":(0x010E, USFL, DLC_BASE),
    "Random Melee Weapon":  (0x010F, USFL, DLC_BASE),
    "Progressive Gold Reserves":(0x0110, USFL, DLC_BASE),

    # ── Melee Weapons (Useful) ────────────────────────────────────────
    "Balanced Blade":           (0x0200, USFL, DLC_BASE),
    "Spite Sword":         (0x0201, USFL, DLC_BASE),
    "Assassin's Dagger":          (0x0202, USFL, DLC_BASE),
    "Blood Sword":              (0x0203, USFL, DLC_BASE),
    "Twin Daggers":          (0x0204, USFL, DLC_BASE),
    "Broadsword":           (0x0205, USFL, DLC_BASE),
    "Shovel":               (0x0206, USFL, DLC_BASE),
    "Cursed Sword":            (0x0207, USFL, DLC_BASE),
    "Sadist's Stiletto":            (0x0208, USFL, DLC_BASE),
    "Swift Sword":           (0x0209, USFL, DLC_BASE),
    "Giantkiller":          (0x020A, USFL, DLC_RISE_OF_GIANT),
    "Shrapnel Axes":          (0x020B, USFL, DLC_BASE),
    "Seismic Strike":          (0x020C, USFL, DLC_BASE),
    "War Spear":                (0x020D, USFL, DLC_BASE),
    "Impaler":          (0x020E, USFL, DLC_BASE),
    "Symmetrical Lance":           (0x020F, USFL, DLC_BASE),
    "Rapier":               (0x0210, USFL, DLC_BASE),
    "Meat Skewer":            (0x0211, USFL, DLC_BASE),
    "Nutcracker":             (0x0212, USFL, DLC_BASE),
    "Spartan Sandals":            (0x0213, USFL, DLC_BASE),
    "Spiked Boots":          (0x0214, USFL, DLC_BASE),
    "Hayabusa Boots":       (0x0215, USFL, DLC_BASE),
    "Hayabusa Gauntlets":           (0x0216, USFL, DLC_BASE),
    "Valmont's Whip":                 (0x0217, USFL, DLC_BASE),
    "Wrenching Whip":             (0x0218, USFL, DLC_BASE),
    "Oiled Sword":             (0x0219, USFL, DLC_BASE),
    "Torch":               (0x021A, USFL, DLC_BASE),
    "Frantic Sword":            (0x021B, USFL, DLC_BASE),
    "Flawless":       (0x021C, USFL, DLC_BASE),
    "Flint":       (0x021D, USFL, DLC_BASE),
    "Tentacle":         (0x021E, USFL, DLC_BASE),
    "Vorpan":                  (0x021F, USFL, DLC_BASE),
    "Flashing Fans":           (0x0220, USFL, DLC_BAD_SEED),
    "Scythe Claw":       (0x0221, USFL, DLC_BAD_SEED),
    "Rhythm n' Bouzouki":        (0x0222, USFL, DLC_BAD_SEED),
    "Crowbar":              (0x0223, USFL, DLC_BASE),
    "Snake Fangs":            (0x0224, USFL, DLC_FATAL_FALLS),
    "Iron Staff":           (0x0225, USFL, DLC_FATAL_FALLS),
    "Ferryman's Lantern":              (0x0226, USFL, DLC_FATAL_FALLS),
    "Hattori's Katana":               (0x0227, USFL, DLC_BASE),
    "Tombstone":            (0x0228, USFL, DLC_BASE),
    "Oven Axe":             (0x0229, USFL, DLC_BASE),
    "Toothpick":                 (0x022A, USFL, DLC_RISE_OF_GIANT),
    "Machete and Pistol":        (0x022B, USFL, DLC_BASE),
    "Hard Light Sword":       (0x022C, USFL, DLC_BASE),
    "Pure Nail":             (0x022D, USFL, DLC_BASE),
    "Bone":             (0x022E, USFL, DLC_BASE),
    "Abyssal Trident":              (0x022F, USFL, DLC_QUEEN_AND_SEA),
    "Hand Hook":             (0x0230, USFL, DLC_QUEEN_AND_SEA),
    "Maw of the Deep":                (0x0231, USFL, DLC_QUEEN_AND_SEA),
    "Bladed Tonfas":          (0x0232, USFL, DLC_QUEEN_AND_SEA),
    "Wrecking Ball":         (0x0233, USFL, DLC_QUEEN_AND_SEA),
    "Queen's Rapier":          (0x0234, USFL, DLC_QUEEN_AND_SEA),
    "Dagger of Profit":       (0x0235, USFL, DLC_BASE),
    "Gold Digger":           (0x0236, USFL, DLC_BASE),
    "King Scepter":          (0x0237, USFL, DLC_BASE),
    "Baseball Bat":          (0x0238, USFL, DLC_BASE),
    "Panchaku":          (0x0239, USFL, DLC_BASE),
    "Starfury":             (0x023A, USFL, DLC_BASE),
    "Alucard's Sword":              (0x023B, USFL, DLC_PURPLE),
    "Morning Star":           (0x023C, USFL, DLC_PURPLE),
    "Bible":                (0x023D, USFL, DLC_PURPLE),
    "Whip Sword":     (0x023E, USFL, DLC_PURPLE),
    "Vampire Killer":        (0x023F, USFL, DLC_PURPLE),
    "Death's Scythe":          (0x0240, USFL, DLC_PURPLE),
    "Sewing Scissors":              (0x0241, USFL, DLC_BASE),
    "Giant Comb":                 (0x0242, USFL, DLC_BASE),
    "Misericord":           (0x0243, USFL, DLC_BASE),

    # ── Ranged Weapons (Useful) ───────────────────────────────────────
    "Multiple-nocks Bow":      (0x0300, USFL, DLC_BASE),
    "Bow and Endless Quiver":  (0x0301, USFL, DLC_BASE),
    "Marksman's Bow":          (0x0302, USFL, DLC_BASE),
    "Sonic Carbine":           (0x0303, USFL, DLC_RISE_OF_GIANT),
    "Infantry Bow":            (0x0304, USFL, DLC_BASE),
    "Quick Bow":               (0x0305, USFL, DLC_BASE),
    "Ice Bow":                 (0x0306, USFL, DLC_BASE),
    "Repeater Crossbow":       (0x0307, USFL, DLC_BASE),
    "Multiple-nocks Bow":      (0x0308, USFL, DLC_BASE),
    "Ice Crossbow":            (0x0309, USFL, DLC_BASE),
    "Explosive Crossbow":      (0x030A, USFL, DLC_BASE),
    "Alchemic Carbine":        (0x030B, USFL, DLC_BASE),
    "Boomerang":               (0x030C, USFL, DLC_BASE),
    "Hemorrhage":              (0x030D, USFL, DLC_RISE_OF_GIANT),
    "Boy's Axe":               (0x030E, USFL, DLC_RISE_OF_GIANT),
    "Throwing Spear":          (0x030F, USFL, DLC_RISE_OF_GIANT),
    "Hokuto's Bow":            (0x0310, USFL, DLC_BASE),
    "Nerves of Steel":         (0x0311, USFL, DLC_BASE),
    "Throwing Knife":          (0x0312, USFL, DLC_BASE),
    "Electric Whip":           (0x0313, USFL, DLC_BASE),
    "Firebrands":              (0x0314, USFL, DLC_BASE),
    "Ice Shards":              (0x0315, USFL, DLC_BASE),
    "Fireball":                (0x0316, USFL, DLC_BASE),
    "Lightning Bolt":          (0x0317, USFL, DLC_BASE),
    "Pyrotechnics":            (0x0318, USFL, DLC_BASE),
    "Ice Blast":               (0x0319, USFL, DLC_BASE),
    "Magic Missiles":          (0x031A, USFL, DLC_RISE_OF_GIANT),
    "Blowgun":                 (0x031B, USFL, DLC_BAD_SEED),
    "Barrel Launcher":         (0x031C, USFL, DLC_BASE),
    "Serenade":                (0x031D, USFL, DLC_QUEEN_AND_SEA),
    "Heavy Crossbow":          (0x031E, USFL, DLC_QUEEN_AND_SEA),
    "Gilded Yumi":             (0x031F, USFL, DLC_BASE),
    "Magic Missiles":          (0x0320, USFL, DLC_BASE),
    "Throwable Objects":       (0x0321, USFL, DLC_BASE),
    "Laser Glaive":            (0x0322, USFL, DLC_BASE),
    "Throwable Objects":       (0x0323, USFL, DLC_BASE),
    "Cross":                   (0x0324, USFL, DLC_PURPLE),
    "Throwing Axe":            (0x0325, USFL, DLC_PURPLE),
    "Medusa's Head":           (0x0326, USFL, DLC_PURPLE),
    "Anathema":                (0x0327, USFL, DLC_BASE),

    # ── Shields (Useful) ──────────────────────────────────────────────
    "Front Line Shield":        (0x0400, USFL, DLC_BASE),
    "Cudgel":               (0x0401, USFL, DLC_BASE),
    "Punishment":           (0x0402, USFL, DLC_BASE),
    "Knockback Shield":           (0x0403, USFL, DLC_BASE),
    "Rampart":              (0x0404, USFL, DLC_BASE),
    "Assault Shield":           (0x0405, USFL, DLC_BASE),
    "Bloodthirsty Shield":          (0x0406, USFL, DLC_BASE),
    "Greed Shield":          (0x0407, USFL, DLC_BASE),
    "Spiked Shield":          (0x0408, USFL, DLC_BASE),
    "Parry Shield":          (0x0409, USFL, DLC_BASE),
    "Force Shield":           (0x040A, USFL, DLC_BASE),
    "Thunder Shield":        (0x040B, USFL, DLC_RISE_OF_GIANT),
    "Ice Shield":            (0x040C, USFL, DLC_BASE),
    "Alucard's Shield":        (0x040D, USFL, DLC_PURPLE),

    # ── Powers / Skills (Useful) ──────────────────────────────────────
    "Death Orb":              (0x0500, USFL, DLC_BASE),
    "Tornado":              (0x0501, USFL, DLC_BASE),
    "Knife Dance":         (0x0502, USFL, DLC_BASE),
    "Corrupted Power":           (0x0503, USFL, DLC_BASE),
    "Vampirism":            (0x0504, USFL, DLC_BASE),
    "Tonic":            (0x0505, USFL, DLC_BASE),
    "Grappling Hook":                 (0x0506, USFL, DLC_BASE),
    "Phaser":            (0x0507, USFL, DLC_BASE),
    "Corrosive Cloud":           (0x0508, USFL, DLC_BASE),
    "Lacerating Aura":           (0x0509, USFL, DLC_BASE),
    "Wave of Denial":            (0x050A, USFL, DLC_BASE),
    "Wings of the Crow":                (0x050B, USFL, DLC_BASE),
    "Great Owl of War":                  (0x050C, USFL, DLC_BASE),
    "Lightspeed":                 (0x050D, USFL, DLC_BASE),
    "Giant Whistle":         (0x050E, USFL, DLC_BASE),
    "Telluric Shock":         (0x050F, USFL, DLC_BASE),
    "Collector's Syringe":        (0x0510, USFL, DLC_BASE),
    "Smoke Bomb":            (0x0511, USFL, DLC_BAD_SEED),
    "Mushroom Boi!":   (0x0512, USFL, DLC_BAD_SEED),
    "Ice Armor":             (0x0513, USFL, DLC_BASE),
    "Lightning Rods":         (0x0514, USFL, DLC_FATAL_FALLS),
    "Scarecrow's Sickles":      (0x0515, USFL, DLC_FATAL_FALLS),
    "Serenade":          (0x0516, USFL, DLC_FATAL_FALLS),
    "Cocoon":    (0x0517, USFL, DLC_FATAL_FALLS),
    "Face Flask":            (0x0518, USFL, DLC_BASE),
    "Pollo Power":           (0x0519, USFL, DLC_BASE),
    "Leghugger":       (0x051A, USFL, DLC_QUEEN_AND_SEA),
    "Diverse Deck":(0x051B, USFL, DLC_BASE),
    "Taunt":                (0x051C, USFL, DLC_BASE),
    "Rebound Stone":        (0x051D, USFL, DLC_PURPLE),
    "Maria's Cat":             (0x051E, USFL, DLC_PURPLE),
    "Bat Volley":            (0x051F, USFL, DLC_PURPLE),
    "Indulgence":           (0x0520, USFL, DLC_BASE),

    # ── Grenades (Useful) ─────────────────────────────────────────────
    "Powerful Gernade":     (0x0600, USFL, DLC_BASE),
    "Infantry Grenade":          (0x0601, USFL, DLC_BASE),
    "Cluster Grenade":          (0x0602, USFL, DLC_BASE),
    "Magnetic Grenade":        (0x0603, USFL, DLC_BASE),
    "Stun Grenade":      (0x0604, USFL, DLC_BASE),
    "Ice Grenade":              (0x0605, USFL, DLC_BASE),
    "Fire Grenade":             (0x0606, USFL, DLC_BASE),
    "Root Grenade":             (0x0607, USFL, DLC_BASE),
    "Oil Grenade":              (0x0608, USFL, DLC_BASE),
    "Swarm":             (0x0609, USFL, DLC_BASE),
    "Holy Water":            (0x060A, USFL, DLC_PURPLE),

    # ── Deployed Traps (Useful) ───────────────────────────────────────
    "Double Crossb-o-matic":     (0x0700, USFL, DLC_BASE),
    "Sinew Slicer":       (0x0701, USFL, DLC_BASE),
    "Heavy Turret":          (0x0702, USFL, DLC_BASE),
    "Barnacle":           (0x0703, USFL, DLC_BASE),
    "Flamethrower Turret":           (0x0704, USFL, DLC_BASE),
    "Cleaver":            (0x0705, USFL, DLC_BASE),
    "Wolf Trap":             (0x0706, USFL, DLC_BASE),
    "Crusher":              (0x0707, USFL, DLC_BASE),
    "Explosive Decoy":                (0x0708, USFL, DLC_BASE),
    "Emergency Door":         (0x0709, USFL, DLC_BASE),
    "Tesla Coil":            (0x070A, USFL, DLC_BASE),
    "Scavenged Bombard":               (0x070B, USFL, DLC_QUEEN_AND_SEA),

	# ── Mutations (Useful) ─────────────────────────────────────────────
	"Killer Instinct":              (0x0800, USFL, DLC_BASE),
	"Combo":                        (0x0801, USFL, DLC_BASE),
	"Vengeance":                    (0x0802, USFL, DLC_BASE),
	"Melee":                        (0x0803, USFL, DLC_BASE),
	"Open Wounds":                  (0x0804, USFL, DLC_BASE),
	"Corrupted Power":              (0x0805, USFL, DLC_BASE),
	"Adrenaline":                   (0x0806, USFL, DLC_BASE),
	"Recovery":                     (0x0807, USFL, DLC_BASE),
	"Scheme":                       (0x0808, USFL, DLC_BASE),
	"Initiative":                   (0x0809, USFL, DLC_BASE),
	"Predator":                     (0x080A, USFL, DLC_BASE),
	"Porcupack":                    (0x080B, USFL, DLC_BASE),
	"Support":                      (0x080C, USFL, DLC_BASE),
	"Dead Inside":                  (0x080D, USFL, DLC_BASE),
	"Tranquility":                  (0x080E, USFL, DLC_BASE),
	"Ripper":                       (0x080F, USFL, DLC_BASE),
	"Parting Gift":                 (0x0810, USFL, DLC_BASE),
	"Barbed Tips":                  (0x0811, USFL, DLC_BASE),
	"Point Blank":                  (0x0812, USFL, DLC_BASE),
	"Shared Suffering":             (0x0813, USFL, DLC_BASE),
	"Caltrops":                     (0x0814, USFL, DLC_BASE),
	"Blind Faith":                  (0x0815, USFL, DLC_BASE),
	"Velocity":                     (0x0816, USFL, DLC_BASE),
	"Acrobatipack":                 (0x0817, USFL, DLC_BASE),
	"Necromancy":                   (0x0818, USFL, DLC_BASE),
	"Disengagement":                (0x0819, USFL, DLC_BASE),
	"Counterattack":                (0x081A, USFL, DLC_BASE),
	"Spite":                        (0x081B, USFL, DLC_BASE),
	"What Doesn't Kill Me":         (0x081C, USFL, DLC_BASE),
	"Frenzy":                       (0x081D, USFL, DLC_BASE),
	"Gastronomy":                   (0x081E, USFL, DLC_BASE),
	"Extended Healing":             (0x081F, USFL, DLC_BASE),
	"Armadillopack":                (0x0820, USFL, DLC_BASE),
	"Masochist":                    (0x0821, USFL, DLC_BASE),
	"Kill Rhythm":                  (0x0822, USFL, DLC_BASE),
	"Armadillo Pack":           (0x0823, USFL, DLC_BASE),
	"Ygdar Orus Li Ox":             (0x0824, USFL, DLC_BASE),
	"Frostbite":                    (0x0825, USFL, DLC_BASE),
	"Rally":                        (0x0826, USFL, DLC_BASE),
	"Emergency Triage":             (0x0827, USFL, DLC_BASE),
	"Berserker":                    (0x0828, USFL, DLC_BASE),
	"Soldier's Resistance":         (0x0829, USFL, DLC_BASE),
	"Acceptance":                   (0x082A, USFL, DLC_BASE),
	"Alienation":                   (0x082B, USFL, DLC_BASE),
	"Instinct of the Master of Arms": (0x082C, USFL, DLC_BASE),
	"Disengagement":                (0x082D, USFL, DLC_BASE),
	"Execution":                    (0x082E, USFL, DLC_BASE),
	"Critical Recovery":            (0x082F, USFL, DLC_BASE),
	"Ammo":                         (0x0830, USFL, DLC_BASE),
	"Gold Plating":                 (0x0831, USFL, DLC_BASE),
	"Get Rich Quick":               (0x0832, USFL, DLC_BASE),
	"Midas' Blood":                 (0x0833, USFL, DLC_BASE),
	"Wish":                         (0x0834, USFL, DLC_BASE),
	"Cursed Flask":                 (0x0835, USFL, DLC_BASE),
	"Damned Vigor":                 (0x0836, USFL, DLC_BASE),
	"Demonic Strength":             (0x0837, USFL, DLC_BASE),

    # ── Aspects (Useful) ──────────────────────────────────────────────
    "Blood Drinker":     (0x0900, USFL, DLC_BASE),
    "Stomper":          (0x0901, USFL, DLC_BASE),
    "Shatter":          (0x0902, USFL, DLC_BASE),
    "Toxin Lover":       (0x0903, USFL, DLC_BASE),
    "Relentless":        (0x0904, USFL, DLC_BASE),
    "Gotta Go Fast":      (0x0905, USFL, DLC_BASE),
    "Tinker":           (0x0906, USFL, DLC_BASE),
    "Firestarter":      (0x0907, USFL, DLC_BASE),
    "Menagerie":        (0x0908, USFL, DLC_BASE),
    "Grenadier":        (0x0909, USFL, DLC_BASE),
    "Superconductor":   (0x090A, USFL, DLC_BASE),
    "Assassin":         (0x090B, USFL, DLC_BASE),
    "Damned":           (0x090C, USFL, DLC_BASE),

    # ── Consumables / Fillers ─────────────────────────────────────────
    "AnyUp":                (0x1000, FILR, DLC_BASE),
    "BTUp":                 (0x1001, FILR, DLC_BASE),
    "BSUp":                 (0x1002, FILR, DLC_BASE),
    "TSUp":                 (0x1003, FILR, DLC_BASE),
    "AllUp":                (0x1004, FILR, DLC_BASE),
    "DeathMoney":           (0x1005, FILR, DLC_BASE),
    "DeathCells":           (0x1006, FILR, DLC_BASE),
    "SmallMeat":            (0x1007, FILR, DLC_BASE),
    "LargeMeat":            (0x1008, FILR, DLC_BASE),
    "SmallVeggie":          (0x1009, FILR, DLC_BASE),
    "LargeVeggie":          (0x100A, FILR, DLC_BASE),
    "SmallMonster":         (0x100B, FILR, DLC_BASE),
    "LargeMonster":         (0x100C, FILR, DLC_BASE),
    "SmallFruit":           (0x100D, FILR, DLC_BASE),
    "LargeFruit":           (0x100E, FILR, DLC_BASE),
    "SmallCastlevania":     (0x100F, FILR, DLC_BASE),
    "LargeCastlevania":     (0x1010, FILR, DLC_BASE),
    "SmallBaguette":        (0x1011, FILR, DLC_BASE),
    "LargeBaguette":        (0x1012, FILR, DLC_BASE),
    "SmallHalfLife":        (0x1013, FILR, DLC_BASE),
    "LargeHalfLife":        (0x1014, FILR, DLC_BASE),
    "SmallCheese":          (0x1015, FILR, DLC_BASE),
    "LargeCheese":          (0x1016, FILR, DLC_BASE),
    "FlaskRefill":          (0x1017, FILR, DLC_BASE),
    "InfectionRemedy":      (0x1018, FILR, DLC_BASE),
    "InfectionRemedySmall": (0x1019, FILR, DLC_BASE),
    "CellBonus":            (0x101A, FILR, DLC_BASE),

    # ── Precious Loot / Fillers ───────────────────────────────────────
    "LegendGem":            (0x1100, FILR, DLC_BASE),
    "HugeGem":              (0x1101, FILR, DLC_BASE),
    "BigGem":               (0x1102, FILR, DLC_BASE),
    "MediumGem":            (0x1103, FILR, DLC_BASE),
    "SmallGem":             (0x1104, FILR, DLC_BASE),
    "MinorGem":             (0x1105, FILR, DLC_BASE),
    "SpawnerGem":           (0x1106, FILR, DLC_BASE),
    "GreedGem":             (0x1107, FILR, DLC_BASE),
    "CellGold":             (0x1108, FILR, DLC_BASE),
    "GreedArrow":           (0x1109, FILR, DLC_BASE),
    "CursedGem":            (0x110A, FILR, DLC_BASE),

	# ── Skins / Fillers ───────────────────────────────────────────────
	"Golden Outfit":                     (0x1200, USFL, DLC_BASE),
	"Son Goku Outfit":                   (0x1201, USFL, DLC_BASE),
	"Black Outfit":                      (0x1202, USFL, DLC_BASE),
	"Ghost Outfit":                      (0x1203, USFL, DLC_BASE),
	"Sewers Outfit":                     (0x1204, USFL, DLC_BASE),
	"Santa Outfit":                      (0x1205, USFL, DLC_RISE_OF_GIANT),
	"Stilt Outfit":                      (0x1206, USFL, DLC_BASE),
	"Skeleton Outfit":                   (0x1207, USFL, DLC_BASE),
	"Carduus Outfit":                    (0x1208, USFL, DLC_BASE),
	"Aphrodite Outfit":                  (0x1209, USFL, DLC_BASE),
	"Shaman Outfit":                     (0x120A, USFL, DLC_BASE),
	"Cloud Outfit":                      (0x120B, USFL, DLC_BASE),
	"Hyper Light Drifter Outfit":        (0x120C, USFL, DLC_BASE),
	"Aladdin Outfit":                    (0x120D, USFL, DLC_BASE),
	"Bison Outfit":                      (0x120E, USFL, DLC_BASE),
	"Warrior Outfit":                    (0x120F, USFL, DLC_BASE),
	"Mage Outfit":                       (0x1210, USFL, DLC_BASE),
	"Neon Outfit":                       (0x1211, USFL, DLC_BASE),
	"Bobby Outfit":                      (0x1212, USFL, DLC_BASE),
	"Demon Outfit":                      (0x1213, USFL, DLC_BASE),
	"Sylvanian Outfit":                  (0x1214, USFL, DLC_BASE),
	"Sand Outfit":                       (0x1215, USFL, DLC_BASE),
	"GOG Outfit":                        (0x1216, USFL, DLC_BASE),
	"French Outfit":                     (0x1217, USFL, DLC_BASE),
	"Festive Outfit":                    (0x1218, USFL, DLC_BASE),
	"Gardener Outfit":                   (0x1219, USFL, DLC_BAD_SEED),
	"Friendly Hardy Outfit":             (0x121A, USFL, DLC_BAD_SEED),
	"Mushroom King Outfit":              (0x121B, USFL, DLC_BAD_SEED),
	"Fugitive Outfit":                   (0x121C, USFL, DLC_BAD_SEED),
	"Blowgunner Outfit":                 (0x121D, USFL, DLC_BAD_SEED),
	"Tick Outfit":                       (0x121E, USFL, DLC_BAD_SEED),
	"Royal Gardener Outfit":             (0x121F, USFL, DLC_BAD_SEED),
	"Retro Outfit":                      (0x1220, USFL, DLC_BASE),
	"Gordon Freeman Outfit":             (0x1221, USFL, DLC_BASE),
	"Javelin Snake Outfit":              (0x1222, USFL, DLC_FATAL_FALLS),
	"Necromancer Outfit":                (0x1223, USFL, DLC_FATAL_FALLS),
	"Bootleg Outfit":                    (0x1224, USFL, DLC_FATAL_FALLS),
	"Kamikaze Outfit":                   (0x1225, USFL, DLC_BASE),
	"Crossbowman Outfit":                (0x1226, USFL, DLC_BASE),
	"Kill Bill Outfit":                  (0x1227, USFL, DLC_BASE),
	"King Outfit":                       (0x1228, USFL, DLC_BASE),
	"White King Outfit":                 (0x1229, USFL, DLC_BASE),
	"Concierge Outfit":                  (0x122A, USFL, DLC_BASE),
	"Piccolo Concierge Outfit":          (0x122B, USFL, DLC_BASE),
	"Misunderstood Concierge Outfit":    (0x122C, USFL, DLC_BASE),
	"Blacksmith Concierge Outfit":       (0x122D, USFL, DLC_BASE),
	"Golden Concierge Outfit":           (0x122E, USFL, DLC_BASE),
	"Classic Conjunctivius Outfit":      (0x122F, USFL, DLC_BASE),
	"Starved Conjunctivius Outfit":      (0x1230, USFL, DLC_BASE),
	"Enraged Conjunctivius Outfit":      (0x1231, USFL, DLC_BASE),
	"Tentacled Conjunctivius Outfit":    (0x1232, USFL, DLC_BASE),
	"Aurora Borealis Conjunctivius Outfit": (0x1233, USFL, DLC_BASE),
	"Classic Temporal Outfit":           (0x1234, USFL, DLC_BASE),
	"Apex Temporal Outfit":              (0x1235, USFL, DLC_BASE),
	"Red Temporal Outfit":               (0x1236, USFL, DLC_BASE),
	"Hunter's Temporal Outfit":      (0x1237, USFL, DLC_BASE),
	"Devilish Temporal Outfit":          (0x1238, USFL, DLC_BASE),
	"Classic Giant Outfit":              (0x1239, USFL, DLC_RISE_OF_GIANT),
	"Mutineer Giant Outfit":             (0x123A, USFL, DLC_RISE_OF_GIANT),
	"Royal Giant Outfit":                (0x123B, USFL, DLC_RISE_OF_GIANT),
	"Frustrated Giant's Outfit":         (0x123C, USFL, DLC_RISE_OF_GIANT),
	"Cavern Dweller Giant Outfit":       (0x123D, USFL, DLC_RISE_OF_GIANT),
	"The Hand of the King Outfit":       (0x123E, USFL, DLC_BASE),
	"Loyal Hand of the King Outfit":     (0x123F, USFL, DLC_BASE),
	"Majestic Hand of the King Outfit":  (0x1240, USFL, DLC_BASE),
	"Red Hand of the King Outfit":       (0x1241, USFL, DLC_BASE),
	"The Leeching Hand of the King Outfit": (0x1242, USFL, DLC_BASE),
	"Statue Outfit":                     (0x1243, USFL, DLC_FATAL_FALLS),
	"Collector Outfit":                  (0x1244, USFL, DLC_BASE),
	"Classic Mama Tick Outfit":          (0x1245, USFL, DLC_BAD_SEED),
	"Sharp Mama Tick Outfit":            (0x1246, USFL, DLC_BAD_SEED),
	"Wigged Mama Tick Outfit":           (0x1247, USFL, DLC_BAD_SEED),
	"Mad Tick Outfit":                   (0x1248, USFL, DLC_BAD_SEED),
	"Furious Tick Outfit":          (0x1249, USFL, DLC_BAD_SEED),
	"Sacrificial Tick Outfit":           (0x124A, USFL, DLC_BAD_SEED),
	"Classic Scarecrow Outfit":          (0x124B, USFL, DLC_FATAL_FALLS),
	"Rusted Scarecrow Outfit":           (0x124C, USFL, DLC_FATAL_FALLS),
	"Cardinal Scarecrow Outfit":         (0x124D, USFL, DLC_FATAL_FALLS),
	"Festering Scarecrow Outfit":        (0x124E, USFL, DLC_FATAL_FALLS),
	"Murderous Scarecrow Outfit":        (0x124F, USFL, DLC_FATAL_FALLS),
	"Cultist Outfit":                    (0x1250, PROG, DLC_FATAL_FALLS),
	"Flawless Concierge Outfit":         (0x1251, USFL, DLC_BASE),
	"Flawless Conjunctivius Outfit":     (0x1252, USFL, DLC_BASE),
	"Flawless Time Keeper Outfit":       (0x1253, USFL, DLC_BASE),
	"Flawless Giant Outfit":             (0x1254, USFL, DLC_RISE_OF_GIANT),
	"Flawless Hand of the King Outfit":  (0x1255, USFL, DLC_BASE),
	"Flawless Mama Tick Outfit":         (0x1256, USFL, DLC_BAD_SEED),
	"Flawless Scarecrow Outfit":         (0x1257, USFL, DLC_FATAL_FALLS),
	"Snowman Outfit":                    (0x1258, USFL, DLC_BASE),
	"Santa Outfit":                      (0x1259, USFL, DLC_BASE),
	"Hollow Knight Outfit":              (0x125A, USFL, DLC_BASE),
	"Blasphemous Outfit":                (0x125B, USFL, DLC_BASE),
	"Guacamelee Outfit":                 (0x125C, USFL, DLC_BASE),
	"Skul Outfit":                       (0x125D, USFL, DLC_BASE),
	"Hyper Light Drifter Outfit":        (0x125E, USFL, DLC_BASE),
	"Curse of the Dead Gods Outfit":     (0x125F, USFL, DLC_BASE),
	"Soul Knight Outfit":                (0x1260, USFL, DLC_BASE),
	"Staphy Outfit":                     (0x1261, USFL, DLC_QUEEN_AND_SEA),
	"Anchor Guy Outfit":                 (0x1262, USFL, DLC_QUEEN_AND_SEA),
	"Servants Outfit":                   (0x1263, USFL, DLC_QUEEN_AND_SEA),
	"Burnished Servants Outfit":         (0x1264, USFL, DLC_QUEEN_AND_SEA),
	"Indigo Servants Outfit":            (0x1265, USFL, DLC_QUEEN_AND_SEA),
	"Shining Servants Outfit":           (0x1266, USFL, DLC_QUEEN_AND_SEA),
	"Luminous Servants Outfit":          (0x1267, USFL, DLC_QUEEN_AND_SEA),
	"Flawless Servants Outfit":          (0x1268, USFL, DLC_QUEEN_AND_SEA),
	"Queen Outfit":                      (0x1269, USFL, DLC_QUEEN_AND_SEA),
	"White Gold Queen Outfit":           (0x126A, USFL, DLC_QUEEN_AND_SEA),
	"Cherry Blossom Queen Outfit":       (0x126B, USFL, DLC_QUEEN_AND_SEA),
	"Spicy Queen Outfit":                (0x126C, USFL, DLC_QUEEN_AND_SEA),
	"Stinging Queen Outfit":             (0x126D, USFL, DLC_QUEEN_AND_SEA),
	"Flawless Queen Outfit":             (0x126E, USFL, DLC_QUEEN_AND_SEA),
	"Delayed Hedgehog Outfit":             (0x126F, USFL, DLC_QUEEN_AND_SEA),
	"Banker Outfit":                     (0x1270, USFL, DLC_BASE),
	"Guillain Outfit":                   (0x1271, USFL, DLC_BASE),
	"Bobby Outfit":                      (0x1272, USFL, DLC_BASE),
	"Knight's Outfit":                   (0x1273, USFL, DLC_BASE),
	"Hotline Miami Outfit":              (0x1274, USFL, DLC_BASE),
	"Katana ZERO Outfit":                (0x1275, USFL, DLC_BASE),
	"Risk of Rain Outfit":               (0x1276, USFL, DLC_BASE),
	"Terraria Outfit":                   (0x1277, USFL, DLC_BASE),
	"Slay the Spire Outfit":             (0x1278, USFL, DLC_BASE),
	"Mentor Outfit":                     (0x1279, USFL, DLC_BASE),
	"Mentor Outfit 1":                   (0x127A, USFL, DLC_BASE),
	"Mentor Outfit 2":                   (0x127B, USFL, DLC_BASE),
	"Mentor Outfit 3":                   (0x127C, USFL, DLC_BASE),
	"Victorious Outfit":                 (0x127D, USFL, DLC_BASE),
	"Victorious Outfit 1":               (0x127E, USFL, DLC_BASE),
	"Victorious Outfit 2":               (0x127F, USFL, DLC_BASE),
	"Victorious Outfit 3":               (0x1280, USFL, DLC_BASE),
	"Simon Outfit":                      (0x1281, USFL, DLC_PURPLE),
	"Alucard Outfit":                    (0x1282, USFL, DLC_PURPLE),
	"Richter Outfit":                    (0x1283, USFL, DLC_PURPLE),
	"Sypha Outfit":                      (0x1284, USFL, DLC_PURPLE),
	"Trevor Outfit":                     (0x1285, USFL, DLC_PURPLE),
	"Maria Outfit":                      (0x1286, USFL, DLC_PURPLE),
	"Hector Outfit":                     (0x1287, USFL, DLC_PURPLE),
	"Haunted Armor Outfit":              (0x1288, USFL, DLC_PURPLE),
	"Death Outfit":                      (0x1289, USFL, DLC_PURPLE),
	"Cold Death Outfit":             (0x128A, USFL, DLC_PURPLE),
	"Twilight Death Outfit":             (0x128B, USFL, DLC_PURPLE),
	"Regal Death Outfit":                (0x128C, USFL, DLC_PURPLE),
	"Pale Death Outfit":                 (0x128D, USFL, DLC_PURPLE),
	"Flawless Death Outfit":             (0x128E, USFL, DLC_PURPLE),
	"Dracula Outfit":                    (0x128F, USFL, DLC_PURPLE),
	"Moonlit Dracula Outfit":            (0x1290, USFL, DLC_PURPLE),
	"Grand Dracula Outfit":              (0x1291, USFL, DLC_PURPLE),
	"Vampiric Dracula Outfit":           (0x1292, USFL, DLC_PURPLE),
	"Dark Lord Dracula Outfit":          (0x1293, USFL, DLC_PURPLE),
	"Flawless Dracula Outfit":           (0x1294, USFL, DLC_PURPLE),

  	# ── Head cosmetics / Fillers ──────────────────────────────────────
	"Bobby Head":               (0x1400, USFL, DLC_BASE),
	"Concierge Flame":          (0x1401, USFL, DLC_BASE),
	"Conjunctivius Tentacles":  (0x1402, USFL, DLC_BASE),
	"Mama Tick Eye":            (0x1403, USFL, DLC_BASE),
	"Time Keeper Hat":          (0x1404, USFL, DLC_BASE),
	"Giant Flame":              (0x1405, USFL, DLC_BASE),
	"Scarecrow Hat":            (0x1406, USFL, DLC_BASE),
	"Hand of the King Flame":   (0x1407, USFL, DLC_BASE),
	"Servants Mask":            (0x1408, USFL, DLC_BASE),
	"Queen Flame":              (0x1409, USFL, DLC_BASE),
	"Collector Hood":           (0x140A, USFL, DLC_BASE),
	"Black Hole":               (0x140B, USFL, DLC_BASE),
	"White Black Hole":         (0x140C, USFL, DLC_BASE),
	"Violet Black Hole":        (0x140D, USFL, DLC_BASE),
	"Red Black Hole":           (0x140E, USFL, DLC_BASE),
	"Green Black Hole":         (0x140F, USFL, DLC_BASE),
	"Blue Black Hole":          (0x1410, USFL, DLC_BASE),
	"Bitter":                   (0x1411, USFL, DLC_BASE),
	"Vortex":                   (0x1412, USFL, DLC_BASE),
	"Sanguine Vortex":          (0x1413, USFL, DLC_BASE),
	"Abyssal Vortex":           (0x1414, USFL, DLC_BASE),
	"Dark Vortex":              (0x1415, USFL, DLC_BASE),
	"Guillain Head":            (0x1416, USFL, DLC_BASE),
	"Fisherman's Hood":         (0x1417, USFL, DLC_BASE),
	"Leghugger Head":           (0x1418, USFL, DLC_BASE),
	"Flawless Head":            (0x1419, USFL, DLC_BASE),
	"Cell Head":                (0x141A, USFL, DLC_BASE),
	"Evil Empire Head":         (0x141B, USFL, DLC_BASE),
	"Toxic Blob":               (0x141C, USFL, DLC_BASE),
	"Glitchy Head":             (0x141D, USFL, DLC_BASE),
	"Mushroom Boi Cap":         (0x141E, USFL, DLC_BASE),
	"Hordes Zero Hood":         (0x141F, USFL, DLC_BASE),
	"Magma Blob":               (0x1420, USFL, DLC_BASE),
	"Malaise Blob":             (0x1421, USFL, DLC_BASE),
	"Sweet Blob":               (0x1422, USFL, DLC_BASE),
	"Spatial Anomaly":          (0x1423, USFL, DLC_BASE),
	"Menacing Anomaly":         (0x1424, USFL, DLC_BASE),
	"Black Blowtorch":          (0x1425, USFL, DLC_BASE),
	"Blowtorch":                (0x1426, USFL, DLC_BASE),
	"Gold Blowtorch":           (0x1427, USFL, DLC_BASE),
	"Bright Red Blowtorch":     (0x1428, USFL, DLC_BASE),
	"Boss Cell Head":           (0x1429, USFL, DLC_BASE),

    # ── AP Trap Items ─────────────────────────────────────────────────
    # These are sent to the Dead Cells player to hinder them mid-run.
    # The mod handles their in-game effect on the client side.
    "Trap_Curse":           (0x1500, TRAP, DLC_BASE),
    "Trap_SpawnElite":      (0x1501, TRAP, DLC_BASE),
    "Trap_RemoveGold":      (0x1502, TRAP, DLC_BASE),
    "Trap_BreakWeapon":     (0x1503, TRAP, DLC_BASE),
    "Trap_InvertControls":  (0x1504, TRAP, DLC_BASE),

    # region lock items
    "Prison Depths":        (0x1600, PROG, DLC_BASE),
    "Corrupted Prison":     (0x1601, PROG, DLC_BASE),
    "Ossuary":              (0x1602, PROG, DLC_BASE),
    "Ancient Sewers":       (0x1603, PROG, DLC_BASE),
    "Insufferable Crypt":   (0x1604, PROG, DLC_BASE),
    "Stilt Village":        (0x1605, PROG, DLC_BASE),
    "Slumbering Sanctuary": (0x1606, PROG, DLC_BASE),
    "Graveyard":            (0x1607, PROG, DLC_BASE),
    "Clock Tower":          (0x1608, PROG, DLC_BASE),
    "Forgotten Sepulcher":  (0x1609, PROG, DLC_BASE),
    "Clock Room":           (0x160A, PROG, DLC_BASE),
    "High Peak Castle":     (0x160B, PROG, DLC_BASE),
    "Derelict Distillery":  (0x160C, PROG, DLC_BASE),
    "Throne Room":          (0x160D, PROG, DLC_BASE),
    "Cavern":               (0x160E, PROG, DLC_RISE_OF_GIANT),
    "Guardian's Haven":     (0x160F, PROG, DLC_RISE_OF_GIANT),
    "Astrolab":             (0x1610, PROG, DLC_RISE_OF_GIANT),
    "Observatory":          (0x1611, PROG, DLC_RISE_OF_GIANT),
    "Dilapidated Arboretum": (0x1612, PROG, DLC_BAD_SEED),
    "Morass of the Banished": (0x1613, PROG, DLC_BAD_SEED),
    "Nest":                 (0x1614, PROG, DLC_BAD_SEED),
    "Fractured Shrines":    (0x1615, PROG, DLC_FATAL_FALLS),
    "Undying Shores":       (0x1616, PROG, DLC_FATAL_FALLS),
    "Mausoleum":            (0x1617, PROG, DLC_FATAL_FALLS),
    "Infested Shipwreck":   (0x1618, PROG, DLC_QUEEN_AND_SEA),
    "Lighthouse":           (0x1619, PROG, DLC_QUEEN_AND_SEA),
    "Crown":                (0x161A, PROG, DLC_QUEEN_AND_SEA),
    "Castle Outskirts":     (0x161B, PROG, DLC_PURPLE),
    "Dracula's Castle":     (0x161C, PROG, DLC_PURPLE),
    "Defiled Necropolis":   (0x161D, PROG, DLC_PURPLE),
    "Master's Keep":        (0x161E, PROG, DLC_PURPLE),
}


# ──────────────────────────────────────────────
# Lookup: item name → AP item ID
# ──────────────────────────────────────────────
def item_id(name: str) -> int:
    """Return the unique AP item ID for a given item name."""
    return BASE_ID + ITEM_TABLE[name][0]


# ──────────────────────────────────────────────
# Filtered item set helpers
# ──────────────────────────────────────────────
def get_items_for_dlcs(enabled_dlcs: Set[str]) -> Dict[str, tuple]:
    """
    Return only items whose DLC is enabled.
    Pass an empty set (or {DLC_BASE}) for base-game only.
    Always includes base-game items (dlc == "").
    """
    return {
        name: data
        for name, data in ITEM_TABLE.items()
        if data[2] == DLC_BASE or data[2] in enabled_dlcs
    }


def get_filler_items(enabled_dlcs):
    return [
        name
        for name, data in ITEM_TABLE.items()
        if data[1] == USFL
        and (data[2] == "" or data[2] in enabled_dlcs)
    ]


def get_trap_items():
    return [
        name
        for name, data in ITEM_TABLE.items()
        if data[1] == TRAP
    ]


def get_progression_items(enabled_dlcs: Set[str]) -> Dict[str, tuple]:
    """Return all progression items for the given DLC set."""
    return {
        name: data
        for name, data in get_items_for_dlcs(enabled_dlcs).items()
        if data[1] == PROG
    }

def is_cosmetic(item_name: str) -> bool:
    """Return True if the item is a cosmetic (skin or head)."""
    offset, _, _ = ITEM_TABLE[item_name]
    return 0x1200 <= offset <= 0x14FF


def get_cosmetic_items(enabled_dlcs: Set[str]) -> Dict[str, tuple]:
    """Return all cosmetic items filtered by enabled DLCs."""
    cosmetics = {}

    for name, (offset, classification, dlc) in ITEM_TABLE.items():
        if not (0x1200 <= offset <= 0x14FF):
            continue

        if dlc and dlc not in enabled_dlcs:
            continue

        cosmetics[name] = (offset, classification, dlc)

    return cosmetics
# ──────────────────────────────────────────────
# Sanity check: no duplicate offsets
# ──────────────────────────────────────────────
def _assert_no_duplicate_offsets() -> None:
    seen: Dict[int, str] = {}
    for name, (offset, _, _) in ITEM_TABLE.items():
        if offset in seen:
            raise ValueError(
                f"Duplicate offset 0x{offset:04X}: '{seen[offset]}' and '{name}'"
            )
        seen[offset] = name

_assert_no_duplicate_offsets()
