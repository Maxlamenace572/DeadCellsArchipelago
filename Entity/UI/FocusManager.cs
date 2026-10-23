using static DeadCellsArchipelago.PauseMenuManager;

namespace DeadCellsArchipelago {
    public class FocusManager
    {
        public FocusItem currentFocus;
        public FocusItem? returnFocus;
        public bool focusModEnabled;
        public int page;
        public int lastPage = 1;
        public int nbPage = 2;
        public int popUp;
        public bool textFieldFocused;

        public FocusManager(FocusItem current)
        {
            currentFocus = current;
        }

        public void Controller(int act)
        {
            if (textFieldFocused) return;
            switch (act)
            {
                case 10:    //up
                    if (!focusModEnabled)
                        InitializeModFocus();
                    else
                        ChangeFocus(currentFocus.GetUp());
                    break;
                case 12:    //down
                    if (focusModEnabled && page == 0)
                        EndModFocus();
                    else
                        ChangeFocus(currentFocus.GetDown());
                    break;
                case 11:    //left
                    ChangeFocus(currentFocus.GetLeft());
                    break;
                case 13:    //right
                    ChangeFocus(currentFocus.GetRight());
                    break;
                case 0:     //a
                    currentFocus.Act();
                    break;
                case 1:     //b
                case 8:     //escape
                    ReturnAct();
                    break;
            }
        }

        private void ReturnAct()
        {
            if (popUp != 0)
            {
                popUp = 0;
                ChangeFocus(returnFocus);
                returnFocus = null;
            }
            else if (page != 0)
            {
                lastPage = page;
                page = 0;
                ChangeApMenuButtonDownTarget();
                EndModFocus();
            }
        }

        public void ChangeFocus(FocusItem? newFocus)
        {
            if(newFocus == null) return;
            currentFocus.StopHighlight();
            newFocus.Highlight();
            currentFocus = newFocus;
        }

        public void ChangePopUpFocus(FocusItem newFocus)
        {
            currentFocus.StopHighlight();
            newFocus.Highlight();
            returnFocus = currentFocus;
            currentFocus = newFocus;
        }

        public void ChangeFocusCursor(FocusItem newFocus)
        {
            if (currentFocus is FocusList list && newFocus != currentFocus)
            {
                list.previousIndex = (int[]) list.currentIndex.Clone();
                list.currentIndex = [0, 0];
            }
            currentFocus.StopHighlight();
            newFocus.Highlight();
            currentFocus = newFocus;
        }

        public void InitializeModFocus()
        {
            currentFocus = topMenu!.menuButton;
            currentFocus.Highlight();
            focusModEnabled = true;
        }

        public void EndModFocus()
        {
            currentFocus.StopHighlight();
            focusModEnabled = false;
        }

        public void ChangeApMenuButtonDownTarget()
        {
            switch (page)
            {
                case 0:
                    topMenu!.SetDown(null);
                    break;
                case 1:
                    topMenu!.SetDown(scrollerBiome);
                    break;
                case 2:
                    topMenu!.SetDown(energyLink!.energyLinkMiddle.upButton);
                    break;
            }
        }
    }
}