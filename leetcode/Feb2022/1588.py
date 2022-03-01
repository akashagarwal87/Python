class Solution:
    def sumOddLengthSubarrays(self, arr):
        result=sum(arr)
        n=len(arr)
        count=0
        noOfElement=1
        while True:
            count+=2
            noOfElement+=2
            if noOfElement > n:
                break
            for i in range(n-count):
                result+=sum(arr[i:i+noOfElement])
        return result

print(Solution().sumOddLengthSubarrays([1,4,2,5,3]))
print(Solution().sumOddLengthSubarrays([1,4]))