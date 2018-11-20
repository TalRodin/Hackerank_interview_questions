#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley=0
    mountain=0
    for i in s:
        if i=='U':
            mountain+=1
        if i=='D':
            mountain+=-1
        if mountain==0 and i=='U':
            valley+=1
    return (valley)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()