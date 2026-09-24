class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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

        def locate_first_position():
            def condition(mid):
                if nums[mid] == target:
                    if mid > 0 and nums[mid - 1] == target:
                        return 'left'
                    else:
                        return 'found'
                elif nums[mid] < target:
                    return 'right'
                else:
                    return 'left'

            return binary_search(0, len(nums) - 1, condition)

        def locate_second_position():
            def condition(mid):
                if nums[mid] == target:
                    if mid < len(nums) - 1 and nums[mid + 1] == target:
                        return 'right'
                    else:
                        return 'found'
                elif nums[mid] < target:
                    return 'right'
                else:
                    return 'left'

            return binary_search(0, len(nums) - 1, condition)

        return [locate_first_position(), locate_second_position()]
