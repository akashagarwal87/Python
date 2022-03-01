class Solution:
    def minOperations(self, boxes):
        posOfBalls=[]
        for pos,val in enumerate(boxes):
            if val =="1":
                posOfBalls.append(pos)
        result=[0]*len(boxes)
        for pos,val in enumerate(boxes):
            moves=0
            for p1 in posOfBalls:
                if p1 == pos:
                    continue
                moves+=abs(pos-p1)
            result[pos]=moves
        return result
        