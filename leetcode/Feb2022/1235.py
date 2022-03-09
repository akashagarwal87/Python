class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        sortedList=[]
        for i in range(len(startTime)):
            sortedList.append([startTime[i],endTime[i],profit[i]])
        sortedList.sort(key=lambda x:x[-1])
        maxProfit=sortedList[-1]
        gaps=[]
        for i in range(len(sortedList)-2,-1,-1):
            if sortedList[i][1] <= sortedList[i+1][0]:
                maxProfit+=sortedList[i][2]
        return maxProfit  