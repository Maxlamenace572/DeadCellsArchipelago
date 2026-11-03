"""Enemy sanity data: one "Kill <enemy>" location per enemy of mobs.json.

Pure functions over the raw JSON so that tools/allocate_enemy_ids.py can use them before ids exist.
Bosses are NOT enemies here: they already are checks ("Boss_*" entries of tracker.json), and they are
derived from the tracker rather than listed by hand, so a new boss can't be forgotten.
"""
from .models import Source


def boss_mobs(tracker: dict) -> set[str]:
    return {s["mob"] for gid, info in tracker.items() if gid.startswith("Boss_")
            for s in info["sources"] if s.get("mob")}


def enemy_sources(tracker: dict, mobs: dict, biomes: dict, config: dict) -> dict[str, tuple[Source, ...]]:
    """{mob: sources}: every (biome, min_bc[, depths]) the enemy appears at, bosses and exclusions removed.
    Bank entries carry the depth(s) of the biome the Bank replaces (same meaning as for item sources)."""
    skip = boss_mobs(tracker) | set(config.get("exclude", []))
    out: dict[str, list[Source]] = {}
    for biome, entry in mobs.items():
        for e in entry["mobs"]:
            if e["name"] in skip:
                continue
            dlc = biomes[biome].get("dlc", "") if isinstance(biomes[biome], dict) else biomes[biome].dlc
            out.setdefault(e["name"], []).append(
                Source(biome=biome, min_bc=e["min_bc"], max_bc=e["max_bc"], dlc=dlc, mob=e["name"],
                       depths=tuple(sorted(e.get("depth", ())))))
    return {m: tuple(s) for m, s in sorted(out.items())}


def location_name(mob: str, config: dict) -> str:
    return f'{config.get("prefix", "Kill ")}{config.get("display_names", {}).get(mob, mob)}'
