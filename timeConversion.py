#!/bin/python3

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
    stringList = s.split(":")
    if "AM" in stringList[2] and stringList[0] == '12':
        stringList[0] = "00"
    elif "PM" in stringList[2] and stringList[0] != "12":
        stringList[0] = str(int(stringList[0]) + 12)
    stringList[2] = stringList[2][:2]
    s = ":".join(stringList)
    print(s)

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

