import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    lys = list(word)
    index = []
    for i in lys:
        index.append(ord(i)-97)
    keys = []
    for i in index:
        keys.append(h[i])
    return max(keys)*len(keys)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
