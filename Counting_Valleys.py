#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    uphill=0
    downhill=0
    for i in s:
        if i=='U':
            uphill+=1
        if i =='D':
            uphill-=1
        if uphill==0 and i=='U':
            downhill+=1
    return (downhill)
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
