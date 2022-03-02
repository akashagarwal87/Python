class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        result=[]
        for p,n in zip(pos,neg):
            result.append(p)
            result.append(n)
        return result