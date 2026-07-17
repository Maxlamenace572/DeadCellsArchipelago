using dc.cine;
using dc.cine.coll;
using dc.cine.dlcp;
using dc.en;
using dc.en.hero;
using dc.en.inter;
using dc.en.inter.npc;
using dc.en.mob;
using dc.en.mob.boss;
using dc.haxe;
using dc.level;
using dc.level.lore;
using dc.level.@struct;
using dc.pr;
using dc.tool;
using dc.tool.atk;
using Hashlink.Virtuals;
using HaxeProxy.Runtime;
using ModCore.Utilities;
using static DeadCellsArchipelago.ItemManager;

namespace DeadCellsArchipelago {
    public static class UnlockItemManager
    {
        //here should be every item that decided not to do as the others, and have a hasUnlockedItem on them
        private static bool brGetBiomeVisitCount = false;

        public static void InitializeUnlockItemHooks()
        {
            Serilog.Log.Information("[AP] Loading Special Unlock Hooks...");
            
            Hook_Beheaded.displayCursePopup += OnDisplayCursePopup;
            Hook_Shipwreck.canGenerateThisLoreRoom += OnCanGenerateThisLoreRoomShipwreck;
            Hook_Shipwreck.buildMainRooms += OnBuildMainRoomsShipwreck;
            Hook_Credits.addEECustomHead += OnAddEECustomHead;
            Hook_CarmillaMask.onActivate += OnActivateCarmillaMask;
            Hook_Gardener.onActivate += OnActivateGardener;
            Hook_AmazonBase.onDie += OnDieAmazonBase;
            Hook_ShopMimic.dropBlueprint += OnDropBlueprint;
            Hook_Maria.onEndCine += OnEndCineMaria;
            Hook_LoreManager.onCustomEvent += OnCustomEventLoreManager;
            Hook_ArenaEntrance.onCreateExaminable += OnCreateExaminableArenaEntrance;
            Hook_Game.unlockVortexBadSeedHead += OnUnlockVortexBadSeedHead;
            Hook_Level.attachDeadCultistsInTumulus += OnAttachDeadCultistsInTumulus;
            Hook__HeadCheckHelper.checkUnlocked += OnCheckUnlocked;
            dc.en.mob.boss.Hook_Collector.onLastHit += OnLastHitCollector;
            dc.en.mob.boss.Hook_Collector.giveHeads += OnGiveHeads;
            Hook_MamaTick.publicSubmerge += OnPublicSubmerge;
            Hook_KingsHand.tryToPreventDeath += OnTryToPreventDeathKingsHand;
            Hook__KingsHand.__constructor__ += OnConstructorKingsHand;
            Hook__AlucardDooku.__constructor__ += OnConstructorAlucardDooku;
            Hook__Credits.__constructor__ += OnConstructorCredits;
            Hook__Merchant.__constructor__ += OnConstructorMerchant;
            Hook_Merchant.onActivate += onActivateMerchant;
            Hook_MerchantPan.canBeActivated += OnCanBeActivatedMerchantPan;
            Hook_MerchantPan.postUpdate += OnPostUpdateMerchantPan;
            Hook_PrisonStart.buildPrisonHUBZDoor += OnBuildPrisonHUBZDoorPrisonStart;
            Hook_Game.getBiomeVisitCount += OnGetBiomeVisitCount;
            Hook_PurpleGarden.buildGardenLoreRooms += OnBuildGardenLoreRooms;
            Hook_MariaRoom.unlockCatExaminable += OnUnlockCatExaminable;
            Hook_MariaRoom.onCreateExaminable += OnOnCreateExaminable;

            Serilog.Log.Information("[AP] Special Unlock Hooks loaded");
        }

        private static void OnDisplayCursePopup(Hook_Beheaded.orig_displayCursePopup orig, Beheaded self, int count, dc.String reason, Ref<bool> hidePopup)
        {//BlackHoleWhite
            useModdedHasUnlock = true;
            orig(self, count, reason, hidePopup);
            useModdedHasUnlock = false;
        }

