class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result=[]
        greater=[]
        pivotCount=0
        for num in nums:
            if num < pivot:
                result.append(num)
            elif num == pivot:
                pivotCount+=1
            else:
                greater.append(num)
        
        for i in range(pivotCount):
            result.append(pivot)
        
        for num in greater:
            result.append(num)
        return result