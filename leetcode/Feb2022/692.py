from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap=defaultdict(int)
        for word in words:
            hashMap[word]+=1
        print(hashMap)
