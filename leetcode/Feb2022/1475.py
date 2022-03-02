class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        minVal=10**4
        l=len(prices)
        result=[0]*l
        for i in range(l-1,-1,-1):
            print(prices[i],minVal)
            if prices[i]-minVal >= 0:
                result[i]=prices[i]-minVal
            else:
                
                minVal=prices[i]
                result[i]=prices[i]
        return result

print(Solution().finalPrices(prices = [8,4,6,2,3]))