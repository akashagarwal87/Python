from operator import xor
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[first]
        for num in encoded:
            result.append(xor(result[-1],num))
        return result