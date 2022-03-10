class Solution:
    def maxSubArray(self, nums):
        maxsum=-(10**4)
        curSum=-(10**4)
        for num in nums:
            curSum=max(nums,curSum+num)
            maxsum=max(maxsum,curSum)
        return maxsum