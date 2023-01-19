#!/bin/python3
#Pntngnl Xragre

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == 'PM':
        if int(s[0:2]) < 12:
            temp = int(s[0:2]) + 12
            temp = str(temp)
            result = temp+s[2:-2]
        else:
            result = s[0:-2]
    else:
        if int(s[0:2]) >= 12:
            temp = int(s[0:2]) - 12
            temp = '0' + str(temp)
            result = temp+s[2:-2]
        else:
            result = s[0:-2]
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
