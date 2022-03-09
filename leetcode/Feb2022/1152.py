from collections import defaultdict
import heapq
class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        userMap=defaultdict(list)
        tup=[]
        for name,web,time in zip(username, website,timestamp):
            tup.append([name,web,time])
        tup.sort(key=lambda x:x[-1])
        print(tup)
        for name,web,time in tup:
            userMap[name].append(web)
        freq=defaultdict(int)
        for val in userMap.values():
            if len(val) == 3:
                freq[','.join(val)]+=1
            elif len(val) > 3:
                for i in range(len(val)-2):
                    freq[','.join(val[i:i+3])]+=1
        result=[]
        maxCount=0
        print(freq)
        for key,val in freq.items():
            if val > maxCount:
                result=[key]
                maxCount=val
            elif val == maxCount:
                result.append(key)

        if len(result) == 1:
            return result[0].split(',')
        else:
            result.sort()
            return result[0].split(',')

# print(Solution().mostVisitedPattern(["dowg","dowg","dowg"],[158931262,562600350,148438945],["y","loedo","y"]))
print(Solution().mostVisitedPattern(["zkiikgv","zkiikgv","zkiikgv","zkiikgv"],[436363475,710406388,386655081,797150921],["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]))
        