#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    A=list(a)
    B=list(b)
    a=list(a)
    for i in a:
        if i in B:
            A.remove(i)
            B.remove(i)
    return (len(A) + len(B))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
