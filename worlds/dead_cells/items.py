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
    "LadderKey":            (0x0000, PROG, DLC_BASE),
    "TeleportKey":          (0x0001, PROG, DLC_BASE),
    "ScoringKey":           (0x0002, PROG, DLC_BASE),
    "CustomKey":            (0x0003, PROG, DLC_BASE),
    "BreakableGroundKey":   (0x0004, PROG, DLC_BASE),
    "WallJumpKey":          (0x0005, PROG, DLC_BASE),
    "HomKey":               (0x0006, PROG, DLC_BASE),
    "ExploKey":             (0x0007, PROG, DLC_BASE),
    "LighthouseKey":        (0x0010, PROG, DLC_BASE),
    "BossRune1":            (0x0008, PROG, DLC_BASE),
    "BossRune2":            (0x0009, PROG, DLC_BASE),
    "BossRune3":            (0x000A, PROG, DLC_BASE),
    "BossRune4":            (0x000B, PROG, DLC_BASE),
    "BossRune5":            (0x000C, PROG, DLC_RISE_OF_GIANT),

    # ── Meta Upgrades (Useful) ────────────────────────────────────────
    "Flask1":               (0x0100, PROG, DLC_BASE),
    "Flask2":               (0x0101, USFL, DLC_BASE),
    "Flask3":               (0x0102, USFL, DLC_BASE),
    "Flask4":               (0x0103, USFL, DLC_BASE),
    "BackpackUnlock":       (0x0104, PROG, DLC_BASE),
    "ForgeRefine1":         (0x0105, USFL, DLC_BASE),
    "ArmoryUnlock":         (0x0106, USFL, DLC_BASE),
    "MirrorUnlock":         (0x0107, USFL, DLC_BASE),
    "PokebombUnlock":       (0x0108, USFL, DLC_BASE),
    "ShopRerolls":          (0x0109, USFL, DLC_BASE),
    "ShopCategories":       (0x010A, USFL, DLC_BASE),
    "Recycling1":           (0x010B, USFL, DLC_BASE),
    "Recycling2":           (0x010C, USFL, DLC_BASE),
    "RandomBow":            (0x010D, USFL, DLC_BASE),
    "RandomShield":         (0x010E, USFL, DLC_BASE),
    "RandomCC":             (0x010F, USFL, DLC_BASE),
    "Money1":               (0x0110, USFL, DLC_BASE),
    "Money2":               (0x0111, USFL, DLC_BASE),
    "Money3":               (0x0112, USFL, DLC_BASE),
    "Money4":               (0x0113, USFL, DLC_BASE),
    "Money5":               (0x0114, USFL, DLC_BASE),

    # ── Melee Weapons (Useful) ────────────────────────────────────────
    "QuickSword":           (0x0200, USFL, DLC_BASE),
    "RevengeSword":         (0x0201, USFL, DLC_BASE),
    "BackStabber":          (0x0202, USFL, DLC_BASE),
    "Bleeder":              (0x0203, USFL, DLC_BASE),
    "DualDaggers":          (0x0204, USFL, DLC_BASE),
    "BroadSword":           (0x0205, USFL, DLC_BASE),
    "Shovel":               (0x0206, PROG, DLC_BASE),
    "EvilSword":            (0x0207, USFL, DLC_BASE),
    "BleedCrit":            (0x0208, USFL, DLC_BASE),
    "SpeedBlade":           (0x0209, USFL, DLC_BASE),
    "GiantKiller":          (0x020A, USFL, DLC_RISE_OF_GIANT),
    "BulletBlade":          (0x020B, USFL, DLC_BASE),
    "SismicBlade":          (0x020C, USFL, DLC_BASE),
    "Spear":                (0x020D, USFL, DLC_BASE),
    "ImpaleSpear":          (0x020E, USFL, DLC_BASE),
    "KingsSpear":           (0x020F, USFL, DLC_BASE),
    "Rapier":               (0x0210, USFL, DLC_BASE),
    "DashSword":            (0x0211, USFL, DLC_BASE),
    "StunMace":             (0x0212, USFL, DLC_BASE),
    "BumpBoots":            (0x0213, USFL, DLC_BASE),
    "SpikedBoots":          (0x0214, USFL, DLC_BASE),
    "MultiKickBoots":       (0x0215, PROG, DLC_BASE),
    "QuickFists":           (0x0216, USFL, DLC_BASE),
    "Whip":                 (0x0217, USFL, DLC_BASE),
    "HookWhip":             (0x0218, USFL, DLC_BASE),
    "OilSword":             (0x0219, USFL, DLC_BASE),
    "Burner":               (0x021A, USFL, DLC_BASE),
    "LowHealth":            (0x021B, USFL, DLC_BASE),
    "PerfectHalberd":       (0x021C, USFL, DLC_BASE),
    "BehemothHammer":       (0x021D, USFL, DLC_BASE),
    "TentacleWhip":         (0x021E, USFL, DLC_BASE),
    "Pan":                  (0x021F, USFL, DLC_BASE),
    "ParryBlade":           (0x0220, USFL, DLC_BAD_SEED),
    "TickScytheLeft":       (0x0221, USFL, DLC_BAD_SEED),
    "RhythmicBlade":        (0x0222, USFL, DLC_BAD_SEED),
    "Crowbar":              (0x0223, USFL, DLC_BASE),
    "SnakeFang":            (0x0224, USFL, DLC_FATAL_FALLS),
    "GiantStaff":           (0x0225, USFL, DLC_FATAL_FALLS),
    "Lantern":              (0x0226, USFL, DLC_FATAL_FALLS),
    "Katana":               (0x0227, PROG, DLC_BASE),
    "Tombstone":            (0x0228, USFL, DLC_BASE),
    "HeavyAxe":             (0x0229, USFL, DLC_BASE),
    "Club":                 (0x022A, USFL, DLC_RISE_OF_GIANT),
    "MachetePistol":        (0x022B, USFL, DLC_BASE),
    "HardLightSword":       (0x022C, PROG, DLC_BASE),
    "PureNail":             (0x022D, PROG, DLC_BASE),
    "SkulBone":             (0x022E, USFL, DLC_BASE),
    "Trident":              (0x022F, USFL, DLC_QUEEN_AND_SEA),
    "HandHook":             (0x0230, USFL, DLC_QUEEN_AND_SEA),
    "Shark":                (0x0231, USFL, DLC_QUEEN_AND_SEA),
    "ElbowBlades":          (0x0232, USFL, DLC_QUEEN_AND_SEA),
    "WreckingBall":         (0x0233, USFL, DLC_QUEEN_AND_SEA),
    "QueenRapier":          (0x0234, USFL, DLC_QUEEN_AND_SEA),
    "CupidityDagger":       (0x0235, USFL, DLC_BASE),
    "GoldDigger":           (0x0236, USFL, DLC_BASE),
    "KingScepter":          (0x0237, USFL, DLC_BASE),
    "BaseballBat":          (0x0238, PROG, DLC_BASE),
    "NunchuckPan":          (0x0239, USFL, DLC_BASE),
    "Starfury":             (0x023A, USFL, DLC_BASE),
    "TPSword":              (0x023B, USFL, DLC_PURPLE),
    "WiggleWhip":           (0x023C, USFL, DLC_PURPLE),
    "Bible":                (0x023D, USFL, DLC_PURPLE),
    "SnakeSwordWeapon":     (0x023E, USFL, DLC_PURPLE),
    "VampireKiller":        (0x023F, USFL, DLC_PURPLE),
    "AdeleScythe":          (0x0240, USFL, DLC_PURPLE),
    "Scissor":              (0x0241, USFL, DLC_BASE),
    "Comb":                 (0x0242, USFL, DLC_BASE),
    "Misericord":           (0x0243, USFL, DLC_BASE),

    # ── Ranged Weapons (Useful) ───────────────────────────────────────
    "DualBow":              (0x0300, USFL, DLC_BASE),
    "InfiniteBow":          (0x0301, USFL, DLC_BASE),
    "LongBow":              (0x0302, USFL, DLC_BASE),
    "SonicCrossbow":        (0x0303, USFL, DLC_RISE_OF_GIANT),
    "CloseCombatBow":       (0x0304, USFL, DLC_BASE),
    "FastBow":              (0x0305, USFL, DLC_BASE),
    "FrostBow":             (0x0306, USFL, DLC_BASE),
    "CrossBow":             (0x0307, USFL, DLC_BASE),
    "MultiCrossBow":        (0x0308, USFL, DLC_BASE),
    "FrostCrossBow":        (0x0309, USFL, DLC_BASE),
    "ExplosiveCrossBow":    (0x030A, USFL, DLC_BASE),
    "AlchemicGun":          (0x030B, USFL, DLC_BASE),
    "Boomerang":            (0x030C, USFL, DLC_BASE),
    "BleedAxe":             (0x030D, USFL, DLC_RISE_OF_GIANT),
    "GodAxe":               (0x030E, USFL, DLC_RISE_OF_GIANT),
    "ThrowingSpear":        (0x030F, USFL, DLC_RISE_OF_GIANT),
    "MarkBow":              (0x0310, USFL, DLC_BASE),
    "PreciseBow":           (0x0311, USFL, DLC_BASE),
    "ThrowingKnife":        (0x0312, USFL, DLC_BASE),
    "LightningWhip":        (0x0313, USFL, DLC_BASE),
    "ThrowingTorch":        (0x0314, USFL, DLC_BASE),
    "ThrowingIce":          (0x0315, USFL, DLC_BASE),
    "FireBall":             (0x0316, USFL, DLC_BASE),
    "Lightning":            (0x0317, USFL, DLC_BASE),
    "FlameThrower":         (0x0318, USFL, DLC_BASE),
    "Freeze":               (0x0319, USFL, DLC_BASE),
    "MagicSalve":           (0x031A, USFL, DLC_RISE_OF_GIANT),
    "Blowgun":              (0x031B, USFL, DLC_BAD_SEED),
    "BarrelLauncher":       (0x031C, USFL, DLC_BASE),
    "ThrowingCards":        (0x031D, USFL, DLC_QUEEN_AND_SEA),
    "HeavyBow":             (0x031E, USFL, DLC_QUEEN_AND_SEA),
    "MoneyShooter":         (0x031F, USFL, DLC_BASE),
    "MagicBow":             (0x0320, USFL, DLC_BASE),
    "ThrowableStuff":       (0x0321, USFL, DLC_BASE),
    "LaserGlaive":          (0x0322, USFL, DLC_BASE),
    "HydraSpell":           (0x0323, USFL, DLC_BASE),
    "Cross":                (0x0324, USFL, DLC_PURPLE),
    "ThrowingAxe":          (0x0325, USFL, DLC_PURPLE),
    "MedusaHead":           (0x0326, USFL, DLC_PURPLE),
    "Anathema":             (0x0327, USFL, DLC_BASE),

    # ── Shields (Useful) ──────────────────────────────────────────────
    "WarriorShield":        (0x0400, USFL, DLC_BASE),
    "Shield":               (0x0401, USFL, DLC_BASE),
    "AreaShield":           (0x0402, USFL, DLC_BASE),
    "BumpShield":           (0x0403, USFL, DLC_BASE),
    "Rampart":              (0x0404, USFL, DLC_BASE),
    "DashShield":           (0x0405, USFL, DLC_BASE),
    "BloodShield":          (0x0406, USFL, DLC_BASE),
    "GreedShield":          (0x0407, USFL, DLC_BASE),
    "SpikeShield":          (0x0408, USFL, DLC_BASE),
    "ParryShield":          (0x0409, USFL, DLC_BASE),
    "HoldShield":           (0x040A, USFL, DLC_BASE),
    "ThunderShield":        (0x040B, USFL, DLC_RISE_OF_GIANT),
    "IceShield":            (0x040C, USFL, DLC_BASE),
    "AlucardShield":        (0x040D, USFL, DLC_PURPLE),

    # ── Powers / Skills (Useful) ──────────────────────────────────────
    "SlowOrb":              (0x0500, USFL, DLC_BASE),
    "Tornado":              (0x0501, USFL, DLC_BASE),
    "KnivesCircle":         (0x0502, USFL, DLC_BASE),
    "DamageBuff":           (0x0503, USFL, DLC_BASE),
    "LeechBuff":            (0x0504, USFL, DLC_BASE),
    "ExtraHeal":            (0x0505, USFL, DLC_BASE),
    "Hook":                 (0x0506, USFL, DLC_BASE),
    "BackBlink":            (0x0507, USFL, DLC_BASE),
    "ToxicCloud":           (0x0508, USFL, DLC_BASE),
    "DamageAura":           (0x0509, USFL, DLC_BASE),
    "Shockwave":            (0x050A, USFL, DLC_BASE),
    "Wings":                (0x050B, USFL, DLC_BASE),
    "Owl":                  (0x050C, USFL, DLC_BASE),
    "Dash":                 (0x050D, USFL, DLC_BASE),
    "GiantWhistle":         (0x050E, USFL, DLC_BASE),
    "SeismicStomp":         (0x050F, USFL, DLC_BASE),
    "CollectorSpin":        (0x0510, USFL, DLC_BASE),
    "SmokeBomb":            (0x0511, USFL, DLC_BAD_SEED),
    "SpawnFriendlyHardy":   (0x0512, PROG, DLC_BAD_SEED),
    "IceArmor":             (0x0513, USFL, DLC_BASE),
    "LightningRod":         (0x0514, USFL, DLC_FATAL_FALLS),
    "GardenerSickles":      (0x0515, USFL, DLC_FATAL_FALLS),
    "FlyingSword":          (0x0516, USFL, DLC_FATAL_FALLS),
    "BubbleShieldPower":    (0x0517, USFL, DLC_FATAL_FALLS),
    "FaceFlask":            (0x0518, PROG, DLC_BASE),
    "PolloPower":           (0x0519, USFL, DLC_BASE),
    "SpawnLilStaphy":       (0x051A, USFL, DLC_QUEEN_AND_SEA),
    "DiverseDeckJuggernaut":(0x051B, USFL, DLC_BASE),
    "Taunt":                (0x051C, USFL, DLC_BASE),
    "BouncingStone":        (0x051D, USFL, DLC_PURPLE),
    "SpawnCat":             (0x051E, USFL, DLC_PURPLE),
    "BatVolley":            (0x051F, USFL, DLC_PURPLE),
    "Indulgence":           (0x0520, USFL, DLC_BASE),

    # ── Grenades (Useful) ─────────────────────────────────────────────
    "ExplosiveGrenade":     (0x0600, USFL, DLC_BASE),
    "FastGrenade":          (0x0601, USFL, DLC_BASE),
    "ClusterBomb":          (0x0602, USFL, DLC_BASE),
    "MagnetGrenade":        (0x0603, USFL, DLC_BASE),
    "StunningGrenade":      (0x0604, USFL, DLC_BASE),
    "IceBomb":              (0x0605, USFL, DLC_BASE),
    "FireBomb":             (0x0606, USFL, DLC_BASE),
    "RootBomb":             (0x0607, USFL, DLC_BASE),
    "OilBomb":              (0x0608, USFL, DLC_BASE),
    "SideBomb":             (0x0609, USFL, DLC_BASE),
    "HolyWater":            (0x060A, USFL, DLC_PURPLE),

    # ── Deployed Traps (Useful) ───────────────────────────────────────
    "HorizontalTurret":     (0x0700, USFL, DLC_BASE),
    "StandardTurret":       (0x0701, USFL, DLC_BASE),
    "HeavyTurret":          (0x0702, USFL, DLC_BASE),
    "CeilTurret":           (0x0703, USFL, DLC_BASE),
    "FireTurret":           (0x0704, USFL, DLC_BASE),
    "GroundSaw":            (0x0705, USFL, DLC_BASE),
    "RootTrap":             (0x0706, USFL, DLC_BASE),
    "Crusher":              (0x0707, USFL, DLC_BASE),
    "Decoy":                (0x0708, USFL, DLC_BASE),
    "PortableDoor":         (0x0709, USFL, DLC_BASE),
    "TeslaCoil":            (0x070A, USFL, DLC_BASE),
    "Cannon":               (0x070B, USFL, DLC_QUEEN_AND_SEA),

    # ── Perks (Useful) ────────────────────────────────────────────────
    "P_CDR_Kill":           (0x0800, USFL, DLC_BASE),
    "P_DmgKill":            (0x0801, USFL, DLC_BASE),
    "P_DmgRevenge":         (0x0802, USFL, DLC_BASE),
    "P_ManyMobsAround":     (0x0803, USFL, DLC_BASE),
    "P_Bleed":              (0x0804, USFL, DLC_BASE),
    "P_CorruptedHealing":   (0x0805, USFL, DLC_BASE),
    "P_DodgeHeal":          (0x0806, USFL, DLC_BASE),
    "P_SpeedHeal":          (0x0807, USFL, DLC_BASE),
    "P_DmgSkl":             (0x0808, USFL, DLC_BASE),
    "P_DmgFirstHit":        (0x0809, USFL, DLC_BASE),
    "P_InvisibilityOnKill": (0x080A, USFL, DLC_BASE),
    "P_Backpack_Melee":     (0x080B, USFL, DLC_BASE),
    "P_DeployedDmg":        (0x080C, USFL, DLC_BASE),
    "P_DeathBomb":          (0x080D, USFL, DLC_BASE),
    "P_NoMobAround":        (0x080E, USFL, DLC_BASE),
    "P_AmmoOnHit":          (0x080F, USFL, DLC_BASE),
    "P_DmgSkillRanged":     (0x0810, USFL, DLC_BASE),
    "P_DmgPlantedArrow":    (0x0811, USFL, DLC_BASE),
    "P_DmgNearRanged":      (0x0812, USFL, DLC_BASE),
    "P_ShareDamage":        (0x0813, USFL, DLC_BASE),
    "P_Caltrops":           (0x0814, USFL, DLC_BASE),
    "P_DodgeSlow":          (0x0815, USFL, DLC_BASE),
    "P_CDR_Distance":       (0x0816, USFL, DLC_BASE),
    "P_Backpack_Ranged":    (0x0817, USFL, DLC_BASE),
    "P_ScaledHealth":       (0x0818, USFL, DLC_BASE),
    "P_DeathShield":        (0x0819, USFL, DLC_BASE),
    "P_CDR_Parry":          (0x081A, USFL, DLC_BASE),
    "P_DmgParry":           (0x081B, USFL, DLC_BASE),
    "P_HealOnParry":        (0x081C, USFL, DLC_BASE),
    "P_HealOnKill":         (0x081D, USFL, DLC_BASE),
    "P_Hot":                (0x081E, USFL, DLC_BASE),
    "P_Food":               (0x081F, USFL, DLC_BASE),
    "P_SuperParry":         (0x0820, USFL, DLC_BASE),
    "P_CDR_locked":         (0x0821, USFL, DLC_BASE),
    "P_AttackSpeed_Combo":  (0x0822, USFL, DLC_BASE),
    "P_Backpack_Shield":    (0x0823, USFL, DLC_BASE),
    "P_Yolo":               (0x0824, USFL, DLC_BASE),
    "P_ColdDmg":            (0x0825, USFL, DLC_BASE),
    "P_Rally":              (0x0826, USFL, DLC_BASE),
    "P_QuickHeal":          (0x0827, USFL, DLC_BASE),
    "P_SpeedBuff":          (0x0828, USFL, DLC_BASE),
    "P_Health":             (0x0829, USFL, DLC_BASE),
    "P_Curse":              (0x082A, USFL, DLC_BASE),
    "P_EasierCurse":        (0x082B, USFL, DLC_BASE),
    "P_Traps":              (0x082C, USFL, DLC_BASE),
    "P_Disengage":          (0x082D, USFL, DLC_BASE),
    "P_Execute_LowHealth":  (0x082E, USFL, DLC_BASE),
    "P_CDR_Crit":           (0x082F, USFL, DLC_BASE),
    "P_Ammo":               (0x0830, USFL, DLC_BASE),
    "P_U28_PerkGoldShield": (0x0831, USFL, DLC_BASE),
    "P_U28_PerkGoldSpeed":  (0x0832, USFL, DLC_BASE),
    "P_U28_PerkGoldPerDamage": (0x0833, USFL, DLC_BASE),
    "P_Wishes":             (0x0834, USFL, DLC_BASE),
    "P_CursedFlask":        (0x0835, USFL, DLC_BASE),
    "P_DamnedVigor":        (0x0836, USFL, DLC_BASE),
    "P_DemonicForce":       (0x0837, USFL, DLC_BASE),

    # ── Aspects (Useful) ──────────────────────────────────────────────
    "ASP_BloodDrinker":     (0x0900, USFL, DLC_BASE),
    "ASP_Stomper":          (0x0901, USFL, DLC_BASE),
    "ASP_Shatter":          (0x0902, USFL, DLC_BASE),
    "ASP_ToxinLover":       (0x0903, USFL, DLC_BASE),
    "ASP_Berzerker":        (0x0904, USFL, DLC_BASE),
    "ASP_GottaGoFast":      (0x0905, USFL, DLC_BASE),
    "ASP_Tinker":           (0x0906, USFL, DLC_BASE),
    "ASP_Firestarter":      (0x0907, USFL, DLC_BASE),
    "ASP_Menagerie":        (0x0908, USFL, DLC_BASE),
    "ASP_Grenadier":        (0x0909, USFL, DLC_BASE),
    "ASP_Superconductor":   (0x090A, USFL, DLC_BASE),
    "ASP_Assassin":         (0x090B, USFL, DLC_BASE),
    "ASP_Damned":           (0x090C, USFL, DLC_BASE),

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
    "PrisonerGold":         (0x1200, USFL, DLC_BASE),
    "PrisonerSonGoku":      (0x1201, USFL, DLC_BASE),
    "PrisonerBlack":        (0x1202, USFL, DLC_BASE),
    "PrisonerGhost":        (0x1203, USFL, DLC_BASE),
    "PrisonerSewers":       (0x1204, USFL, DLC_BASE),
    "PrisonerSanta":        (0x1205, USFL, DLC_RISE_OF_GIANT),
    "PrisonerStilt":        (0x1206, USFL, DLC_BASE),
    "PrisonerSkeleton":     (0x1207, USFL, DLC_BASE),
    "PrisonerCarduus":      (0x1208, USFL, DLC_BASE),
    "PrisonerAphrodite":    (0x1209, USFL, DLC_BASE),
    "PrisonerShaman":       (0x120A, USFL, DLC_BASE),
    "PrisonerCloud":        (0x120B, USFL, DLC_BASE),
    "PrisonerHyperlight":   (0x120C, USFL, DLC_BASE),
    "PrisonerAladdin":      (0x120D, USFL, DLC_BASE),
    "PrisonerBison":        (0x120E, USFL, DLC_BASE),
    "PrisonerWarrior":      (0x120F, USFL, DLC_BASE),
    "PrisonerMage":         (0x1210, USFL, DLC_BASE),
    "PrisonerNeon":         (0x1211, USFL, DLC_BASE),
    "PrisonerBobby":        (0x1212, USFL, DLC_BASE),
    "PrisonerDemon":        (0x1213, USFL, DLC_BASE),
    "PrisonerSylvanian":    (0x1214, USFL, DLC_BASE),
    "PrisonerSand":         (0x1215, USFL, DLC_BASE),
    "PrisonerGOG":          (0x1216, USFL, DLC_BASE),
    "PrisonerFrench":       (0x1217, USFL, DLC_BASE),
    "PrisonerXmas":         (0x1218, USFL, DLC_BASE),
    "PrisonerGardener":     (0x1219, USFL, DLC_BAD_SEED),
    "PrisonerFriendlyHardy":(0x121A, USFL, DLC_BAD_SEED),
    "PrisonerMushroom":     (0x121B, USFL, DLC_BAD_SEED),
    "PrisonerFugitive":     (0x121C, USFL, DLC_BAD_SEED),
    "PrisonerBlowgunner":   (0x121D, USFL, DLC_BAD_SEED),
    "PrisonerTick":         (0x121E, USFL, DLC_BAD_SEED),
    "RoyalGardener":        (0x121F, USFL, DLC_BAD_SEED),
    "PrisonerRetro":        (0x1220, USFL, DLC_BASE),
    "FreemanSkin":          (0x1221, USFL, DLC_BASE),
    "PrisonerJavelinSnake": (0x1222, USFL, DLC_FATAL_FALLS),
    "PrisonerNecromant":    (0x1223, USFL, DLC_FATAL_FALLS),
    "PrisonerBootleg":      (0x1224, USFL, DLC_FATAL_FALLS),
    "PrisonerKamikaze":     (0x1225, USFL, DLC_BASE),
    "PrisonerCrossbowMan":  (0x1226, USFL, DLC_BASE),
    "PrisonerKillBill":     (0x1227, USFL, DLC_BASE),
    "KingDefault":          (0x1228, USFL, DLC_BASE),
    "KingWhite":            (0x1229, USFL, DLC_BASE),
    "BehemothDefault":      (0x122A, USFL, DLC_BASE),
    "Behemoth1":            (0x122B, USFL, DLC_BASE),
    "Behemoth2":            (0x122C, USFL, DLC_BASE),
    "Behemoth3":            (0x122D, USFL, DLC_BASE),
    "Behemoth4":            (0x122E, USFL, DLC_BASE),
    "BeholderDefault":      (0x122F, USFL, DLC_BASE),
    "Beholder1":            (0x1230, USFL, DLC_BASE),
    "Beholder2":            (0x1231, USFL, DLC_BASE),
    "Beholder3":            (0x1232, USFL, DLC_BASE),
    "Beholder4":            (0x1233, USFL, DLC_BASE),
    "AssassinDefault":      (0x1234, USFL, DLC_BASE),
    "Assassin1":            (0x1235, USFL, DLC_BASE),
    "Assassin2":            (0x1236, USFL, DLC_BASE),
    "Assassin3":            (0x1237, USFL, DLC_BASE),
    "Assassin4":            (0x1238, USFL, DLC_BASE),
    "GiantDefault":         (0x1239, USFL, DLC_RISE_OF_GIANT),
    "Giant1":               (0x123A, USFL, DLC_RISE_OF_GIANT),
    "Giant2":               (0x123B, USFL, DLC_RISE_OF_GIANT),
    "Giant3":               (0x123C, USFL, DLC_RISE_OF_GIANT),
    "Giant4":               (0x123D, USFL, DLC_RISE_OF_GIANT),
    "HotkDefault":          (0x123E, USFL, DLC_BASE),
    "Hotk1":                (0x123F, USFL, DLC_BASE),
    "Hotk2":                (0x1240, USFL, DLC_BASE),
    "Hotk3":                (0x1241, USFL, DLC_BASE),
    "Hotk4":                (0x1242, USFL, DLC_BASE),
    "Statue":               (0x1243, USFL, DLC_FATAL_FALLS),
    "CollectorDefault":     (0x1244, USFL, DLC_BASE),
    "TickDefault":          (0x1245, USFL, DLC_BAD_SEED),
    "Tick1":                (0x1246, USFL, DLC_BAD_SEED),
    "Tick2":                (0x1247, USFL, DLC_BAD_SEED),
    "Tick3":                (0x1248, USFL, DLC_BAD_SEED),
    "Tick4":                (0x1249, USFL, DLC_BAD_SEED),
    "TickSacrifice":        (0x124A, USFL, DLC_BAD_SEED),
    "GardenerDefault":      (0x124B, USFL, DLC_FATAL_FALLS),
    "Gardener1":            (0x124C, USFL, DLC_FATAL_FALLS),
    "Gardener2":            (0x124D, USFL, DLC_FATAL_FALLS),
    "Gardener3":            (0x124E, USFL, DLC_FATAL_FALLS),
    "Gardener4":            (0x124F, USFL, DLC_FATAL_FALLS),
    "Cultist":              (0x1250, PROG, DLC_FATAL_FALLS),
    "FlawlessBehemoth":     (0x1251, USFL, DLC_BASE),
    "FlawlessBeholder":     (0x1252, USFL, DLC_BASE),
    "FlawlessAssassin":     (0x1253, USFL, DLC_BASE),
    "FlawlessGiant":        (0x1254, USFL, DLC_RISE_OF_GIANT),
    "FlawlessHotk":         (0x1255, USFL, DLC_BASE),
    "FlawlessTick":         (0x1256, USFL, DLC_BAD_SEED),
    "FlawlessGardener":     (0x1257, USFL, DLC_FATAL_FALLS),
    "Snowman":              (0x1258, USFL, DLC_BASE),
    "SantaKLOS":            (0x1259, USFL, DLC_BASE),
    "HollowKnight":         (0x125A, USFL, DLC_BASE),
    "Blasphemous":          (0x125B, USFL, DLC_BASE),
    "Guacamelee":           (0x125C, USFL, DLC_BASE),
    "Skul":                 (0x125D, USFL, DLC_BASE),
    "HyperLightDrifter":    (0x125E, USFL, DLC_BASE),
    "CurseofTheDeadGods":   (0x125F, USFL, DLC_BASE),
    "SoulKnight":           (0x1260, USFL, DLC_BASE),
    "Staphy":               (0x1261, USFL, DLC_QUEEN_AND_SEA),
    "ANCHORGUY":            (0x1262, USFL, DLC_QUEEN_AND_SEA),
    "ServanteDefault":      (0x1263, USFL, DLC_QUEEN_AND_SEA),
    "Servante1":            (0x1264, USFL, DLC_QUEEN_AND_SEA),
    "Servante2":            (0x1265, USFL, DLC_QUEEN_AND_SEA),
    "Servante3":            (0x1266, USFL, DLC_QUEEN_AND_SEA),
    "Servante4":            (0x1267, USFL, DLC_QUEEN_AND_SEA),
    "FlawlessServante":     (0x1268, USFL, DLC_QUEEN_AND_SEA),
    "QueenDefault":         (0x1269, USFL, DLC_QUEEN_AND_SEA),
    "Queen1":               (0x126A, USFL, DLC_QUEEN_AND_SEA),
    "Queen2":               (0x126B, USFL, DLC_QUEEN_AND_SEA),
    "Queen3":               (0x126C, USFL, DLC_QUEEN_AND_SEA),
    "Queen4":               (0x126D, USFL, DLC_QUEEN_AND_SEA),
    "FlawlessQueen":        (0x126E, USFL, DLC_QUEEN_AND_SEA),
    "BlueErinaceus":        (0x126F, USFL, DLC_QUEEN_AND_SEA),
    "Banker":               (0x1270, USFL, DLC_BASE),
    "GuillainThief":        (0x1271, USFL, DLC_BASE),
    "Bobby":                (0x1272, USFL, DLC_BASE),
    "ShovelKnight":         (0x1273, USFL, DLC_BASE),
    "HotlineMiamiChicken":  (0x1274, USFL, DLC_BASE),
    "KatanaZero":           (0x1275, USFL, DLC_BASE),
    "RiskOfRain":           (0x1276, USFL, DLC_BASE),
    "Terraria":             (0x1277, USFL, DLC_BASE),
    "SlayTheSpire":         (0x1278, USFL, DLC_BASE),
    "Mentor":               (0x1279, USFL, DLC_BASE),
    "Mentor1":              (0x127A, USFL, DLC_BASE),
    "Mentor2":              (0x127B, USFL, DLC_BASE),
    "Mentor3":              (0x127C, USFL, DLC_BASE),
    "VictoriusBeheaded":    (0x127D, USFL, DLC_BASE),
    "VictoriusBeheaded1":   (0x127E, USFL, DLC_BASE),
    "VictoriusBeheaded2":   (0x127F, USFL, DLC_BASE),
    "VictoriusBeheaded3":   (0x1280, USFL, DLC_BASE),
    "Simon":                (0x1281, USFL, DLC_PURPLE),
    "Alucard":              (0x1282, USFL, DLC_PURPLE),
    "RichterROB":           (0x1283, USFL, DLC_PURPLE),
    "Sypha":                (0x1284, USFL, DLC_PURPLE),
    "Trevor":               (0x1285, USFL, DLC_PURPLE),
    "Maria":                (0x1286, USFL, DLC_PURPLE),
    "Hector":               (0x1287, USFL, DLC_PURPLE),
    "HauntedArmor":         (0x1288, USFL, DLC_PURPLE),
    "AdeleDefault":         (0x1289, USFL, DLC_PURPLE),
    "Adele1":               (0x128A, USFL, DLC_PURPLE),
    "Adele2":               (0x128B, USFL, DLC_PURPLE),
    "Adele3":               (0x128C, USFL, DLC_PURPLE),
    "Adele4":               (0x128D, USFL, DLC_PURPLE),
    "FlawlessAdele":        (0x128E, USFL, DLC_PURPLE),
    "DookuDefault":         (0x128F, USFL, DLC_PURPLE),
    "Dooku1":               (0x1290, USFL, DLC_PURPLE),
    "Dooku2":               (0x1291, USFL, DLC_PURPLE),
    "Dooku3":               (0x1292, USFL, DLC_PURPLE),
    "Dooku4":               (0x1293, USFL, DLC_PURPLE),
    "FlawlessDooku":        (0x1294, USFL, DLC_PURPLE),

    # ── Head cosmetics / Fillers ──────────────────────────────────────
    "BobbyFlame":           (0x1400, USFL, DLC_BASE),
    "ConciergeFlame":       (0x1401, USFL, DLC_BASE),
    "ConjunctiviusHead":    (0x1402, USFL, DLC_BASE),
    "MamaTickEye":          (0x1403, USFL, DLC_BASE),
    "TimeKeeperHat":        (0x1404, USFL, DLC_BASE),
    "GiantFlame":           (0x1405, USFL, DLC_BASE),
    "ScarecrowHat":         (0x1406, USFL, DLC_BASE),
    "HandOfTheKingFlame":   (0x1407, USFL, DLC_BASE),
    "ServantsMask":         (0x1408, USFL, DLC_BASE),
    "QueenFlame":           (0x1409, USFL, DLC_BASE),
    "CollectorHood":        (0x140A, USFL, DLC_BASE),
    "BlackHole":            (0x140B, USFL, DLC_BASE),
    "BlackHoleWhite":       (0x140C, USFL, DLC_BASE),
    "BlackHoleViolet":      (0x140D, USFL, DLC_BASE),
    "BlackHoleRed":         (0x140E, USFL, DLC_BASE),
    "BlackHoleGreen":       (0x140F, USFL, DLC_BASE),
    "BlackHoleBlue":        (0x1410, USFL, DLC_BASE),
    "Bitter":               (0x1411, USFL, DLC_BASE),
    "VortexHelloDarkness":  (0x1412, USFL, DLC_BASE),
    "VortexBadSeed":        (0x1413, USFL, DLC_BASE),
    "VortexAndSea":         (0x1414, USFL, DLC_BASE),
    "VortexFoundry":        (0x1415, USFL, DLC_BASE),
    "Guillain":             (0x1416, USFL, DLC_BASE),
    "Pecheur":              (0x1417, USFL, DLC_BASE),
    "StaphyHead":           (0x1418, USFL, DLC_BASE),
    "Flawless":             (0x1419, USFL, DLC_BASE),
    "CellHead":             (0x141A, USFL, DLC_BASE),
    "EvilEmpire":           (0x141B, USFL, DLC_BASE),
    "BlobbyFlame":          (0x141C, USFL, DLC_BASE),
    "GlitchyHead":          (0x141D, USFL, DLC_BASE),
    "MushroomBoi":          (0x141E, USFL, DLC_BASE),
    "HordesZeroHood":       (0x141F, USFL, DLC_BASE),
    "BlobbyFlameMagma":     (0x1420, USFL, DLC_BASE),
    "BlobbyFlameMalaise":   (0x1421, USFL, DLC_BASE),
    "BlobbyFlameGum":       (0x1422, USFL, DLC_BASE),
    "GlitchyHeadDeepSpace": (0x1423, USFL, DLC_BASE),
    "GlitchyHeadRed":       (0x1424, USFL, DLC_BASE),
    "BlowTorchBlack":       (0x1425, USFL, DLC_BASE),
    "BlowTorch":            (0x1426, USFL, DLC_BASE),
    "BlowTorchGold":        (0x1427, USFL, DLC_BASE),
    "BlowTorchRed":         (0x1428, USFL, DLC_BASE),
    "BossCellHead":         (0x1429, USFL, DLC_BASE),

    # ── AP Trap Items ─────────────────────────────────────────────────
    # These are sent to the Dead Cells player to hinder them mid-run.
    # The mod handles their in-game effect on the client side.
    "Trap_Curse":           (0x1500, TRAP, DLC_BASE),
    "Trap_SpawnElite":      (0x1501, TRAP, DLC_BASE),
    "Trap_RemoveGold":      (0x1502, TRAP, DLC_BASE),
    "Trap_BreakWeapon":     (0x1503, TRAP, DLC_BASE),
    "Trap_InvertControls":  (0x1504, TRAP, DLC_BASE),
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


def get_filler_items(enabled_dlcs: Set[str]) -> Dict[str, tuple]:
    """Return all filler items for the given DLC set."""
    return {
        name: data
        for name, data in get_items_for_dlcs(enabled_dlcs).items()
        if data[1] == FILR
    }


def get_trap_items() -> Dict[str, tuple]:
    """Return all trap items (DLC-independent)."""
    return {name: data for name, data in ITEM_TABLE.items() if data[1] == TRAP}


def get_progression_items(enabled_dlcs: Set[str]) -> Dict[str, tuple]:
    """Return all progression items for the given DLC set."""
    return {
        name: data
        for name, data in get_items_for_dlcs(enabled_dlcs).items()
        if data[1] == PROG
    }


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
