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
    FIELD = int(1e5)

    # Initialize opening and closing arrays
    opening = [0] * FIELD
    closing = [0] * FIELD

    # Read ranges for shots
    for a,b in shots:
        opening[a] += 1
        closing[b + 1] += 1

    # Compute cumulative sums for opening and closing arrays
    for i in range(1, FIELD):
        opening[i] += opening[i - 1]
        closing[i] += closing[i - 1]

    # Calculate the total overlapping shots for all players
    overlapping = 0
    for a,b in players:
        overlapping += opening[b] - closing[a]


    return overlapping
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

