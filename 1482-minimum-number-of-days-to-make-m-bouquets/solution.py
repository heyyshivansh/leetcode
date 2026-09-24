class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        lo = min(bloomDay)
        hi = max(bloomDay)

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            flower = 0
            bouquet = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    flower += 1

                    if flower == k:
                        bouquet += 1
                        flower = 0
                else:
                    flower = 0

            if bouquet >= m:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
