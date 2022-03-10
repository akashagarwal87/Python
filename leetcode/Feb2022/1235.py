import heapq
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        sortedList=[]
        for i in range(len(startTime)):
            sortedList.append([startTime[i],endTime[i],profit[i]])
        sortedList.sort(key=lambda x:x[0])
        print(sortedList)
        maxProfit=0
        job=[]
        heapq.heapify(job)
        for i in range(len(sortedList)):
            currentJob=sortedList[i]
            while job and job[0][0] <= currentJob[0]:
                maxProfit=max(heapq.heappop(job)[1],maxProfit)
            heapq.heappush(job,[currentJob[1],maxProfit+currentJob[2]])
        maxProfit=0
        for jobs in job:
            maxProfit=max(maxProfit,jobs[1])
        return maxProfit
        
print(Solution().jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
print(Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))