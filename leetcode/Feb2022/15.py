from collections import defaultdict
class Solution:
    def threeSum(self, nums):
        hashmap=defaultdict(list)
        for pos,num in enumerate(nums):
            hashmap[num].append(pos)
        result=[]
        for i in range(len(nums)-1):
            s=[]
            for j in range(i,len(nums)):
                com=0-(nums[i]+nums[j])
                if com in hashmap:
                    idxs=hashmap[com]
                    print(com,idxs,i,j)
                    for idx in idxs:
                        if idx != i and idx != j:
                            s.append(nums[i])
                            s.append(nums[j])
                            s.append(nums[idx])
                            s.sort()
                            if s not in result:
                                result.append(s)
                            s=[]
        return result

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))