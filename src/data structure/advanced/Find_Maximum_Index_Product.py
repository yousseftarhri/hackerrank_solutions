#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    left_side_index = [0] * len(arr)
    stack_left = []
    right_side_index = [0] * len(arr)
    stack_right = []
    for i in range(len(arr)):
        while stack_left and arr[stack_left[-1]] <= arr[i]:
            stack_left.pop()

        if stack_left:
            left_side_index[i] = stack_left[-1] + 1

        stack_left.append(i)

    for i in range(len(arr) - 1, -1, -1):
        while stack_right and arr[stack_right[-1]] <= arr[i]:
            stack_right.pop()

        if stack_right:
            right_side_index[i] = stack_right[-1] + 1

        stack_right.append(i)

    index_product = []
    for i, e in zip(left_side_index, right_side_index):
        index_product.append(i * e)
    print(index_product)
    return max(index_product)

    """for i in range(len(arr)):
        left=0
        right=0

        if i == 0:
            if i==len(arr)-1:
                break
            continue
        for e in range(len(arr[i+1:])):
            if arr[i+1:][e] > arr[i]:
                right=len(arr[:i+1]) + e+1
                break
        for e in range(len(arr[:i]) -1,-1,-1):
            if arr[e]>arr[i]:
                left = e+1
                break

        index_product.append(left*right)"""


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
