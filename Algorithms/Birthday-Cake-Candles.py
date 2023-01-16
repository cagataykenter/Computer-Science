#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles,candles_count):
    result = []
    for i in range(candles_count):
        if len(result) == 0:
            result.append(candles[i])
        elif len(result) != 0:
            if candles[i] > result[0]:
                result = []
                result.append(candles[i])
            elif candles[i] == result[0]:
                result.append(candles[i])
            elif candles[i] < result[0]:
                continue
    return len(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles,candles_count)

    fptr.write(str(result) + '\n')

    fptr.close()
