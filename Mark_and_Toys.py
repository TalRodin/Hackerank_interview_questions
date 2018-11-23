#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sum=0
    total=0
    
    list.sort(prices)
    for i in range(len(prices)):
        if sum+prices[i]<=k:
            sum=sum+prices[i]
            total=total+1
        else:
            break
    return(total)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
