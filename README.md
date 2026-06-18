<h1>Dead Cells Archipelago</h1>

This is an [Archipelago](https://github.com/ArchipelagoMW/Archipelago) mod for Dead Cells, using [Dead Cells Core Modding](https://github.com/dead-cells-core-modding/core).

## Setup

### Installer

For windows users, you can download the DeadCellsArchipelagoInstaller.zip from the latest release and launch the DeadCellsInstaller.exe. It will download dependencies (.net 10, DCCM), update the mod if needed and launch the game in modded.

Note: It can work for some non-Steam versions, but the GOG version is known to be incompatible.

### Manual install

To set up this mod, you'll first need to follow the Core Modding installation guide. You’ll also need the [.net SDK 10](https://dotnet.microsoft.com/fr-fr/download/dotnet/10.0).

Then in the coremod directory you'll need to put the mods directory from the .zip of the latest release of DeadCellsArchipelago. In the end, the path should look like `Dead Cells\coremod\mods\DeadCellsArchipelago`.

If you want to launch the modded game, you'll find it at `Dead Cells\coremod\core\host\startup\DeadCellsModding.exe`.

## YAML

You can use the Options Creator in the Archipelago launcher version 0.6.6 and newer.
To do that, you'll need to put `dead_cells.apworld` in `Archipelago\custom_worlds` before launching Options Creator. Then the Dead Cells option will appear in the scrollable menu.

## Gameplay

The DLCs aren't mandatory, and you can select which ones are active in the yaml.

You should start your game from a new save.

Achievements are disabled by this mod.

You define the goal in BSC in the yaml. This is the number of active BSC you should have when beating one of the final bosses to complete the archipelago.

Picking up blueprints, runes, aspects, killing bosses, and entering/exiting a biome are checks.

Except for Promenade of the Condemned, Ramparts, Toxic Sewers, Black Bridge and Bank, you'll need the key's biome to enter it.

A rework of the Hunter's Grenade makes it reusable and stacks active BSC+1 charges per biome completed.

An integrated menu allows you to see the history of items received, buy colorless affixes, gives you filler items and allows you to use a progression tracker. The menu button is in the equipment menu.

The number of kills you need for boss heads is reduced.

Blueprints in the daily challenge are given at each completion. The difficulty increases four times, and when you have every blueprint, you gain a Hunter's Grenade upon completion.

There is a x4 multiplier on cells, and completing a biome grants you 40 cells.

Outfits (except Cultist) cost 50 cells.

Items in the Collector's shop aren't locked anymore if you don't have enough items or don't have the previous item.

You can open the door of the mutation shop (because I never liked this door...).

You can use Death Link with this mod, including a variant that curses you instead of directly killing you.

## Known issues

Responsiveness issues for the mod's UI on resolutions higher than 1920*1080.

If you have another version of .NET other than 10, the installer will skip the .NET download even though the game won't launch.

Dying with assist mode will send the biome's end check.

Killing an enemy while using the blueprint extractor will lose you a charge.

## Contributors

Thanks to OnlyLeafeon and Rayze, who helped me with the apworld.

Thanks to Libellule57, who drew the Dead Cells Archipelago logo.

## Contact

If you encounter any issues or just want to find a community to talk with, you can join us in the [Archipelago discord server](https://discord.gg/archipelago), in the [Dead Cells post](https://discord.com/channels/731205301247803413).
