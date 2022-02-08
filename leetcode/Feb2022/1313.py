class Solution:
    def decompressRLElist(self, nums):
        n=len(nums)
        result=[]
        for i in range(0,n,2):
            freq=nums[i]
            val=nums[i+1]
            for j in range(freq):
                result.append(val)
        return result