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
        visited.add(start_node)

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



if __name__ == "__main__":
    g = Graph()
    g.add_edge('a', 'w', 14)
    g.add_edge('a', 'x', 7)
    g.add_edge('a', 'y', 9)
    g.add_edge('b', 'w', 9)
    g.add_edge('b', 'z', 6)
    g.add_edge('w', 'a', 14)
    g.add_edge('w', 'b', 9)
    g.add_edge('w', 'y', 2)
    g.add_edge('x', 'a', 7)
    g.add_edge('x', 'y', 10)
    g.add_edge('x', 'z', 15)
    g.add_edge('y', 'a', 9)
    g.add_edge('y', 'w', 2)
    g.add_edge('y', 'x', 10)
    g.add_edge('y', 'z', 11)
    g.add_edge('z', 'b', 6)
    g.add_edge('z', 'x', 15)
    g.add_edge('z', 'y', 11)

    print(g.dijkstra('a'))