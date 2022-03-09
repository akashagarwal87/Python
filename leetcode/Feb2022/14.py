class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort(key=lambda x:len(x))
        result=""
        for ps,ch in enumerate(strs[0]):
            for i in range(1,len(strs)):
                if strs[i][ps] != ch:
                    return result
            result+=ch
        return result