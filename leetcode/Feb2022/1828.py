class Solution:
    def countPoints(self, points, queries):
        result=[]
        for query in queries:
            x=query[0]
            y=query[1]
            radius=query[2]
            count=0
            for point in points:
                xp=point[0]
                yp=point[1]
                dx=(xp-x) 
                dy=(yp-y) 
                # print(x,xp,dx,y,yp,dy,radius)
                if dx**2+ dy**2 <= radius**2:
                    count +=1
            result.append(count)
        return result
print(Solution().countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))