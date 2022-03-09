from collections import defaultdict

from zmq import has
class Solution:
    def originalDigits(self, s: str) -> str:
        hashMap=defaultdict(int)
        for ch in s:
            hashMap[ch]+=1
        counts=[0]*10
        result=""
        
        if 'z' in hashMap:
            #zero
                result+="0"*hashMap['z']
                counts[0]=hashMap['z']
        if 'w' in hashMap:
            #two
            result+="2"*hashMap['w']
            counts[2]=hashMap['w']
        if 'u' in hashMap:
            #four
            result+="4"*hashMap['u']
            counts[4]=hashMap['u']
        if 'o' in hashMap:
            #one
            counts[1]=hashMap['o']-counts[4]-counts[0]-counts[2]
            result+="1"*counts[1]
        if 'r' in hashMap:
            #three
            counts[3]=hashMap['r']-counts[4]-counts[0]
            result+="3"*counts[3]
        if 'f' in hashMap:
            ##five
            counts[5]=hashMap['f']-counts[4]
            result+='5'*(counts[5])
        if 'x' in hashMap:
            #six
            result+='6'*(hashMap['x'])
            counts[6]=hashMap['x']
        if 'v' in hashMap:
            #seven
            counts[7]=hashMap['v']-counts[5]
            result+='7'*(counts[7])
        if 'h' in hashMap:
            counts[8]=hashMap['h']-counts[3]
            result+='8'*(counts[8])
        if 'i' in hashMap:
            counts[9]=hashMap['i']-counts[8]-counts[6]-counts[5]
            result+='9'*counts[9]
        return ''.join(sorted(result))