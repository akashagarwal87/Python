class Solution:
    def myPow(self, x: float, n: int) -> float:
        result=1
        if n == 1:
            return x
        count=1
        isNegative=False
        if n < 0:
            n=n*-1
            isNegative=True
        while n > 0:
            result=result*x
            x=result
            n-=1
        if isNegative:
            result=1/result
        return result
