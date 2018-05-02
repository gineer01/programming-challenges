import fileinput
import itertools
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

f = fileinput.input()

t = int(next(f))

ERDOS = 'Erdos, P.'

def solve(papers, names):
    adjacency = Graph()

    for p in papers:
        authors = get_authors(p)
        # print(authors)
        for a in authors:
            for co in authors:
                # adjacency.setdefault(a, set()).update(authors)
                adjacency.add_edge(a, co, True)

    erdos = {}

    def cal_erdos(parent, child, edge):
        if parent:
            erdos[child] = erdos[parent] + 1
        else:
            erdos[child] = 0

    adjacency.bfs(ERDOS, cal_erdos)

    for n in names:
        print("{} {}".format(n, erdos.get(n, 'infinity')))


def get_authors(p):
    import re
    authors = p.split(':')[0]
    return re.split(r'(?<=\.)\s*, ', authors)


def solve_case(f):
    l = next(f).strip()
    if not l:
        l = next(f).strip()

    p, n = map(int, l.split())
    papers = list(itertools.islice(f, p))
    names = [l.strip() for l in itertools.islice(f, n)]

    solve(papers, names)

for i in range(t):
    print("Scenario {}".format(i + 1))
    solve_case(f)
