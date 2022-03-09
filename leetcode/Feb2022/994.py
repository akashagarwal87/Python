class Solution:
    def orangesRotting(self, grid):
        #0-empty
        #1-fresh orange
        #2- rotten orange
        rows=len(grid)
        cols=len(grid[0])
        self.numberOfMoves=-1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    ##start the search
                    self.algo(row,col,rows,cols,grid,2)
        print(grid)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        if self.numberOfMoves < 0:
            return 0
        return self.numberOfMoves-2
    
    def algo(self,row,col,rows,cols,grid,move):
        # print(grid)
        self.numberOfMoves=max(self.numberOfMoves,move)
        if col+1 < cols and grid[row][col+1]==1:
            grid[row][col+1]=move+1
            self.algo(row,col+1,rows,cols,grid,move+1)
        if col>0 and grid[row][col-1] == 1:
            grid[row][col-1]=move+1
            self.algo(row,col-1,rows,cols,grid,move+1)
        if row+1 < rows and grid[row+1][col]==1:
            grid[row+1][col]=move+1
            self.algo(row+1,col,rows,cols,grid,move+1)
        if row > 0 and grid[row-1][col]==1:
            grid[row-1][col]=move+1
            self.algo(row-1,col,rows,cols,grid,move+1)

# print(Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
# print(Solution().orangesRotting(grid = [[0,2]]))
# print(Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting(grid = [[2,1,1],[1,1,1],[0,1,2]]))