#!/bin/python3

import sys
MODULUS = 10**9 + 7

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, u, v, data):
        self.vertices.add(u)
        self.vertices.add(v)

        self.edges.setdefault(u, {})[v] = data




g = Graph()
n = int(input().strip())
for a0 in range(n-1):
    u,v = map(int, input().strip().split(' '))
    g.add_edge(u, v, True)
    g.add_edge(v, u, True)





def dfs(g, start_node):
    count = 2
    visited = set()

    q = [start_node]
    visited.add(start_node)

    while len(q) > 0:
        node = q.pop()

        has_one = False
        component_count = 0
        for c in g.edges[node]:
            if c in visited:
                continue
            else:
                if len(g.edges[c]) == 1:
                    has_one = True
                    visited.add(c)
                else:
                    component_count += 1
                    visited.add(c)
                    q.append(c)

        if has_one:
            count = (count * 2**(component_count)) % MODULUS
        else:
            count = (count * (2**(component_count) - 1)) % MODULUS

    return count

print(dfs(g, 1))
