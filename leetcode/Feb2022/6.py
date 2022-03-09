class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result=['']*numRows
        isForward=True
        count=0
        if numRows <= 1:
            return s
        for pos,letter in enumerate(s):
            # print(letter,count)
            result[count]+=letter
            if count < numRows and isForward:
                count+=1
                if count >= numRows:
                    count =numRows-2

                    isForward=False
            elif not isForward and count > 0:
                count-=1
            else:
                count=1
                isForward=True
        return ''.join(result)

# print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))
print(Solution().convert(s = "ABC", numRows = 2))