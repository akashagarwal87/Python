class Solution:
    def minRemoveToMakeValid(self, s):
        result=[]
        stack=[]
        for pos,letter in enumerate(s):
            if letter == ")":
                if stack:
                    stack.pop()
                    result.append(letter)
                continue
            elif letter == "(":
                stack.append(pos)
            result.append(letter)
        while stack:
            for i in range(len(result)-1,-1,-1):
                if result[i] == "(":
                    result.pop(i)
                    stack.pop()
        return ''.join(result)