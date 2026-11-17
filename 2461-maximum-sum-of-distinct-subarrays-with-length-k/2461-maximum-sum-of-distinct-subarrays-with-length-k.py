class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        i=0
        j=(k-1)
        s=sum(nums[:k])
        max_sum=0
        flag=False

        dic={}
        sub=nums[i:j+1]
        for value in (sub):
            dic[value]=dic.get(value,0)+1


        while(j!=len(nums)):
            sub=nums[i:j+1]
            
        
            # x=0
            # y=1

            # repeatition check


            if k==(len(dic.values())):
                flag=False
            else:
                flag=True


            #sum updattion  
            if flag==False:
                if s>max_sum:
                    max_sum=s

            if j<len(nums)-1:
                s=s-nums[i]+nums[j+1]
            
            flag=False
            if j<len(nums)-1: 
                dic[nums[i]]-=1                                     #outgoing elememt
                if dic[nums[i]]==0:
                    del dic[nums[i]]

                dic[nums[j+1]]=dic.get(nums[j+1],0)+1               #incoming element
            
            i+=1
            j+=1

            
        return max_sum
        




