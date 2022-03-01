from typing import DefaultDict
import heapq

class Solution:
    def diagonalSort(self, mat):
        rows=len(mat)
        cols=len(mat[0])
        tmp=DefaultDict(list)
        for row in range(rows):
            for col in range(cols):
                tmp[row-col].append(mat[row][col])
        for diag in tmp.values():
            heapq.heapify(diag)
        for row in range(rows):
            for col in range(cols):
                val=heapq.heappop(tmp[row-col])
                mat[row][col]=val
        return mat
                 