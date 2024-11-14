#!/bin/python3
#https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem?isFullScreen=true
import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    stack = deque()
    sum_ = 0

    for i in range(len(arr)):
        while stack and stack[-1][0] < arr[i]:
            stack.pop()

        if stack and arr[i] == stack[-1][0]:
            sum_ += stack[-1][1]
            stack[-1] = (arr[i], stack[-1][1] + 1)

        else:
            stack.append((arr[i], 1))

    return sum_ * 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
