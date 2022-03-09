class Solution:
    def maxProfit(self, prices):
        maxPrice=0
        minprice=10**4
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            else:
                maxPrice=max(maxPrice,prices[i]-minprice)
        return maxPrice

print(Solution().maxProfit(prices = [7,1,5,3,6,4]))
print(Solution().maxProfit(prices = [7,6,4,3,1]))
print(Solution().maxProfit(prices = [2,1,4]))