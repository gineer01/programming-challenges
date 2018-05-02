import fileinput


def check_sort(n, l):
    for i in range(n - 1):
        if l[i] > l[i + 1]:
            return i
    return "OK"


def solve(n, l):
    sorted_l = trouble_sort(l, n)

    return check_sort(n, sorted_l)


def trouble_sort(l, n):
    even = l[0::2]
    odd = l[1::2]
    even.sort()
    odd.sort()
    merge = []
    for i in range(n):
        is_even = i % 2 == 0
        if is_even:
            merge.append(even[i // 2])
        else:
            merge.append(odd[i // 2])
    return merge


def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        n = int(next(f))
        l = [int(x) for x in next(f).split()]
        print("Case #%s: %s" % (i + 1, solve(n, l)))


main()
