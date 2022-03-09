class Solution:
    def dailyTemperatures(self, temperatures):
        l=len(temperatures)
        result=[0]*l
        stack=[]
        for i in range(l-1):
            if temperatures[i] < temperatures[i+1]:
                result=[i]
        ##Brute Force
        # result=[]
        # for i in range(len(temperatures)-1):
        #     count=0
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures:
        #             result.append(count)
        #             break
        #         count+=1
        # return result