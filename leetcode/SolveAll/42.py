class Solution:
    def trap(self, height):
        n=len(height)
        left=[height[0]]
        right=[0]*n
        right[-1]=height[-1]
        maxWater=0
        for i in range(1,n):
            left.append(max(left[-1],height[i]))
        for i in range(n-2,-1,-1):
            right[i]=max(height[i],right[i+1])
        for i in range(n):
            maxWater+=(min(left[i],right[i])-height[i])
        return maxWater