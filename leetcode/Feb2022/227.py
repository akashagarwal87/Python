class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sM=""
        for letter in s:
            if letter != " ":
                sM+=letter
        s=sM
        # print(s)
        ## BODMAS
        val=0
        operatorSequence=["/","*","+","-"]
        flag=False
        for operator in operatorSequence:
            sArr=s.split(operator)
            # print(operator,sArr)
            while len(sArr) > 1:
                flag=True
                ## operator is present
                val1,left=self.extractNumber(sArr[0],True,operatorSequence)
                val2,right=self.extractNumber(sArr[1],False,operatorSequence)
                if operator == "/":
                    val=str(val1//val2)
                elif operator =="+":
                    val=str(val1+val2)
                elif operator == "*":
                    val=str(val1*val2)
                else:
                    val=str(val1-val2)
                s=left+val+right
                sArr=s.split(operator)

                # print(val)
        if not flag:
            return int(s)
        return val
    
    def extractNumber(self,s,isLeft,operatorList):
        val=0
        removedString=""
        if isLeft:
            n=len(s)
            multiplier=1
            flag=True
            for i in range(len(s)-1,-1,-1):
                if ord(s[i]) >= 48 and ord(s[i]) <= 57 and flag:
                    # print(s[i],multiplier,val)
                    val=int(s[i])*(multiplier)+val
                    multiplier=multiplier*10
                else:
                    removedString=s[i]+removedString
                    flag=False
        else:
            flag=True
            for i in range(len(s)):
                if ord(s[i]) >= 48 and ord(s[i]) <= 57 and flag:
                    val=val*10+int(s[i])
                else:
                    removedString+=s[i]
                    flag=False
        return (val,removedString)

if __name__ == "__main__":
    print(Solution().calculate(" 33 + 3 /3"))
    # assert Solution().calculate(" 3 + 3") == 6, "Failed Test case"