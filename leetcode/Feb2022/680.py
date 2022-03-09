class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return self.isPalindrome(s[left+1:right+1]) or self.isPalindrome(s[left:right])
        return True
    def isPalindrome(self,s):
        # print(s)
        left=0
        right=len(s)-1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        return True