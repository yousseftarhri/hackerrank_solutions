# !/bin/python3
#https://www.hackerrank.com/challenges/x-and-his-shots/problem?isFullScreen=true
import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY shots
#  2. 2D_INTEGER_ARRAY players
#

def solve(shots, players):
    # Write your code here
    shots.sort(key=lambda x: x[0])
    players.sort(key=lambda x: x[0])
    s = 0
    for p_start, p_end in players:
        for s_start, s_end in shots:

            if p_start > s_end:
                continue
            elif p_end < s_start:
                break
            else:
                s = s + 1
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
