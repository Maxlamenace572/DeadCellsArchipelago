<h1>Dead Cells Archipelago</h1>

This is an [Archipelago](https://github.com/ArchipelagoMW/Archipelago) mod for Dead Cells, using [Dead Cells Core Modding](https://github.com/dead-cells-core-modding/core).

In its current state, this implementation is best suited for long sync or async games, as there are multiple situations where you can become blocked. For short sync, you should use advanced YAML parameters such as `start_inventory`, `exclude_locations`, etc.

## Setup

### Installer

For windows users, you can download the DeadCellsArchipelagoInstaller.zip from the latest release and launch the DeadCellsInstaller.exe. It will download dependencies (.net 10, DCCM), install the mod and launch the game in modded. You can update the mod or DCCM from the launcher, or launch without updating. If you have an ongoing game, you should check at the end of the release log if the new version is still compatible with your current apworld.

Note: This mod can be played with the Steam and GOG versions, and on the Goldberg emulator.

### Steam Workshop

For Steam players, you can subscribe to [Dead Cells Archipelago](https://steamcommunity.com/sharedfiles/filedetails/?id=3799334420). If you haven't used DCCM on Steam before, you'll need to also subscribe to it; a pop-up will ask you directly if you want to subscribe to dependencies, so you don't have to search for it. A small manual step is required the first time; you can find more details about it in [this guide](https://dead-cells-core-modding.github.io/docs/docs/tutorial/install-workshop/). 

### Manual install

To set up this mod, you'll first need to follow the [Core Modding installation guide](https://dead-cells-core-modding.github.io/docs/docs/tutorial/install-core/). You’ll also need the [.net SDK 10](https://dotnet.microsoft.com/fr-fr/download/dotnet/10.0).

Then in the coremod directory you'll need to put the mods directory from the .zip of the latest release of DeadCellsArchipelago. In the end, the path should look like `Dead Cells\coremod\mods\DeadCellsArchipelago`.

If you want to launch the modded game, you'll find it at `Dead Cells\coremod\core\host\startup\DeadCellsModding.exe`.

## YAML

You can use the Options Creator in the Archipelago launcher version 0.6.6 and newer.
To do that, you'll need to put `dead_cells.apworld` in `Archipelago\custom_worlds` before launching Options Creator. Then the Dead Cells option will appear in the scrollable menu.

## Gameplay

The DLCs aren't mandatory, and you can select which ones are active in the yaml.

You should start your game from a new save.
- You can duplicate your AP save and play on multiple slots at the same time, as some data is shared between them.

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

There is a biome warp that allows you to quickly go back to biomes you have already visited, as long as they are further than your current biome.
- You can also reload your current biome, allowing easier farming for blueprints.

There is a x4 multiplier on cells, and completing a biome grants you 40 cells.

Outfits (except Cultist) cost 50 cells.

Items in the Collector's shop aren't locked anymore if you don't have enough items or don't have the previous item.

You can open the door of the mutation shop (because I never liked this door...).

On the second page of the ap menu, there is an Energy Link, allowing you to save or share your cells with other players.

You can use Death Link with this mod, including two variants, one that curses you instead of directly killing you, and the other that gives you a trap.

Damage Link, Health Link, and Trap Link are available, with the last two only compatible with other Dead Cells players.

For now, the following traps can be found in the item pool:
- Curse Trap: Gives you a 50-stack of curses.
- Elite Trap: Spawns a team of two or three elite mobs on you. They are stunned for one second.
- Gold Trap: Deletes all your hard-earned gold.
- Weapon Break Trap: Randomly deletes one of your two weapons, or one of your two skills
- Reverse Trap: Swap every controls for one minute.
- Challenge Trap: Warps you into a challenge rift and gives you one curse (the curse is removed if you complete the challenge). 

## Known issues

A lot of improvements were done for the responsiveness issues on the mod's UI, but there are still some:
- The game needs to be played on fullscreen.
- Most new UI features have a tendency to have responsiveness issues. If you encounter any, you can post a screenshot with your resolution settings.

Dying with assist mode will send the biome's end check, and doesn’t send an aspect check. This is mostly due to the fact that the game itself doesn't recognize those as deaths, as you continue the same run. 

The reverse control trap seems to reset custom keybinds. They are set back to what they should be when entering the options menu.

The flawless challenge trap has some save stability issues. So when you encounter one, you should complete it before exiting the game.

The game wasn't originally made to handle multiple Hunter's Grenade uses. So the icons on the mobs aren't perfectly updated and can sometimes falsely indicate a mob as having a blueprint, even though you just took it.

## Contributors

Thanks to OnlyLeafeon and Rayze, who helped me with the apworld.

Thanks to Libellule57, who drew the Dead Cells Archipelago logo.

## Contact

If you encounter any issues or just want to find a community to talk with, you can join us in the [Archipelago discord server](https://discord.gg/archipelago), in the [Dead Cells post](https://discord.com/channels/731205301247803413/1552826784544850041).

## Support the Project

If you enjoy this mod and would like to support my work, you can leave a donation on [Ko-fi](https://ko-fi.com/maxlamenace572). Donations are completely optional and are not required to download or use the mod.

