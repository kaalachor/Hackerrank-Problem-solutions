#!/bin/python3
from collections import Counter
import operator
import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l = len(arr)
    b = [l]
    cn = sorted(Counter(arr).items(),key = operator.itemgetter(0))
    for i,v in cn:
        l -= v
        if l > 0:
            b.append(l)

    return b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
