class Solution:
    def trap(self, height) -> int:
        maxWater=0
        stackleft=[height[0]]
        for i in range(1,len(height)):
            stackleft.append(max(height[i],stackleft[-1]))
        stackRight=[0]*len(height)
        stackRight[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            stackRight[i]=max(stackRight[i+1],height[i])
        # print(stackRight,stackleft,height)
        for i in range(len(height)):
            maxWater+=min(stackleft[i],stackRight[i])-height[i]
        return maxWater

print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap(height = [4,2,0,3,2,5]))