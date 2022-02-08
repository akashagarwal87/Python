class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=0
        for candy in candies:
            maxCandies=max(maxCandies,candy)
        result=[]
        for candy in candies:
            if candy+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result