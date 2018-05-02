#!/bin/python3

import sys


n, k = map(int, input().strip().split(' '))
rQueen, cQueen = map(int, input().strip().split(' '))

rows = []
cols = []
diag = []
rdiag = []

for i in range(k):
    rObstacle,cObstacle = map(int, input().strip().split(' '))
    if rObstacle == rQueen:
        rows.append(cObstacle)
    elif cObstacle == cQueen:
        cols.append(rObstacle)
    elif (rObstacle + cObstacle) == (rQueen + cQueen):
        diag.append(rObstacle)
    elif (rObstacle - cObstacle) == (rQueen - cQueen):
        rdiag.append(rObstacle)


def count_attack(pos, p):
    import bisect
    pos.sort()
    i = bisect.bisect(pos, p)
    if i == 0:
        left = 0
    else:
        left = pos[i - 1]

    if i == len(pos):
        right = n + 1
    else:
        right = pos[i]

    return right - left - 2


sum_attack = count_attack(rows, cQueen)
sum_attack += count_attack(cols, rQueen)


def count_attack_diag(diag, rQueen, cQueen):
    import bisect
    diag.sort()
    i = bisect.bisect(diag, rQueen)
    if i == 0:
        left = max(0, rQueen + cQueen - n - 1)
    else:
        left = diag[i - 1]

    if i == len(diag):
        right = min(n + 1, rQueen + cQueen)
    else:
        right = diag[i]

    return right - left - 2


def count_attack_rdiag(diag, rQueen, cQueen):
    import bisect
    diag.sort()
    i = bisect.bisect(diag, rQueen)
    if i == 0:
        left = max(0, rQueen - cQueen)
    else:
        left = diag[i - 1]

    if i == len(diag):
        right = min(n + 1, rQueen - cQueen + n + 1)
    else:
        right = diag[i]

    return right - left - 2


sum_attack += count_attack_diag(diag, rQueen, cQueen)
sum_attack += count_attack_rdiag(rdiag, rQueen, cQueen)
print(sum_attack)