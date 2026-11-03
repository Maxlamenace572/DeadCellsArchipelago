"""Plain, immutable records describing the game. No Archipelago imports on purpose,
so the data layer can be unit-tested (and reused by tools) without the framework."""
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass(frozen=True)
class Gate:
    """One way to obtain a location: reach one of `biomes` with `min_bc` Boss Cells and, for Bank
    sources, with a biome of one of `depths` reachable (the Bank replaces a biome of that depth)."""
    min_bc: int
    depths: tuple[int, ...]
    biomes: frozenset[str]


def gates_of(sources) -> list[Gate]:
    """The logic-relevant view of a list of sources (max_bc and mobs are ignored on purpose)."""
    out: dict[tuple, set[str]] = {}
    for s in sources:
        out.setdefault((s.min_bc, s.depths), set()).add(s.biome)
    return [Gate(bc, depths, frozenset(b)) for (bc, depths), b in sorted(out.items())]




@dataclass(frozen=True)
class Biome:
    id: str                     #game id, like "TopClockTower"
    ap_name: str                #display name, like "Clock Room"
    depth: Optional[int] = None
    dlc: str = ""
    min_bc: int = 0             #biome only exists if the goal BC is >= this


@dataclass(frozen=True)
class ItemDef:
    name: str
    id: int                     #offset from ITEM_BASE_ID
    classification: str         #progression / useful / filler / trap
    cat: str                    #rune, melee, skin, unlock, event
    dlc: str = ""
    start: str = ""             #"weapon" | "mutation": precollected when the matching option is off
    count: int = 1              #copies placed in the pool
    count_option: str = ""      #option name overriding `count` (Stem Cells -> boss_cells)
    unlock_for: str = ""        #biome id this item unlocks
    filler_pool: bool = False
    keep_without_cosmetics: bool = False


@dataclass(frozen=True)
class Source:
    """One place an item can be obtained. mob is None for floor drops."""
    biome: str
    min_bc: int = 0
    max_bc: int = 5             #informational only: logic never uses it (see notes)
    dlc: str = ""
    mob: Optional[str] = None
    depths: tuple[int, ...] = ()    #Bank only: depth(s) of the replaced biome (empty = unconstrained)


@dataclass(frozen=True)
class LocationDef:
    name: str
    id: int                     #offset from LOCATION_BASE_ID
    game_id: str
    type: str                   #blueprint_enemy, skin, rune, biome_enter, boss_defeat, ...
    dlc: str
    rarity: str
    sources: tuple[Source, ...]

    @property
    def gates(self) -> list[Gate]:
        return gates_of(self.sources)


@dataclass(frozen=True)
class Transition:
    src: str
    dst: str
    require: Any                #raw requirement, compiled later by logic.requirements
