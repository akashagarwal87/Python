import heapq
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            curInterval=intervals[i]
            if curInterval[0] <= result[-1][1]:
                if result[-1][1] > curInterval[1]:
                    result[-1][1]=curInterval[1]
            else:
                result.append(curInterval)
        return result
    
