#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    c_a = 0
    c_b = 0
    for i in range(0,len(a)):
        if a[i] > b[i] : c_a = c_a + 1
        if b[i] > a[i] : c_b = c_b + 1
    return c_a,c_b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
