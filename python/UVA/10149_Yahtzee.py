import fileinput
import itertools
import functools

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, u, v, data):
        self.vertices.add(u)
        self.vertices.add(v)

        self.edges.setdefault(u, {})[v] = data

    def remove_edge(self, u, v):
        return self.edges[u].pop(v, None)

    def bfs(self, start_node, node_func):
        """
        Do BFS and for each node, call node_func
        :param start_node:
        :param node_func: a function that takes parent node, child node, and edge data
        :return: None
        """
        import collections

        visited = set()

        q = collections.deque()
        q.append(start_node)
        node_func(None, start_node, None)

        while len(q) > 0:
            node = q.popleft()

            for c in self.edges[node]:
                if c in visited:
                    continue
                else:
                    node_func(node, c, self.edges[node][c])
                    visited.add(c)
                    q.append(c)

    def dijkstra(self, start):
        """
        Find shortest paths to all vertices
        :param start: start node
        :return: D, P where where D[v] is the distance
            from start to v and P[v] is the predecessor of v along
            the shortest path from s to v.
        """
        import heapq

        D = {}
        P = {}

        q = [(0, start, None)] # initial heap
        visited = set()

        while len(q) > 0:
            (cost, v, parent) = heapq.heappop(q)
            if v not in visited:
                visited.add(v)
                D[v] = cost
                P[v] = parent

                for c in self.edges.get(v, []):
                    if c not in visited:
                        item = (cost + self.edges[v][c], c, v)
                        heapq.heappush(q, item)

        return D, P

def solve_minimum_assignment(edge_cost, n):
    SOURCE = ("s", 0)

    SINK = ("t", 0)

    def reduce_cost(x, y, p, edge_cost):
        return p[x] + edge_cost - p[y]


    def get_edge_cost(edge_cost, x, y):
        return edge_cost[x[1]][y[1]]

    def update_matching(v, u, M, g):
        if v[0] == 'x' and u[0] == 'y':
            M[v[1]] = u[1]

            g.remove_edge(v, u)
            g.add_edge(u, v, 0) #cost to be updated later

        elif v[0] == 'y' and u[0] == 'x':
            del M[u[1]]

            g.remove_edge(v, u)
            g.add_edge(u, v, 0) #cost to be updated later
        else:
            raise Exception("Not an X-Y edge")


    def update_cost(n, g, p, edge_cost):
        for i in range(n):
            for j in range(n):
                x = x_node(i)
                y = y_node(j)
                if x in g.edges and y in g.edges[x]:
                    g.add_edge(x, y, reduce_cost(x, y, p, get_edge_cost(edge_cost, x, y)))
                else:
                    assert g.edges[y][x] == 0

    def x_node(i):
        return ("x", i)

    def y_node(i):
        return ("y", i)

    def augment_path(n, M, P, g):
        u = SINK
        v = P[u]
        path = []

        while v and v != SOURCE:
            if u != SINK:
                path.append((v, u))

            u = v
            v = P[u]

        path.reverse()
        for p in path:
            update_matching(p[0], p[1], M, g)

        vals = set(M.values())
        for i in range(n):
            x = x_node(i)
            if i in M:
                g.remove_edge(SOURCE, x)
            else:
                g.add_edge(SOURCE, x, 0)

            y = y_node(i)
            if i in vals:
                g.remove_edge(y, SINK)
            else:
                g.add_edge(y, SINK, 0)

        assert len(M.keys()) == len(set(M.values())), M

    M = {}
    p = {}
    for i in range(n):
        p[x_node(i)] = 0
        p[y_node(i)] = min(edge_cost[j][i] for j in range(n))

    g = Graph()
    for i in range(n):
        g.add_edge(SOURCE, x_node(i), 0)
        g.add_edge(y_node(i), SINK, 0)

        for j in range(n):
            x = x_node(i)
            y = y_node(j)
            g.add_edge(x, y, reduce_cost(x, y, p, get_edge_cost(edge_cost, x, y)))

    while len(M) < n:
        D, P = g.dijkstra(SOURCE)
        augment_path(n, M, P, g)

        for k in p:
            p[k] = D[k] + p[k]
        update_cost(n, g, p, edge_cost)
        # print(M)
    return M



BONUS_THRESHOLD = 63

f = fileinput.input()


