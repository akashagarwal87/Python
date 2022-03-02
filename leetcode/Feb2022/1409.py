class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p=[]
        for i in range(m):
            p.append(i+1)
        result=[]
        for query in queries:
            idx=p.index(query)
            result.append(idx)
            p.pop(idx)
            p.insert(0,query)
        return result
