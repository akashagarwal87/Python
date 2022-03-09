class Solution:
    def myAtoi(self, s: str) -> int:
        result=""
        isSingFound=False

        for letter in s:
            if letter == " " and len(result) == 0:
                continue
            if letter in ['-','+']:
                if isSingFound or len(result) > 0:
                    break
                if len(result) == 0:
                    result+=letter+"0"
                    isSingFound=True
                continue
            if letter.isnumeric():
                # print(result)
                if len(result) > 1 and result[-1] in ['-','+']:
                    break
                result+=letter
            else:
                break
        if len(result) > 0:
            result=int(result)
            if result < (-2**31):
                return (-2**31)
            if result > (2**31-1):
                return 2**31-1
            return result
        return 0

# print(Solution().myAtoi("42"))
print(Solution().myAtoi("00000-42a1234"))