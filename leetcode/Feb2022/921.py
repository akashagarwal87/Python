class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        numberofmoves=0
        stack=[]
        for letter in s:
            if letter== "(":
                stack.append("(")
            else:
                if len(stack) > 0:
                    stack.pop(0)
                else:
                    numberofmoves+=1
        return len(stack)+numberofmoves