def of_a_kind(counter, required_num, result):
    count = counter.most_common(1)[0][1]
    if count == required_num:
        return result
    else:
        return 0


def full_house(counter):
    counts = counter.most_common(2)
    if counts[0][1] == 3 and counts[1][1] == 2:
        return 40
    else:
        return 0


LONGS = [set(range(i, i + 5)) for i in [1, 2]]
def long_straight(r):
    s = set(r)
    if any(s.issuperset(t) for t in LONGS):
        return 35
    else:
        return 0


SHORTS = [set(range(i, i + 4)) for i in range(1, 4)]
def short_straight(r):
    s = set(r)
    if any(s.issuperset(t) for t in SHORTS):
        return 25
    else:
        return 0


@functools.lru_cache()
def get_value(r):
    import collections
    counter = collections.Counter(r)
    one_to_six = [i * counter.get(i, 0) for i in range(1,7)]
    sum_of_dices = sum(r)
    others = [sum_of_dices,
              of_a_kind(counter, 3, sum_of_dices),
              of_a_kind(counter, 4, sum_of_dices),
              of_a_kind(counter, 5, 50),
              short_straight(r),
              long_straight(r),
              full_house(counter)]
    return tuple(one_to_six + others)


def get_values(rounds):
    values = [get_value(r) for r in rounds]
    return values


def convert(game, positions):
    rounds = [game[i] for i in positions]
    return rounds




def find_max_matching(values):
    MAX = 50
    n = len(values)

    #Convert to min matrix because the algorithm is for finding min matching
    edge_cost = [[MAX - i for i in v] for v in values]

    return solve_minimum_assignment(edge_cost, n)


def find_max_perm(rounds):
    if len(rounds) == 1:
        return (rounds[0][0], (rounds[0][0],))

    max_val = max(r[0] for r in rounds)
    max_rounds = set(r for r in rounds if r[0] == max_val)

    max_perm_val = 0
    max_perm = tuple()
    for t in max_rounds:
        rounds_copy = list(rounds)
        rounds_copy.remove(t)
        sub_rounds = [r[1:] for r in rounds_copy]
        sub_rounds_result = find_max_perm(sorted_tuple(sub_rounds))
        val = max_val + sub_rounds_result[0]

        if val > max_perm_val:
            max_perm_val = val
            max_perm = (max_val,) + sub_rounds_result[1]

    return max_perm_val, max_perm

def solve_left(game, r):
    rounds = sorted_tuple(get_values(convert(game, r)))
    result = find_max_perm(rounds)
    return result


def sorted_tuple(l):
    return tuple(sorted(l))


def get_result(values, match):
    n = len(match)
    result = {match[i]:values[i][match[i]] for i in range(n)}
    l = [result[i] for i in range(n)]
    return l


def likely_have_bonus(subvalues):
    n = len(subvalues)
    max_sum = sum((max(subvalues[j][i] for j in range(n)) for i in range(n)))
    return max_sum >= BONUS_THRESHOLD


def attempt_bonus(values, max_result):
    positions = set(range(13))

    max_val = max_result[-1]
    for r in itertools.combinations(positions, 6):
        subvalues = [values[i][:6] for i in r]

        if not likely_have_bonus(subvalues):
            continue

        M = find_max_matching(subvalues)
        l = get_result(subvalues, M)

        if sum(l) < BONUS_THRESHOLD:
            continue

        # print("Some hope", max_result)

        other = positions - set(r)
        other_values = [values[i][6:] for i in other]

        M2 = find_max_matching(other_values)
        l2 = get_result(other_values, M2)

        l.extend(l2)
        l.append(35)
        l.append(sum(l))

        if l[-1] > max_val:
            max_val = l[-1]
            max_result = l

    print(" ".join(map(str, max_result)))


def solve(game):
    values = get_values(game)
    perm = find_max_matching(values)
    # print(perm)
    l = get_result(values, perm)
    l.append(35 if sum(l[0:6]) >= BONUS_THRESHOLD else 0)
    l.append(sum(l))
    if l[-2] == 35:
        print(" ".join(map(str, l)))
        return
    else:
        attempt_bonus(values, l)


for l in f:
    game = [l.strip()]
    game.extend([l.strip() for l in itertools.islice(f, 12)])

    solve([tuple(sorted(map(int, r.split()))) for r in game])
