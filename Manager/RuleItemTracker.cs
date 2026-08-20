using static DeadCellsArchipelago.ItemManager;
using static DeadCellsArchipelago.TrackerData;

namespace DeadCellsArchipelago {
    public static class RuleItemTracker
    {
        public static void AddSpecialRules()
        {
            Dictionary<string, List<List<string>>> hasRules = [];
            hasRules["BumpBoots"] = [["LadderKey"]];
            hasRules["ExplosiveGrenade"] = [["LadderKey"]];
            hasRules["PrisonCourtyard Exit"] = [["LadderKey"]];
            
            hasRules["Crowbar"] = [["TeleportKey"]];
            hasRules["FreemanSkin"] = [["TeleportKey"]];
            hasRules["RoyalGardener"] = [["TeleportKey"]];
            hasRules["P_Hot"] = [["TeleportKey"]];

            hasRules["P_Disengage"] = [["HomKey"]];
            hasRules["Money5"] = [["HomKey"]];

            hasRules["P_AmmoOnHit"] = [["WallJumpKey"]];
            hasRules["ParryShield"] = [["WallJumpKey", "BreakableGroundKey"]];
            hasRules["ThrowingSpear"] = [["WallJumpKey", "HomKey"]];

            hasRules["SpeedBlade"] = [["ScoringKey"]];
            hasRules["DamageAura"] = [["ScoringKey"]];
            hasRules["DashSword"] = [["ScoringKey"]];

            hasRules["Trident"] = [["BreakableGroundKey"]];
            hasRules["P_DeathBomb"] = [["BreakableGroundKey"]];

            hasRules["ExplosiveCrossBow"] = [
                ["LadderKey", "BreakableGroundKey", "WallJumpKey"], 
                ["LadderKey", "BreakableGroundKey", "HomKey"]
            ];
            hasRules["P_EasierCurse"] = [
                ["LadderKey", "BreakableGroundKey", "WallJumpKey", "TeleportKey", "BeholderPit Unlock", "Cemetery Unlock", "Crypt Unlock"], 
                ["LadderKey", "BreakableGroundKey", "HomKey", "TeleportKey", "BeholderPit Unlock", "Cemetery Unlock", "Crypt Unlock"]
            ];

            hasRules["RichterUppercutKey"] = [["RichterDashKey", "RichterUppercutKey"]];
            hasRules["TPSword"] = [["RichterUppercutKey"]];
            hasRules["RichterCastle Exit"] = [["RichterUppercutKey"]];
            hasRules["RichterROB"] = [["RichterUppercutKey"]];

            hasRules["Bitter"] = [["SideBomb"]];
            hasRules["BlackHoleWhite"] = [["P_CursedFlask"]];
            hasRules["HotlineMiamiChicken"] = [["BaseballBat"]];
            hasRules["KatanaZero"] = [["Katana"]];
            hasRules["ShovelKnight"] = [["Shovel"]];
            hasRules["HollowKnight"] = [["PureNail"]];
            hasRules["Blasphemous"] = [["FaceFlask"]];
            hasRules["Guacamelee"] = [["BumpBoots"], ["SpikedBoots"], ["MultiKickBoots"], ["QuickFists"]];
            hasRules["HyperLightDrifter"] = [["HardLightSword", "PrisonerHyperlight"]];
            hasRules["Guillain"] = [["BossRushUnlock", "BossRushStatue", "BankUnlock"]];
            hasRules["BlowTorchRed"] = [["FlameThrower"]];
            hasRules["StaphyHead"] = [["SpawnLilStaphy"]];
            hasRules["MushroomBoi"] = [["SpawnFriendlyHardy"]];
            hasRules["KingWhite"] = [["KingDefault"]];
            hasRules["TickSacrifice"] = [["SpawnFriendlyHardy"]];
            hasRules["PrisonerGold"] = [["PokebombUnlock"]];
            hasRules["BlackHoleBlue"] = [["LadderKey", "TeleportKey", "ScoringKey", "CustomKey", "BreakableGroundKey", "WallJumpKey", "HomKey", "ExploKey", "BackpackUnlock", "Recycling2",
                "ForgeRefine1", "ArmoryUnlock", "MirrorUnlock", "PokebombUnlock", "ShopRerolls", "ShopCategories", "RandomBow", "RandomShield", "RandomCC", "Flask4", "Money5"]];

            BuildHasRules(hasRules);


            Dictionary<string, List<List<string>>> canReachRules = [];
            canReachRules["Anathema"] = [["SewerShort Enter"], ["PurpleGarden Enter"], ["Greenhouse Enter"]];
            canReachRules["P_CursedFlask"] = [["SewerShort Enter"], ["PurpleGarden Enter"], ["Greenhouse Enter"]];
            canReachRules["P_DemonicForce"] = [["SewerShort Enter"], ["PurpleGarden Enter"], ["Greenhouse Enter"]];
            canReachRules["Misericord"] = [["SewerShort Enter"], ["PurpleGarden Enter"], ["Greenhouse Enter"]];
            canReachRules["P_DamnedVigor"] = [["SewerShort Enter"], ["PurpleGarden Enter"], ["Greenhouse Enter"]];
            canReachRules["Indulgence"] = [["SewerShort Enter"], ["PurpleGarden Enter"], ["Greenhouse Enter"]];

            canReachRules["ShipwreckKey"] = [["SewerShort Enter"]];
            canReachRules["VortexBadSeed"] = [["SewerShort Enter"], ["DookuCastle Enter"], ["Greenhouse Enter"]];
            canReachRules["CurseofTheDeadGods"] = [["Throne Exit"], ["QueenArena Exit"], ["DookuArena Exit"]];
            canReachRules["Flawless"] = [["Boss_Behemoth", "Boss_Beholder", "Boss_MamaTick", "Boss_TimeKeeper", "Boss_Giant", "Boss_GardenerBoss", "Boss_KingsHand",
                "Boss_AmazonBrutal", "Boss_Queen", "Boss_Collector"]];
            canReachRules["BlobbyFlameMagma"] = [["Boss_KingsHand"]];

            BuildReachRules(canReachRules);


            if (ItemsData.ContainsKey("Terraria") && ItemsData["Terraria"].accessible)
            {
                ItemsData["Terraria"].accessible = HasItems([["Backpack"]]) && CanReachLocations([["Boss_KingsHand"], ["Cemetery Enter"]]) ;
                ItemsData["Terraria"].requirements = [["Backpack"]];
            }

            if (ItemsData.ContainsKey("CavernKey") && ItemsData["CavernKey"].accessible)
            {
                ItemsData["CavernKey"].accessible = HasItems([["HomKey"]]) && CanReachLocations([["Boss_KingsHand"]]) ;
                ItemsData["CavernKey"].requirements = [["HomKey"]];
            }

            if (ItemsData.ContainsKey("LongBow") && ItemsData["LongBow"].accessible)
            {
                ItemsData["LongBow"].accessible = HasItems([["TeleportKey", "LadderKey"]]) || (HasItems([["TeleportKey"]]) && CanReachLocations([["Boss_Death"]])) ;
                ItemsData["LongBow"].requirements = [["TeleportKey", "LadderKey"], ["TeleportKey", "Death"]];
            }


            Dictionary<string, int> bossRushRules = [];
            bossRushRules["BossRushStatue"] = 1;
            bossRushRules["Mentor"] = 1;
            bossRushRules["Mentor2"] = 1;
            bossRushRules["Mentor3"] = 1;
            bossRushRules["HydraSpell"] = 1;
            bossRushRules["Taunt"] = 1;

            bossRushRules["Mentor1"] = 2;
            bossRushRules["VictoriusBeheaded"] = 2;
            bossRushRules["VictoriusBeheaded1"] = 2;
            bossRushRules["VictoriusBeheaded2"] = 2;
            bossRushRules["VictoriusBeheaded3"] = 2;
            bossRushRules["P_Wishes"] = 2;

            BuildBossRushRules(bossRushRules);


            Dictionary<string, int> worldDepthRules = [];
            worldDepthRules["RevengeSword"] = 2;
            worldDepthRules["P_ColdDmg"] = 2;
            worldDepthRules["ClusterBomb"] = 2;
            worldDepthRules["HeavyTurret"] = 2;
            worldDepthRules["PrisonerDemon"] = 2;
            worldDepthRules["P_Execute_LowHealth"] = 2;
            worldDepthRules["P_DmgPlantedArrow"] = 2;
            worldDepthRules["Katana"] = 2;
            worldDepthRules["PrisonerKillBill"] = 2;
            worldDepthRules["SpikedBoots"] = 2;
            worldDepthRules["CeilTurret"] = 2;
            worldDepthRules["P_Backpack_Shield"] = 2;
            worldDepthRules["SismicBlade"] = 2;
            worldDepthRules["PrisonerAladdin"] = 2;

            worldDepthRules["Lightning"] = 4;
            worldDepthRules["LeechBuff"] = 4;
            worldDepthRules["HookWhip"] = 4;
            worldDepthRules["P_CDR_locked"] = 4;
            worldDepthRules["Cannon"] = 4;
            worldDepthRules["P_DmgSkillRanged"] = 4;
            worldDepthRules["MarkBow"] = 4;
            worldDepthRules["PrisonerBison"] = 4;
            worldDepthRules["Hook"] = 4;
            worldDepthRules["BumpShield"] = 4;
            worldDepthRules["PrisonerSylvanian"] = 4;

            worldDepthRules["MultiKickBoots"] = 5;
            worldDepthRules["MultiCrossBow"] = 5;
            worldDepthRules["BulletBlade"] = 5;
            worldDepthRules["PrisonerHyperlight"] = 5;
            worldDepthRules["P_DmgNearRanged"] = 5;
            worldDepthRules["SlowOrb"] = 5;
            worldDepthRules["SpikeShield"] = 5;
            worldDepthRules["MagicSalve"] = 5;
            worldDepthRules["PrisonerShaman"] = 5;
            worldDepthRules["Guacamelee"] = 5;

            worldDepthRules["Shockwave"] = 7;
            worldDepthRules["ExplosiveGrenade"] = 7;
            worldDepthRules["Crusher"] = 7;
            worldDepthRules["P_Bleed"] = 7;
            worldDepthRules["PrisonerCarduus"] = 7;
            worldDepthRules["Tornado"] = 7;
            worldDepthRules["P_ScaledHealth"] = 7;
            worldDepthRules["QuickFists"] = 7;
            worldDepthRules["P_Health"] = 7;
            worldDepthRules["BarrelLauncher"] = 7;

            BuildWorldDepthRules(worldDepthRules);


            Dictionary<string, int> outfitsRules = [];
            outfitsRules["Scissor"] = 16;
            outfitsRules["Comb"] = 51;

            int nbOutfits = BuildOutfitRules(outfitsRules);


            Dictionary<string, int> itemsRules = [];
            itemsRules["BlackHoleGreen"] = 75;

            BuildItemRules(itemsRules, nbOutfits);


            Dictionary<string, int> headsRules = [];
            headsRules["BlackHoleRed"] = 7;
            headsRules["VortexFoundry"] = 14;
            headsRules["GlitchyHeadDeepSpace"] = 31;
            headsRules["Pecheur"] = 35;

            BuildHeadRules(headsRules);
        }

