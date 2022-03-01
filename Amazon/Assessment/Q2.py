#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxFreqDeviation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMaxFreqDeviation(s):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getMaxFreqDeviation(s)

    fptr.write(str(result) + '\n')

    fptr.close()
