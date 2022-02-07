class Solution:
    def removeVowels(self, s: str) -> str:
        vowlelist=['a','e','i','o','u']
        result=""
        for letter in s:
            if letter not in vowlelist:
                result+=letter
        return result