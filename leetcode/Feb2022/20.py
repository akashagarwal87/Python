class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for letter in s:
            if letter in ['(','[','{']:
                stack.append(letter)
            else:
                if stack:
                    if letter == ")" and stack[-1] == "(":
                        stack.pop()
                    elif letter== "}" and stack[-1] == "{":
                        stack.pop()
                    elif letter == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True