class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        current = []
        i = 0
        result = []

        def backtrack(i):
            if i == len(nums):
                result.append(current.copy())
                return

            current.append(nums[i])
            backtrack(i + 1)

            current.pop()
            backtrack(i + 1)

        backtrack(i)

        return result
