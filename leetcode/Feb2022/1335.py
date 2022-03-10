import heapq
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n=len(jobDifficulty)
        if n < d:
            return -1
        jobArr=[]
        equalDistribution=n//d
        for i in range(d-1):
            jobArr.append(jobDifficulty[i*equalDistribution:(i+1)*equalDistribution])
        jobArr.append(jobDifficulty[(i+1)*equalDistribution:])
        for i in range(len(jobArr)-1):
            
