class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtype=[nums[0]]
        for i in range(1,len(nums)):
            rtype.append(rtype[i-1]+nums[i])
        return rtype
                