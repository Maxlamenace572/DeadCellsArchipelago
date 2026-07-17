using dc;
using dc.achievements;
using HaxeProxy.Runtime;
using Serilog;

namespace DeadCellsArchipelago {
    public static class AchievementManager
    {
        public static void InitializeAchievementHooks()
        {
            Log.Information("[AP] Loading Achievement Hooks...");

            Hook__Achievements.setAchievement += OnSetAchievement;
            Hook__Achievements.hasAchievement += OnHasAchievement;

            Log.Information("[AP] Achievement Hooks loaded");
        }

        private static void OnSetAchievement(Hook__Achievements.orig_setAchievement orig, EAchievement id, Ref<bool> showLog)
        {
            //remove in-game achievement
        }

        private static bool OnHasAchievement(Hook__Achievements.orig_hasAchievement orig, EAchievement id)
        {
            //say that the player doesn't have in-game achievements
            return false;
        }
    }
 }