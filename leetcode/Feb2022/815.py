from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        routeMap=defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                routeMap[stop].append(i)
        #check if same bus goes to source and detination
        for bus in routeMap[source]:
            if bus in routeMap[target]:
                return 0
        numberofbuses=0
        seen=[]
        while len(seen) < len(routes):
            nextBus=[source]
            for bus in routeMap[nextBus]:
                if bus in routeMap[target]:
                    return numberofbuses+1
                seen.append(bus)
                numberofbuses+=1
                nextBus=bus
        return -1
