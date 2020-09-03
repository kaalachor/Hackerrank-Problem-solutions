import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    s_n = str(n)
    c = 0
    for char in s_n:
        if int(char) == 0 : pass
        elif n%int(char) == 0 : c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
