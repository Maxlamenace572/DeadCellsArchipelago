using dc;
using dc.achievements;
using HaxeProxy.Runtime;

namespace DeadCellsArchipelago {
    public static class AchievementManager
    {
        /*public static bool RemoveShouldDisplayInGameNotification(Hook_SteamAchievementManager.orig_shouldDisplayInGameNotification orig, SteamAchievementManager self)
        {
            //disable achievement pop up
            return false;
        }

        public static void RemoveUnlock(Hook_SteamAchievementManager.orig_unlock orig, SteamAchievementManager self, EAchievement achievement)
        {
            //remove steam achievement
        }

        public static bool RemoveIsUnlocked(Hook_SteamAchievementManager.orig_isUnlocked orig, SteamAchievementManager self, EAchievement achievement)
        {
            //say that the player doesn't have steam achievements
            return false;
        }*/

        public static void OnSetAchievement(Hook__Achievements.orig_setAchievement orig, EAchievement id, Ref<bool> showLog)
        {
            //remove in-game achievement
        }

        public static bool OnHasAchievement(Hook__Achievements.orig_hasAchievement orig, EAchievement id)
        {
            //say that the player doesn't have in-game achievements
            return false;
        }
    }
 }