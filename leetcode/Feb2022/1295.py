class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(map(str,nums))
        count = 0
        for num in nums:
            if len(num)%2 == 0:
                count += 1
        return count