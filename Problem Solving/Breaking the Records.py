#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    ma = scores[0]
    cma = 0
    cmi = 0
    mi = scores[0]
    for i in range(0,len(scores)):
        if scores[i] > ma :
            ma = scores[i]
            cma = cma + 1
        if scores[i]<mi:
            mi = scores[i]
            cmi = cmi + 1
    return cma , cmi
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
