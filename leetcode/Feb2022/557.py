class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(' ')
        reversedArr=[]
        for word in arr:
            l=len(word)
            result=''
            for i in range(l-1,-1,-1):
                result+=word[i]
            reversedArr.append(result)
        return ' '.join(reversedArr)