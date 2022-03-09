class Solution:
    def fullJustify(self, words, maxWidth):
        lengthArr=[]
        for word in words:
            lengthArr.append(len(word))
        i = 0
        result=[]
        while i < len(words):
            tmp=[]
            k=maxWidth
            k-=lengthArr[i]
            tmp.append(words[i])
            i+=1
            if i == len(words):
                result.append(self.getline(tmp,maxWidth,True))
                return result
            while k-1 >= lengthArr[i]:
                k-=1
                tmp.append(words[i])
                k-=lengthArr[i]
                i+=1
                if i == len(words):
                    result.append(self.getline(tmp,maxWidth,True))
                    return result
            result.append(self.getline(tmp,maxWidth,False))
        return result
    def getline(self,tmpArr,maxWidth,isLastLine):
        numberofwords=len(tmpArr)
        textlenght=sum(len(x) for x in tmpArr)
        whitespace=maxWidth-textlenght
        s=""
        if isLastLine:
            for word in tmpArr:
                s+=word
                if whitespace > 0:
                    s+=' '
                whitespace-=1
            print(whitespace,s)
            if whitespace > 0:
                s+=' '*whitespace
            return s
        else:
            if numberofwords > 1:
                spacebetweenwords=(whitespace)//(numberofwords-1)
                isEven=True
                extraSpaces=whitespace%(numberofwords-1)
                if extraSpaces != 0:
                    isEven=False

                for i in range(numberofwords-1):
                    s+=tmpArr[i]
                    s+=' '*spacebetweenwords
                    if not isEven:
                        s+= ' '
                        extraSpaces-=1
                        if extraSpaces == 0:
                            isEven=True
                s+=tmpArr[-1]
            else:
                s=tmpArr[0]
                s+=' '*whitespace
        return s


        
# print(Solution().fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
# print(Solution().fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
# print(Solution().fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))
print(Solution().fullJustify(words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
, maxWidth = 16))