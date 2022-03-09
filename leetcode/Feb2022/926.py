class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        hashMap={'1':[],'0':[]}
        for pos,val in enumerate(s):
            hashMap[val].append(pos)
        
