from collections import OrderedDict
class Solution:
    def partitionLabels(self, s: str):
        posMap=OrderedDict()
        for pos,letter in enumerate(s):
            posMap[letter]=pos
        stack=[]
        count=0
        maxPos=0
        for pos,letter in enumerate(s):
            maxPos=max(maxPos,posMap[letter])
            if pos == maxPos:
                stack.append(pos-count+1)
                count=pos+1
        return stack

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))