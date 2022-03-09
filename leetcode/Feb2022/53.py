class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum=nums[0]
        curSum=nums[0]
        for i in range(1,len(nums)):
            curSum=max(nums[i],curSum+nums[i])
            maxSum=max(maxSum,curSum)
        return maxSum