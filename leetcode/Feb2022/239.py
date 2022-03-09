class Solution:
    def maxSlidingWindow(self, nums, k):
        if k==1:
            return nums
        result=[max(nums[0:k])]
        lastVal=result[-1]
        for i in range(k,len(nums)):
            if nums[i] > lastVal:
                lastVal=nums[i]
            result.append(lastVal)
        return result

# print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(Solution().maxSlidingWindow(nums = [1,-1], k = 1))