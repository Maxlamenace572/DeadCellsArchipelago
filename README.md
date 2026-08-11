<h1>Dead Cells Archipelago</h1>

This is an [Archipelago](https://github.com/ArchipelagoMW/Archipelago) mod for Dead Cells, using [Dead Cells Core Modding](https://github.com/dead-cells-core-modding/core).

In its current state, this implementation is best suited for long sync or async games, as there are multiple situations where you can become blocked. For short sync, you should use advanced YAML parameters such as `start_inventory`, `exclude_locations`, etc.

## Setup

### Installer

For windows users, you can download the DeadCellsArchipelagoInstaller.zip from the latest release and launch the DeadCellsInstaller.exe. It will download dependencies (.net 10, DCCM), install the mod and launch the game in modded. You can update the mod or DCCM from the launcher, or launch without updating. If you have an ongoing game, you should check at the end of the release log if the new version is still compatible with your current apworld.

Note: This mod can be played with the Steam and GOG versions, and on the Goldberg emulator.

### Manual install

To set up this mod, you'll first need to follow the Core Modding installation guide. You’ll also need the [.net SDK 10](https://dotnet.microsoft.com/fr-fr/download/dotnet/10.0).

Then in the coremod directory you'll need to put the mods directory from the .zip of the latest release of DeadCellsArchipelago. In the end, the path should look like `Dead Cells\coremod\mods\DeadCellsArchipelago`.

If you want to launch the modded game, you'll find it at `Dead Cells\coremod\core\host\startup\DeadCellsModding.exe`.

## YAML

You can use the Options Creator in the Archipelago launcher version 0.6.6 and newer.
To do that, you'll need to put `dead_cells.apworld` in `Archipelago\custom_worlds` before launching Options Creator. Then the Dead Cells option will appear in the scrollable menu.

## Gameplay

The DLCs aren't mandatory, and you can select which ones are active in the yaml.

You should start your game from a new save, and you can duplicate your save and play on multiple slots at the same time, as some data is shared between them.

Achievements are disabled by this mod.

You define the goal in BSC in the yaml. This is the number of active BSC you should have when beating one of the final bosses to complete the archipelago.

Picking up blueprints, runes, aspects, killing bosses, and entering/exiting a biome are checks.

Except for Promenade of the Condemned, Ramparts, Toxic Sewers, Black Bridge and Bank, you'll need the key's biome to enter it.

Receiving the bank unlock item will make the biome appear at each transition until you enter it.

Scissor, Comb, Green Hole, Red Hole, Dark Vortex, Spatial Anomaly and Fisherman Hood have requirements based on the locations checked, not items received and unlocked.

A rework of the Hunter's Grenade makes it reusable and stacks active BSC+1 charges per biome completed.

An integrated menu allows you to see the history of items received, buy colorless affixes, gives you filler items and allows you to use a progression tracker. The menu button is at the top right of the equipment menu.

In the ap shop, you can buy colorless or legendary affixes, or Hunter's Grenade charges if you have one.

The number of kills you need for boss heads is reduced.

Blueprints in the daily challenge are given at each completion. The difficulty increases four times, and when you have every blueprint, you gain a Hunter's Grenade upon completion.

There is a x4 multiplier on cells, and completing a biome grants you 40 cells.

Outfits (except Cultist) cost 50 cells.

Items in the Collector's shop aren't locked anymore if you don't have enough items or don't have the previous item.

You can open the door of the mutation shop (because I never liked this door...).

On the second page of the ap menu, there is an Energy Link, allowing you to save or share your cells with other players.

You can use Death Link with this mod, including two variants, one that curses you instead of directly killing you, and the other that gives you a trap.

Damage Link, Health Link, and Trap Link are available, with the last two only compatible with other Dead Cells players.

## Known issues

Responsiveness issues for the mod's UI on resolutions other than 1920*1080 or 3840x2160.

Dying with assist mode will send the biome's end check.

There are currently issues with the king outfit. Once bought in the collector shop, the giants event will play and the king will disappear, making the Homunculus Rune and Symmetrical Lance disappear.

## Contributors

Thanks to OnlyLeafeon and Rayze, who helped me with the apworld.

Thanks to Libellule57, who drew the Dead Cells Archipelago logo.

## Contact

If you encounter any issues or just want to find a community to talk with, you can join us in the [Archipelago discord server](https://discord.gg/archipelago), in the [Dead Cells post](https://discord.com/channels/731205301247803413).

## Support the Project

If you enjoy this mod and would like to support my work, you can leave a donation on [Ko-fi](https://ko-fi.com/maxlamenace572). Donations are completely optional and are not required to download or use the mod.

