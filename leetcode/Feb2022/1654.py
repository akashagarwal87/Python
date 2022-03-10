class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        jumps=0
        start=0
        if x in forbidden:
            return -1
        forbidden.sort()
        bound = max(max(forbidden) + a + b, x + b)
        isNextJump=True
        covered=[]
        print(forbidden)
        while isNextJump:
            print(covered,start)
            if start == x:
                return jumps
            if start > bound:
                return -1
            if start < x:
                start +=a
            elif start > x:
                if start -b < 0:
                    start+=a
                else:
                    start-=b
            if start in forbidden:
                return -1
            jumps+=1
            if start in covered:
                return -1
            covered.append(start)
        return jumps
# print(Solution().minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))
print(Solution().minimumJumps(forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], a = 29, b = 98, x = 80))