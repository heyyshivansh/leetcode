class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0

        for i in range(len(grid)):
            lo = 0
            hi = len(grid[i]) - 1
            neg_row = 0

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if grid[i][mid] < 0:
                    neg_row = len(grid[i]) - mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            count += neg_row

        return count
