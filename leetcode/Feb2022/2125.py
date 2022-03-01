class Solution:
    def numberOfBeams(self, bank):
        rows=len(bank)
        cols=len(bank[0])
        maxLasers=0
        lastRowLaserCount=0
        currentRowLaser=0
        for row in range(rows):
            currentRowLaser=0
            for col in range(cols):
                if bank[row][col] == '1':
                    currentRowLaser+=1
            maxLasers+=(currentRowLaser*lastRowLaserCount)
            if currentRowLaser > 0:
                lastRowLaserCount=currentRowLaser
        return maxLasers
        
print(Solution().numberOfBeams(["011001","000000","010100","001000"]))
print(Solution().numberOfBeams(["000","111","000"]))