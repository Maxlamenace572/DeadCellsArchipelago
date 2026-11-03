"""Loads every JSON file once and exposes it as typed records.

    from .data import game_data
    data = game_data()
    data.items["Vine Rune"], data.locations["Spider Rune"], data.transitions ...

Everything is resolved to Archipelago display names here, so the rest of the
world never touches raw game ids.
"""
import json
import pkgutil
from dataclasses import dataclass, field, replace
from functools import lru_cache
from typing import Any

from . import enemies
from .models import Biome, Gate, ItemDef, LocationDef, Source, Transition, gates_of

__all__ = ["GameData", "game_data", "Biome", "Gate", "ItemDef", "LocationDef", "Source", "Transition", "gates_of"]


def _read(name: str) -> Any:
    return json.loads(pkgutil.get_data(__package__, name).decode("utf-8"))


@dataclass
class GameData:
    game_ids: dict[str, str]
    biomes: dict[str, Biome]
    items: dict[str, ItemDef]
    locations: dict[str, LocationDef]
    transitions: list[Transition]                  # biome graph from regions.json (+ extras)
    menu_transitions: list[Transition]
    endings: dict[str, Any]                        # biome id -> requirement for "-> End"
    rules: dict[str, Any]                          # location name -> extra requirement
    macros: dict[str, Any]
    count_kinds: dict[str, list[str]]
    boss_tiers: dict[str, list[str]]
    event_items: dict[str, str]                    # "Death Defeated" -> "Death Defeat"
    mobs: dict[str, list[dict]]                    # mobs.json, untouched (enemy sanity)
    groups: dict[str, dict[str, list[str]]]
    true_ending: dict[str, Any]
    room_rando: dict = field(default_factory=dict)
    enemy_names: dict[str, str] = field(default_factory=dict)    # mob id -> "Kill <mob>" location name

    # ── name resolution ──────────────────────────────────────────────────────
    def ap_name(self, game_id: str) -> str:
        return self.game_ids.get(game_id, game_id)

    def count_excluded(self, kind: str) -> set[str]:
        """A location can't count itself: skip those whose own rule counts the same kind."""
        return {name for name, raw in self.rules.items() if f"count:{kind}:" in repr(raw)}

    def boss_location(self, boss_token: str) -> str:
        """'Boss_Death' -> 'Death' (the boss-kill location)."""
        return self.game_ids[boss_token]

    def resolve_item(self, token: str) -> str:
        """Game id or display name -> item name. Raises KeyError if unknown."""
        if token in self.items:
            return token
        if token.startswith("Boss_"):
            return self.game_ids["D_" + token[5:]].replace("Defeat", "Defeated")
        if token in self.biomes:
            return f"{self.biomes[token].ap_name} Unlock"
        mapped = self.game_ids.get(token)
        if mapped in self.items:
            return mapped
        raise KeyError(f"unknown item token {token!r}")


def _norm_sources(raw: list[dict], default_dlc: str = "") -> tuple[Source, ...]:
    return tuple(Source(biome=s["biome"], min_bc=s.get("min_bc", 0), max_bc=s.get("max_bc", 5),
                        dlc=s.get("dlc", default_dlc), mob=s.get("mob")) for s in raw)


def _with_bank_depths(sources: tuple[Source, ...], bank_mobs: list[dict], forced: list[int] | None) -> tuple[Source, ...]:
    """The Bank replaces a random biome, and its enemies depend on the depth of that biome.
    mobs.json["Bank"] lists, per enemy, the depth(s) it appears at. A Bank source becomes one Source
    per (min_bc, depths) variant so that the depth is only required *for the Bank source*.
    `forced` (locations.json overrides "bank_depths") wins over the data."""
    out: list[Source] = []
    for s in sources:
        if s.biome != "Bank":
            out.append(s)
            continue
        if forced:
            out.append(replace(s, depths=tuple(forced)))
            continue
        entries = [e for e in bank_mobs if e["name"] == s.mob]
        exact = [(e["min_bc"], e.get("depth")) for e in entries if e["min_bc"] == s.min_bc]
        # No exact entry (e.g. prisoner outfits): keep this source's min_bc, take the depths from the mob.
        variants = exact or [(max(s.min_bc, e["min_bc"]), e["depth"]) for e in entries if e.get("depth")]
        seen = set()
        for bc, depths in variants:
            key = (bc, tuple(sorted(depths or ())))
            if key not in seen:
                seen.add(key)
                out.append(replace(s, min_bc=bc, depths=key[1]))
        if not variants:
            out.append(s)
    return tuple(out)


