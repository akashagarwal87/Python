class Solution:
    def smallerNumbersThanCurrent(self, nums):
        map={}
        for num in nums:
            if num in map:
                map[num]=map[num]+1
            else:
                map[num]=1
        result=[]
        for num in nums:
            count=0
            for key,val in map.items():
                if key >= num:
                    continue
                count+=val
            result.append(count)
        return result