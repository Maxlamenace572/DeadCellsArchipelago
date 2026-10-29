namespace DeadCellsArchipelago {
    public class FocusList : FocusItem
    {
        public bool IsVertical;
        public bool IsHorizontal;
        public int[] previousIndex = new int[2];
        public int[] currentIndex = new int[2];
        public int[] resetIndex = [0, 0];
        public int[] listSizes = new int[2];

        public override FocusItem? GetUp()
        {
            if (!IsVertical) return ClassicChange(base.GetUp());
            return ChangeIndex(base.GetUp(), -1, -1, 1);
        }

        public override FocusItem? GetDown()
        {
            if (!IsVertical) return ClassicChange(base.GetDown());
            return ChangeIndex(base.GetDown(), 1, listSizes[1], 1);
        }

        public override FocusItem? GetLeft()
        {
            if (!IsHorizontal) return ClassicChange(base.GetLeft());
            return ChangeIndex(base.GetLeft(), -1, -1, 0);
        }

        public override FocusItem? GetRight()
        {
            if (!IsHorizontal) return ClassicChange(base.GetRight());
            return ChangeIndex(base.GetRight(), 1, listSizes[0], 0);
        }

        private FocusItem? ChangeIndex(FocusItem? orig, int offset, int limit, int coord)
        {
            if (listSizes[0] == 0 && listSizes[1] == 0)
                return orig;

            previousIndex = (int[]) currentIndex.Clone();
            currentIndex[coord] += offset;

            if (currentIndex[coord] == limit)
            {
                if(orig != null)
                    currentIndex = (int[]) resetIndex.Clone();
                else
                    currentIndex = (int[]) previousIndex.Clone();
                return orig;
            }
            return this;
        }

        private FocusItem? ClassicChange(FocusItem? orig)
        {
            previousIndex = (int[]) currentIndex.Clone();

            if(orig != null)
                currentIndex = (int[]) resetIndex.Clone();
            else
                currentIndex = (int[]) previousIndex.Clone();
            return orig;
        }
    }
}