def _build_locations(game_ids, biomes, tracker, mobs, loc_json) -> dict[str, LocationDef]:
    ids: dict[str, int] = loc_json["ids"]
    bank_mobs = mobs.get("Bank", {}).get("mobs", [])
    out: dict[str, LocationDef] = {}

    def add(name, game_id, type_, dlc, rarity, sources):
        if name not in ids:
            raise KeyError(f"location {name!r} has no frozen id in locations.json")
        patch = loc_json["overrides"].get(name, {})
        type_ = patch.get("type", type_)
        if "biome" in patch:
            sources = tuple(replace(s, biome=patch["biome"]) for s in sources)
        sources = _with_bank_depths(sources, bank_mobs, patch.get("bank_depths"))
        out[name] = LocationDef(name, ids[name], game_id, type_, dlc, rarity, sources)

    for gid, info in tracker.items():
        src = _norm_sources(info["sources"], info.get("dlc", ""))
        if info["type"] in ("biome_enter", "biome_exit"):
            side = "Enter" if info["type"] == "biome_enter" else "Exit"
            name = f"{biomes[src[0].biome].ap_name} {side}"
        else:
            name = game_ids.get(gid, gid)
        add(name, gid, info["type"], info.get("dlc", ""), info.get("rarity", ""), src)

    # "<Boss> Defeat" event locations: only exist in game_ids.json (D_ prefix).
    for gid, name in game_ids.items():
        if gid.startswith("D_"):
            boss = tracker["Boss_" + gid[2:]]
            src = (Source(biome=boss["sources"][0]["biome"], dlc=boss.get("dlc", "")),)
            add(name, gid, "boss_defeat", boss.get("dlc", ""), "", src)

    for name, e in loc_json["extra"].items():
        add(name, name, e["type"], e.get("dlc", ""), "", _norm_sources(e["sources"], e.get("dlc", "")))
    return out


def _add_enemy_locations(out, biomes, tracker, mobs, loc_json, config) -> dict[str, str]:
    """Enemy sanity locations (type "enemy"). They exist in the data package always; the option decides per seed."""
    names: dict[str, str] = {}
    sources = enemies.enemy_sources(tracker, mobs, biomes, config)
    for mob, srcs in sources.items():
        if mob not in loc_json["enemy_ids"]:
            raise KeyError(f"enemy {mob!r} (mobs.json) has no id in data/locations.json -> \"enemy_ids\". "
                           f"Run `python tools/allocate_enemy_ids.py` from the repo root, or add \"{mob}\": <next free id> "
                           f"by hand (ids are frozen: never reuse or change one).")
        name = enemies.location_name(mob, config)
        if name in out:
            raise KeyError(f"enemy location name {name!r} collides with an existing location")
        out[name] = LocationDef(name, loc_json["enemy_ids"][mob], mob, "enemy", "", "", srcs)
        names[mob] = name
    return names


def _transitions(raw: dict[str, list[dict]]) -> list[Transition]:
    return [Transition(src, e["to"], e.get("require"))
            for src, exits in raw.items() for e in exits if "to" in e]  #tolerates the stray {} entries


@lru_cache(maxsize=1)
def game_data() -> GameData:
    game_ids = _read("game_ids.json")
    tracker = _read("tracker.json")
    extra = _read("world_extra.json")
    rules = _read("rules.json")
    loc_json = _read("locations.json")

    biomes = {bid: Biome(bid, game_ids.get(bid, bid), b.get("depth"), b.get("dlc", ""), b.get("min_bc", 0))
              for bid, b in _read("biomes.json").items()}
    items = {name: ItemDef(name=name, id=e["id"], classification=e["class"], cat=e["cat"],
                           dlc=e.get("dlc", ""), start=e.get("start", ""), count=e.get("count", 1),
                           count_option=e.get("count_option", ""), unlock_for=e.get("unlock_for", ""),
                           filler_pool=e.get("filler_pool", False),
                           keep_without_cosmetics=e.get("keep_without_cosmetics", False))
             for name, e in _read("items.json").items()}
    mobs = _read("mobs.json")
    locations = _build_locations(game_ids, biomes, tracker, mobs, loc_json)
    enemy_names = _add_enemy_locations(locations, biomes, tracker, mobs, loc_json, _read("enemy_sanity.json"))

    graph = _transitions(_read("regions.json"))
    known = {(t.src, t.dst) for t in graph}
    graph += [t for t in _transitions(extra["extra_transitions"]) if (t.src, t.dst) not in known]
    menu = [Transition("Menu", e["to"], e["require"]) for e in extra["menu"]]
    event_items = {loc.replace("Defeat", "Defeated"): loc
                   for loc, d in locations.items() if d.type == "boss_defeat"}

    return GameData(game_ids, biomes, items, locations, graph, menu, extra["endings"], rules["locations"],
                    rules["macros"], rules["count_kinds"], rules["boss_tiers"], event_items,
                    mobs, _read("groups.json"), extra["true_ending_only_at_bc"], _read("room_rando.json"), enemy_names)
