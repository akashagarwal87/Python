class Solution:
    def findBuildings(self, heights):
        result=[]
        n=len(heights)
        maxHeight=-1
        for i in reversed(range(n)):
            if heights[i] > maxHeight:
                result.append(i)
                maxHeight=heights[i]
        result.reverse()
        return result

print(Solution().findBuildings([4,2,3,1]))