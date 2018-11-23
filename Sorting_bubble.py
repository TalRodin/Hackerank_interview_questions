import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count=0
    for i in range(0, len(a)-1,1):
        for j in range(0, len(a)-1-i,1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                count+=1
    print(a)
    print("Array is sorted in",count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1]) 
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
    print(a)

    countSwaps(a)

