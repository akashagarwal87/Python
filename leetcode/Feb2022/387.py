from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap=defaultdict(int)
        for letter in s:
            hashMap[letter]+=1
        
        for pos,letter in enumerate(s):
            if hashMap[letter] == 1:
                return pos
        return -1