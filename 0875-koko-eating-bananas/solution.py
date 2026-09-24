class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        hi = max(piles)
        k = 1

        while low <= hi:
            mid = low + (hi - low) // 2
            s = 0

            for i in range(len(piles)):
                s += (-(piles[i] // -mid))

            if s <= h:
                hi = mid - 1
            else:
                low = mid + 1

        return low
