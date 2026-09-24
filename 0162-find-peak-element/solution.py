class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(lo, hi, condition):
            while lo <= hi:
                mid = (lo + hi) // 2
                result = condition(mid)
                if result == 'found':
                    return mid
                elif result == 'left':
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        def condition(mid):
            left = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')

            if nums[mid] > left and nums[mid] > right:
                return 'found'
            elif nums[mid] < left:
                return 'left'
            else:
                return 'right'

        return binary_search(0, len(nums) - 1, condition)
