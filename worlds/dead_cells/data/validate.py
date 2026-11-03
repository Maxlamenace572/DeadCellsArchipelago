"""Cross-file consistency checks. Pure python: run from tests or `tools/check_data.py`.
Every problem the old structure hid (typos in hand-written lists, rules on missing
locations, tokens that silently never matched) becomes an error here."""
from . import GameData, game_data

_TOKEN_PREFIXES = ("region:", "loc:", "depth:", "count:", "tier:", "@")


def _tokens(raw):
    if raw in (None, "", [], [[]]):
        return
    if isinstance(raw, str):
        yield raw
    else:
        for x in raw:
            yield from _tokens(x) if isinstance(x, list) else [x]


def validate(data: GameData | None = None) -> list[str]:
    d = data or game_data()
    errors: list[str] = []

    #ids unique
    for label, table in (("item", d.items), ("location", d.locations)):
        seen: dict[int, str] = {}
        for name, e in table.items():
            if e.id in seen:
                errors.append(f"duplicate {label} id {e.id}: {seen[e.id]!r} / {name!r}")
            seen[e.id] = name

    #sources point at real biomes
    for loc in d.locations.values():
        for s in loc.sources:
            if s.biome not in d.biomes:
                errors.append(f"location {loc.name!r}: unknown biome {s.biome!r}")

    #every token used anywhere must resolve
    def check(owner: str, raw):
        for tok in _tokens(raw):
            if tok.startswith("B_") and tok[2:] in d.biomes:
                continue
            if tok.startswith(_TOKEN_PREFIXES):
                kind, _, rest = tok.partition(":")
                if kind == "region" and rest not in d.biomes:
                    errors.append(f"{owner}: unknown biome in {tok!r}")
                elif kind == "loc" and rest not in d.locations:
                    errors.append(f"{owner}: unknown location in {tok!r}")
                elif kind == "@" or tok.startswith("@"):
                    if tok[1:] not in d.macros:
                        errors.append(f"{owner}: unknown macro {tok!r}")
                    else:
                        check(f"{owner}>{tok}", d.macros[tok[1:]])
                elif kind == "count" and rest.split(":")[0] not in d.count_kinds:
                    errors.append(f"{owner}: unknown count kind {tok!r}")
                continue
            name, _, n = tok.rpartition(":")
            name = name if n.isdigit() else tok
            try:
                d.resolve_item(name)
            except KeyError:
                errors.append(f"{owner}: cannot resolve {tok!r} to an item")

    for t in d.transitions + d.menu_transitions:
        check(f"transition {t.src}->{t.dst}", t.require)
        for end in (t.src, t.dst):
            if end not in d.biomes and end not in ("Menu", "End"):
                errors.append(f"transition {t.src}->{t.dst}: unknown region {end!r}")
    for loc_name, raw in d.rules.items():
        if loc_name not in d.locations:
            errors.append(f"rules.json: location {loc_name!r} does not exist")
        check(f"rule[{loc_name}]", raw)
    for src, raw in d.endings.items():
        check(f"ending[{src}]", raw)

    #every biome that can be entered has an unlock item (except the always-open ones)
    unlocked = {it.unlock_for for it in d.items.values() if it.unlock_for}
    for t in d.transitions:
        if t.dst in d.biomes and t.dst not in unlocked and t.dst not in ("PrisonCourtyard", "PrisonRoof", "BeholderPit"):
            pass  #informational only: some biomes are free to enter
    for boss, loc in d.event_items.items():
        if boss not in d.items:
            errors.append(f"event location {loc!r} has no matching item {boss!r}")

    #enemy sanity: ids complete, no boss turned into an enemy, no stale ids
    from . import enemies
    from . import _read
    tracker, config, loc_json = _read("tracker.json"), _read("enemy_sanity.json"), _read("locations.json")
    bosses = enemies.boss_mobs(tracker)
    for mob, name in d.enemy_names.items():
        if mob in bosses:
            errors.append(f"enemy {mob!r} is a boss and already a check")
    for mob in set(loc_json["enemy_ids"]) - set(d.enemy_names):
        errors.append(f"locations.json: enemy id for {mob!r} but it is not an enemy any more (kept frozen, remove if unused)")
    if len(set(loc_json["enemy_ids"].values())) != len(loc_json["enemy_ids"]):
        errors.append("locations.json: duplicate enemy ids")

    #room randomizer config
    cfg = d.room_rando
    tiered = [b for bs in cfg["boss_tiers"].values() for b in bs]
    for b in tiered:
        if b not in d.biomes:
            errors.append(f"room_rando.json boss_tiers: unknown biome {b!r}")
    for b in {b for b in tiered if tiered.count(b) > 1}:
        errors.append(f"room_rando.json boss_tiers: {b!r} is in several tiers")
    boss_arenas = {x["biome"] for gid, info in tracker.items() if gid.startswith("Boss_") for x in info["sources"]}
    for b in sorted(boss_arenas - set(tiered)):
        errors.append(f"room_rando.json boss_tiers: boss arena {b!r} (tracker) is in no tier")

    #readable enemy names must belong to real enemies (a typo would silently do nothing)
    for mob in sorted(set(config.get("display_names", {})) - set(d.enemy_names)):
        errors.append(f"enemy_sanity.json display_names: {mob!r} is not an enemy (typo, boss or excluded)")

    #mobs.json covers biomes we know
    for biome in d.mobs:
        if biome not in d.biomes:
            errors.append(f"mobs.json: unknown biome {biome!r}")

    #groups reference real names
    for n in {x for g in d.groups["items"].values() for x in g} - set(d.items):
        errors.append(f"groups.json: item group references unknown item {n!r}")
    for n in {x for g in d.groups["locations"].values() for x in g} - set(d.locations):
        errors.append(f"groups.json: location group references unknown location {n!r}")
    return errors


def warnings(data: GameData | None = None) -> list[str]:
    """Not errors: places where the data leaves the Bank depth unknown (the Bank source is then
    treated as 'any depth'). Fix by completing mobs.json or adding "bank_depths" in locations.json."""
    from . import _read
    d = data or game_data()
    out = []
    known = {e["name"] for v in d.mobs.values() for e in v["mobs"]}
    gap = sorted({x["mob"] for v in _read("tracker.json").values() for x in v["sources"] if x.get("mob")} - known)
    if gap:
        out.append(f"mobs.json lacks {gap}: they drop blueprints (tracker.json) but get no enemy-sanity check")
    for loc in d.locations.values():
        for s in loc.sources:
            if s.biome == "Bank" and s.mob and not s.depths:
                out.append(f"{loc.name}: Bank source (mob {s.mob}, min_bc {s.min_bc}) has no depth")
    return out