        //For items received. sub lists are AND condition, an OR condition is applied between sub lists.
        public static bool HasItems(List<List<string>> requirements)
        {
            foreach (List<string> requirement in requirements)
            {
                bool line = true;
                foreach (string item in requirement)
                {
                    line = line && SAVED_DATA!.IsItemReceived(item);
                }
                if (line) return true;
            }
            return false;
        }

        //Check if this location is sent or accessible
        private static bool CanReachLocations(List<List<string>> allLocations)
        {
            foreach (List<string> locations in allLocations)
            {
                bool line = true;
                foreach (string location in locations)
                {
                    line = line && (SAVED_DATA!.IsCheckSent(location) || (ItemsData.ContainsKey(location) && ItemsData[location].accessible));
                }
                if (line) return true;
            }
            return false;
        }

        //return 1 for trial 1 & 2 accessible, 2 for trial 3 & 4 accessible. If None accessible, return 0
        private static int GetBossRushLevel()
        {
            List<List<string>> AllBosses = [
                ["Boss_Behemoth", "Boss_Beholder", "Boss_MamaTick", "Boss_Death"],
                ["Boss_TimeKeeper", "Boss_Giant", "Boss_GardenerBoss", "Boss_DookuBeast"],
                ["Boss_KingsHand", "Boss_AmazonSurvival", "Boss_Queen", "Boss_DookuBeast"]
            ];

            if (!HasItems([["BossRushUnlock"]])) return 0;

            List<int> bosses = [0, 0, 0];
            for (int i = 0; i > AllBosses.Count; i++)
            {
                foreach (string boss in AllBosses[i])
                {
                    if (CanReachLocations([[boss]])) bosses[i]++;
                }
            }
            if (bosses[0] >= 2 && bosses[1] >= 2 && bosses[2] >= 1) return 2;
            if (bosses[0] >= 1 && bosses[1] >= 1 && bosses[2] >= 1) return 1;
            return 0;
        }

