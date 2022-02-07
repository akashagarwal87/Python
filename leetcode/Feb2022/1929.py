class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)*2
        n=len(nums)
        for i in range(len(nums)):
            result[i]=nums[i]
            result[n+i]=nums[i]
        return result