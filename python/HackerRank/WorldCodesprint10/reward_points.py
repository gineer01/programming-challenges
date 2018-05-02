#!/bin/python3

def getPoints(swipes):
    return sum(min(100, x * 10) for x in swipes)

swipes = [int(s) for s in input().split()]
print(getPoints(swipes))
