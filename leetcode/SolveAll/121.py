class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal=10**5
        maxProfit=0
        for price in prices:
            if price < minVal:
                minVal=price
                continue
            maxProfit=max(maxProfit,price-minVal)
        return maxProfit