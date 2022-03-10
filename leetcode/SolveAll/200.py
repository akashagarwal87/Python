class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        numberofIslands=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    self.dfs(grid,row,col,rows,cols)
                    numberofIslands+=1
        return numberofIslands
    def dfs(self,grid,row,col,rows,cols):
        boundary=[[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
        grid[row][col]="0"
        for r,c in boundary:
            if r > -1 and r < rows and c > -1 and c < cols and grid[r][c] == "1":
                self.dfs(grid,r,c,rows,cols)