#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apc = 0
    for i in range(0,len(apples)):
        if s<= a + int(apples[i]) <= t : apc = apc + 1
    
    bpc = 0
    for i in range(0,len(oranges)):
        if s<= b + int(oranges[i]) <= t : bpc = bpc + 1

    return print(str(apc) + '\n' + str(bpc))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