        private static bool OnCanGenerateThisLoreRoomShipwreck(Hook_Shipwreck.orig_canGenerateThisLoreRoom orig, Shipwreck self, virtual_arc_examinables_fxEmitters_Intention_levels_onlyUseOnce_rarity_requiredLore_requiredMeta_room_roomLoot_sprites_status_structMode_ lore)
        {//Trident (part1)
            useModdedHasUnlock = true;
            var res = orig(self, lore);
            useModdedHasUnlock = false;
            return res;
        }

        private static RoomNode OnBuildMainRoomsShipwreck(Hook_Shipwreck.orig_buildMainRooms orig, Shipwreck self)
        {//Trident (part2)
            useModdedHasUnlock = true;
            var res = orig(self);
            useModdedHasUnlock = false;
            return res;
        }

        private static void OnAddEECustomHead(Hook_Credits.orig_addEECustomHead orig, Credits self, Section lastEESection)
        {//EvilEmpire
            useModdedHasUnlock = true;
            orig(self, lastEESection);
            useModdedHasUnlock = false;
        }

        private static void OnActivateCarmillaMask(Hook_CarmillaMask.orig_onActivate orig, CarmillaMask self, Hero by, bool lp)
        {//Simon
            useModdedHasUnlock = true;
            orig(self, by, lp);
            useModdedHasUnlock = false;
        }

