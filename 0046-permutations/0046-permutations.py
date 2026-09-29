class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        used=[False]*len(nums)
        curr=[]
        output=[]
        def perm(used,curr):
            if len(curr)==len(nums):
                output.append(curr.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    curr.append(nums[i])
                    used[i]=True
                    perm(used,curr)
                    curr.pop()
                    used[i]=False
            return output
        return(perm(used,curr))
                


