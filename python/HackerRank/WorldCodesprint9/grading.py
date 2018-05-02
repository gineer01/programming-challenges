#!/bin/python3

import sys
import math


n = int(input().strip())


def round_up(grade):
    if grade < 38:
        return grade

    upper = math.ceil(grade/5) * 5
    if upper - grade < 3:
        return upper
    else:
        return grade


for a0 in range(n):
    grade = int(input().strip())

    print(round_up(grade))