        //return the maximal depth possible
        private static int GetMaxWorldDepth()
        {
            List<List<string>> AllBiomes = [
                ["PrisonStart Enter"],
                ["PrisonCourtyard Enter", "SewerShort Enter", "PrisonDepths Enter", "PrisonCorrupt Enter", "Greenhouse Enter", "PurpleGarden Enter"],
                ["PrisonRoof Enter", "Ossuary Enter", "SewerDepths Enter", "Swamp Enter", "DookuCastle Enter"],
                ["Bridge Enter", "BeholderPit Enter", "SwampHeart Enter", "DeathArena Enter"],
                ["StiltVillage Enter", "AncientTemple Enter", "Cemetery Enter", "Tumulus Enter"],
                ["ClockTower Enter", "Crypt Enter", "Cavern Enter", "Cliff Enter"],
                ["TopClockTower Enter", "Giant Enter", "GardenerStage Enter"],
                ["Castle Enter", "Distillery Enter", "Shipwreck Enter", "DookuCastleHard Enter"],
                ["Throne Enter", "Lighthouse Enter", "DookuArena Enter"],
                ["Astrolab Enter"],
                ["Observatory Enter", "QueenArena Enter"]
            ];

            for (int i = AllBiomes.Count-1; i >= 0; i--)
            {
                foreach (string biome in AllBiomes[i])
                {
                    if (CanReachLocations([[biome]])) return i;
                }
            }
            return 0;
        }

