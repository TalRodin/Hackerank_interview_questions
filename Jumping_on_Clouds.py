#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    j = 0
    i = 0
    while(i < n - 2):
        if c[i + 2] != 1:
            i += 2
            j += 1
        else:
            i +=1
            j += 1
    if i == n - 2:
        j += 1
    return(j)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()