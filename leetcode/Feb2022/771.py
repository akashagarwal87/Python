class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map={}
        for x in jewels:
            map[x]=0
        count=0
        for stone in stones:
            if stone in map:
                count+=1
        return count