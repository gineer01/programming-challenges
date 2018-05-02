#!/bin/python3


def minimumDeletions(n, a):
    if n < 3:
        return 0

    count = 0
    i = 2
    last_pair = a[1] - a[0]
    last_i = 1
    while i < n:
        current_pair = a[i] - a[last_i]

        if current_pair * last_pair > 0:
            count += 1
            last_i = i
            i += 1
        else:
            last_pair = current_pair
            last_i = i
            i += 1

    return count

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Return the minimum number of elements to delete to make the array zigzag
print(minimumDeletions(n, a))
