class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWord=0
        for sentence in sentences:
            maxWord=max(maxWord,sentence.count(' ')+1)
        return maxWord