        private static void OnActivateGardener(Hook_Gardener.orig_onActivate orig, Gardener self, Hero by, bool lp)
        {//RoyalGardener
            useModdedHasUnlock = true;
            orig(self, by, lp);
            useModdedHasUnlock = false;
        }

        
        private static void OnDieAmazonBase(Hook_AmazonBase.orig_onDie orig, AmazonBase self)
        {//3 Amazon
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnDropBlueprint(Hook_ShopMimic.orig_dropBlueprint orig, ShopMimic self)
        {//2 ShopMimic
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnEndCineMaria(Hook_Maria.orig_onEndCine orig, Maria self)
        {//Maria
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnCustomEventLoreManager(Hook_LoreManager.orig_onCustomEvent orig, LoreManager self, dc.String id, Examinable e)
        {//Sypha and Trevor (part1)
            useModdedHasUnlock = true;
            orig(self, id, e);
            useModdedHasUnlock = false;
        }

        private static bool OnCreateExaminableArenaEntrance(Hook_ArenaEntrance.orig_onCreateExaminable orig, ArenaEntrance self, dc.String custId, Examinable exam)
        {//Sypha and Trevor (part2)
            useModdedHasUnlock = true;
            var res = orig(self, custId, exam);
            useModdedHasUnlock = false;
            return res;
        }

        private static void OnUnlockVortexBadSeedHead(Hook_Game.orig_unlockVortexBadSeedHead orig, Game self)
        {//VortexBadSeed
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnAttachDeadCultistsInTumulus(Hook_Level.orig_attachDeadCultistsInTumulus orig, Level self)
        {//Cultist
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static bool OnCheckUnlocked(Hook__HeadCheckHelper.orig_checkUnlocked orig, dc.String itemKind)
        {//at least 13 heads
            useModdedHasUnlock = true;
            var res = orig(itemKind);
            useModdedHasUnlock = false;
            return res;
        }

        private static EndCollectorPreSmash OnLastHitCollector(dc.en.mob.boss.Hook_Collector.orig_onLastHit orig, dc.en.mob.boss.Collector self)
        {//KingWhite
            useModdedHasUnlock = true;
            var res = orig(self);
            useModdedHasUnlock = false;
            return res;
        }

        private static void OnGiveHeads(dc.en.mob.boss.Hook_Collector.orig_giveHeads orig, dc.en.mob.boss.Collector self)
        {//GlitchyHead
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnPublicSubmerge(Hook_MamaTick.orig_publicSubmerge orig, MamaTick self)
        {//TickSacrifice
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static bool OnTryToPreventDeathKingsHand(Hook_KingsHand.orig_tryToPreventDeath orig, KingsHand self, AttackData a, double prevLife)
        {//Bitter
            useModdedHasUnlock = true;
            var res = orig(self, a, prevLife);
            useModdedHasUnlock = false;
            return res;
        }

        private static void OnConstructorKingsHand(Hook__KingsHand.orig___constructor__ orig, KingsHand arg1, Level lvl, int x, int y, int dmgTier, int lifeTier)
        {//ArmoryUnlock
            useModdedHasUnlock = true;
            orig(arg1, lvl, x, y, dmgTier, lifeTier);
            useModdedHasUnlock = false;
        }

        private static void OnConstructorAlucardDooku(Hook__AlucardDooku.orig___constructor__ orig, AlucardDooku arg1, Hero h, AlucardNpc npc)
        {//Alucard
            useModdedHasUnlock = true;
            orig(arg1, h, npc);
            useModdedHasUnlock = false;
        }

        private static void OnConstructorCredits(Hook__Credits.orig___constructor__ orig, Credits arg1, EndRunKind kind)
        {//at least VortexAndSea
            useModdedHasUnlock = true;
            orig(arg1, kind);
            useModdedHasUnlock = false;
        }

        private static void OnConstructorMerchant(Hook__Merchant.orig___constructor__ orig, Merchant arg1, Level lvl, int x, int y, int d, MerchantType type)
        {//Pan (part1)
            useModdedHasUnlock = true;
            orig(arg1, lvl, x, y, d, type);
            useModdedHasUnlock = false;
        }

        private static void onActivateMerchant(Hook_Merchant.orig_onActivate orig, Merchant self, Hero by, bool lp)
        {//Pan (part2)
            useModdedHasUnlock = true;
            orig(self, by, lp);
            useModdedHasUnlock = false;
        }

        private static bool OnCanBeActivatedMerchantPan(Hook_MerchantPan.orig_canBeActivated orig, MerchantPan self, Hero by)
        {//Pan (part3)
            useModdedHasUnlock = true;
            var res = orig(self, by);
            useModdedHasUnlock = false;
            return res;
        }

        private static void OnPostUpdateMerchantPan(Hook_MerchantPan.orig_postUpdate orig, MerchantPan self)
        {//Pan (part4)
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnBuildPrisonHUBZDoorPrisonStart(Hook_PrisonStart.orig_buildPrisonHUBZDoor orig, PrisonStart self)
        {//BossRushUnlock (part 1)
            if (SAVED_DATA != null && SAVED_DATA.IsItemReceived("BossRushUnlock")) self.user.story.counters.set("BRUnlockPopUp".AsHaxeString(), 1);
            else self.user.story.counters.set("BRUnlockPopUp".AsHaxeString(), 0);

            brGetBiomeVisitCount = true;
            orig(self);
            brGetBiomeVisitCount = false;

            if (SAVED_DATA != null && SAVED_DATA.IsCheckSent("BossRushUnlock")) self.user.story.counters.set("BRUnlockPopUp".AsHaxeString(), 1);
            else self.user.story.counters.set("BRUnlockPopUp".AsHaxeString(), 0);
        }

        private static int? OnGetBiomeVisitCount(Hook_Game.orig_getBiomeVisitCount orig, Game self, dc.String id)
        {//BossRushUnlock (part 2)
            if (brGetBiomeVisitCount) return 0;
            return orig(self, id);
        }

        private static void OnBuildGardenLoreRooms(Hook_PurpleGarden.orig_buildGardenLoreRooms orig, PurpleGarden self)
        {//SpawnCat (part 1)
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static void OnUnlockCatExaminable(Hook_MariaRoom.orig_unlockCatExaminable orig, MariaRoom self)
        {//SpawnCat (part 2)
            useModdedHasUnlock = true;
            orig(self);
            useModdedHasUnlock = false;
        }

        private static bool OnOnCreateExaminable(Hook_MariaRoom.orig_onCreateExaminable orig, MariaRoom self, dc.String custId, Examinable exam)
        {//SpawnCat (part 3)
            useModdedHasUnlock = true;
            var res = orig(self, custId, exam);
            useModdedHasUnlock = false;
            return res;
        }
    }
}