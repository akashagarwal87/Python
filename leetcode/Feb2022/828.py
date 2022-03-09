from re import S


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        hashMap = {}   # {char: [positions]}
        for i in range(len(s)):
            char = s[i]
            if char in hashMap:
                hashMap[char].append(i)
            else:
                hashMap[char] = [-1]
                hashMap[char].append(i)
                
        count = 0
        for key in hashMap:
            positions = hashMap[key]
            
            positions.append(len(s))
            for i in range(1, len(positions) - 1):
                count = count + (positions[i] - positions[i-1]) * (positions[i+1] - positions[i])
        return count

print(Solution().uniqueLetterString("LEETCODE"))