        private static int GetNbItemSend()
        {
            if(!itemList.Any()) InitLists();

            int count = 0;
            foreach (string item in itemList)
            {
                if (CanReachLocations([[item]])) count ++;
            }
            return count;
        }

        private static int GetNbOutfitSend()
        {
            if(!outfitList.Any()) InitLists();

            int count = 0;
            foreach (string outfit in outfitList)
            {
                if (CanReachLocations([[outfit]])) count ++;
            }
            return count;
        }

        private static int GetNbHeadSend()
        {
            if(!headList.Any()) InitLists();

            int count = 0;
            foreach (string head in headList)
            {
                if (!new[] {"BlackHoleRed", "VortexFoundry", "GlitchyHeadDeepSpace", "Pecheur" }.Any(head.Contains) && CanReachLocations([[head]])) count ++;
            }
            return count;
        }

        private static void BuildHasRules(Dictionary<string, List<List<string>>> rules)
        {
            foreach (KeyValuePair<string, List<List<string>>> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = HasItems(rule.Value);
                    ItemsData[rule.Key].requirements = rule.Value;
                }
            }
        }

        private static void BuildReachRules(Dictionary<string, List<List<string>>> rules)
        {
            foreach (KeyValuePair<string, List<List<string>>> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = CanReachLocations(rule.Value);
                }
            }
        }

        private static void BuildBossRushRules(Dictionary<string, int> rules)
        {
            int bossRushLevel = GetBossRushLevel();

            foreach (KeyValuePair<string, int> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = bossRushLevel >= rule.Value;
                }
            }
        }

        private static void BuildWorldDepthRules(Dictionary<string, int> rules)
        {
            int maxWorldDepth = GetMaxWorldDepth();

            foreach (KeyValuePair<string, int> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = maxWorldDepth >= rule.Value;
                }
            }
        }

        private static int BuildOutfitRules(Dictionary<string, int> rules)
        {
            int outfits = GetNbOutfitSend();

            foreach (KeyValuePair<string, int> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = outfits >= rule.Value;
                }
            }

            return outfits;
        }

        private static void BuildItemRules(Dictionary<string, int> rules, int outfits)
        {
            int items = GetNbItemSend() + outfits;

            foreach (KeyValuePair<string, int> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = items >= rule.Value;
                }
            }
        }

        private static void BuildHeadRules(Dictionary<string, int> rules)
        {
            int heads = GetNbHeadSend();
            foreach (KeyValuePair<string, int> rule in rules)
            {
                if (ItemsData.ContainsKey(rule.Key) && ItemsData[rule.Key].accessible)
                {
                    ItemsData[rule.Key].accessible = heads >= rule.Value;
                }
            }
        }
    }
}