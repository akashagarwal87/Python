class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while n > 0:
            val=n%10
            n=n//10
            sum+=val
            product*=val
        return product-sum