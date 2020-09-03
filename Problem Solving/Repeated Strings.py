#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt_a_sub = s.count('a')
    total_sub_in_string = int(n/len(s))
    rem = n%len(s)
    cnt_in_rem = s.count('a',0,rem)
    total_count = cnt_a_sub*total_sub_in_string + cnt_in_rem
    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
