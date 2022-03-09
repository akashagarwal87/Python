class Solution:
    def prisonAfterNDays(self, cells, n):
        l=len(cells)
        loop=15
        if n <= loop:
            loop=n
        else:
            loop=(n-1)%14+1
        for i in range(loop):
            
            cellsCopy=cells.copy()
            for j in range(1,l-1):
                if cells[j-1] == cells[j+1]:
                    cellsCopy[j]=1
                else:
                    cellsCopy[j]=0
            cells=cellsCopy.copy()
            cells[-1]=0
            cells[0]=0
        return cells

# print(Solution().prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], n = 17))
# print(Solution().prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 1000000000))
print(Solution().prisonAfterNDays(cells =[1,1,0,1,1,0,0,1], n = 300663720))