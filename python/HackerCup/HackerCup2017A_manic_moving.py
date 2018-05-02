import fileinput
import math

f = fileinput.input()

t = int(next(f))


def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                new_dist = dist[i][k] + dist[k][j]
                if dist[i][j] > new_dist:
                    dist[i][j] = new_dist



def solve(m, n, k, dist, families):
    floyd_warshall(n, dist)

    def get_source(f):
        return families[f][0]

    def get_dest(f):
        return families[f][1]

    def find_cost(start):
        if k == 1:
            return dist[start][get_source(0)] + dist[get_source(0)][get_dest(0)]

        costs = [[math.inf for i in range(2)] for j in range(k)]
        DELIVER = 0
        PICK = 1
        costs[k - 1][DELIVER] = dist[get_source(k - 1)][get_dest(k - 1)]
        costs[k - 1][PICK] = dist[get_dest(k - 2)][get_dest(k - 1)]

        def cal_min_cost(starting, i):
            s1 = starting
            s2 = get_source(i + 1)
            d1 = get_dest(i)
            deliver = dist[s1][d1] + dist[d1][s2] + costs[i + 1][DELIVER]
            pick = dist[s1][s2] + dist[s2][d1] + costs[i + 1][PICK]
            if deliver <= pick:
                return deliver
            else:
                return pick

        for i in range(k - 2, 0, -1):
            costs[i][DELIVER] = cal_min_cost(get_source(i), i)
            costs[i][PICK] = cal_min_cost(get_dest(i - 1), i)

        cost = dist[start][get_source(0)] + cal_min_cost(get_source(0), 0)
        return cost



    cost = find_cost(0)
    if cost == math.inf:
        cost = -1
    return cost



for i in range(t):
    n, m, k = map(int, next(f).split())
    dist = [[0 if i == j else math.inf for i in range(n)] for j in range(n)]
    for j in range(m):
        a, b, g = map(int, next(f).split())
        a -= 1
        b -= 1
        dist[a][b] = min(g, dist[a][b])
        dist[b][a] = min(g, dist[b][a])

    families = []
    for j in range(k):
        s, d = map(int, next(f).split())
        s -= 1
        d -= 1
        families.append((s, d))
    print("Case #{}: {}".format(i + 1, solve(m, n, k, dist, families)))

