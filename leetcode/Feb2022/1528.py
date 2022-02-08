class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=['']*len(indices)
        for pos,letter in enumerate(s):
            result[indices[pos]]=letter
        return ''.join(result)