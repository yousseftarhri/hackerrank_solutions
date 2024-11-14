#!/bin/python3

import os
import sys


#
# Complete the solve function below.
#
def solve(t):
    #
    # Return the ID
    #
    sum_list = []
    for i in range(len(t)):

        new_list = t[i:] + t[:i]
        # new_list_added = [new_list[0]] + [new_list[e] - e if new_value > 0 else 0 for e in range(1,len(new_list))]
        new_list_added = []
        for e in range(len(new_list[1:])):
            new_value = new_list[e] - e
            if new_value <= 0:
                new_list_added.append(0)

            # else:
            # new_list_added.append(new_value)

        sum_list.append(len(new_list_added))

        print(new_list_added)

    return sum_list.index(max(sum_list)) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
