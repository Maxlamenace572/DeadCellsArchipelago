namespace DeadCellsArchipelago {
    public class FocusItem
    {
        public FocusItem? up;
        public FocusItem? down;
        public FocusItem? left;
        public FocusItem? right;
        public bool focusDisabled;
        public bool canRepeatAct;

        public virtual void Highlight(){}

        public virtual void StopHighlight(){}

        public virtual void Act(){}

        public virtual FocusItem? GetUp()
        {
            if (SkipVoidList(up) || SkipFocusDisabled(up)) return up!.GetUp();
            return up;
        }

        public virtual FocusItem? GetDown()
        {
            if (SkipVoidList(down) || SkipFocusDisabled(down)) return down!.GetDown();
            return down;
        }

        public virtual FocusItem? GetLeft()
        {
            if (SkipVoidList(left) || SkipFocusDisabled(left)) return left!.GetLeft();
            return left;
        }

        public virtual FocusItem? GetRight()
        {
            if (SkipVoidList(right) || SkipFocusDisabled(right)) return right!.GetRight();
            return right;
        }

        public static void SetLeftRight(FocusItem fiLeft, FocusItem fiRight)
        {
            fiLeft.right = fiRight;
            fiRight.left = fiLeft;
        }

        public static void SetUpDown(FocusItem fiUp, FocusItem fiDown)
        {
            fiUp.down = fiDown;
            fiDown.up = fiUp;
        }

        public bool SkipVoidList(FocusItem? dir)
        {
            return dir != null && dir is FocusList list && list.listSizes[0] == 0 && list.listSizes[1] == 0;
        }

        public bool SkipFocusDisabled(FocusItem? dir)
        {
            return dir != null && dir.focusDisabled;
        }
    }
}