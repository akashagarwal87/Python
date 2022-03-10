from collections import defaultdict
class Solution:
    def twoSum(self, nums, target: int):
        result=[]
        hashMap=defaultdict(list)
        for pos,val in enumerate(nums):
            hashMap[val].append(pos)
        
        for i in range(len(nums)):
            com=target-nums[i]
            if com in hashMap:
                for j in hashMap[com]:
                    if i != j:
                        return [i,j]
        return []