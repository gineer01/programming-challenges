#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())


def cal_weights(s):
    def weight(s):
        return ord(s) - ord('a') + 1


    weights = set()
    l = len(s)

    i = 0
    j = i + 1
    weights.add(weight(s[i]))
    while j < l:
        if s[j] != s[i]:
            i = j
            j = i + 1
            weights.add(weight(s[i]))
            continue
        else:
            weights.add(weight(s[i]) * (j - i + 1))
            j += 1

    return weights



weights = cal_weights(s)
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    if x in weights:
        print("Yes")
    else:
        print("No")

