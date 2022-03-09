from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashMap=defaultdict(int)
        para=''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        for word in para.split():
            if word not in banned:
                hashMap[word.lower()]+=1
        summary=list(hashMap.items())
        # print(summary)
        summary.sort(key=lambda x:x[1])
        return summary[-1][0]
