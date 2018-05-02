import fileinput
import math

f = fileinput.input()

t = int(next(f))


def solve(m, n, costs):
    def min_pay(i, j):
        if i == 0:
            return today_cost(0, (j + 1))

        temp = []
        for k in range(j + 2):
            this_day = today_cost(i, k)
            prev_day = pay[i - 1][j - k + 1]
            temp.append(this_day + prev_day)

        return min(temp)

    def today_cost(i, k):
        if k > m:
            return math.inf
        return sum(costs[i][:k]) + k ** 2

    pay = [[math.inf for j in range(n)] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                break

            pay[i][j] = min_pay(i, j)
    return pay[n - 1][0]


for i in range(t):
    n, m = map(int, next(f).split())
    costs = []
    for j in range(n):
        costs.append([c for i, c in enumerate(sorted(map(int, next(f).strip().split())), start=1)])
    print("Case #{}: {}".format(i + 1, solve(m, n, costs)))

