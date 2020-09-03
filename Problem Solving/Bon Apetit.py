#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s = sum(bill)
    b_g = s-bill[k]
    b_actual = b_g/2
    if(b>b_actual):
        return print(int(b-b_actual))
    if(b==b_actual):
        return print('Bon Appetit')

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
