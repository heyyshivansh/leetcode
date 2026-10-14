class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def new_func(nums):
            curr=1
            output=[1]*len(nums)
            for i in range(1,len(nums)):
                curr*=nums[i-1]
                output[i]=curr

            curr=1

            for i in range(len(nums)-2,-1,-1):
                curr*=nums[i+1]
                output[i]*=curr

            return output
        
        return new_func(nums)