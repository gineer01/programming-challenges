import fileinput

import collections

f = fileinput.input()

SIZE = 4
TILES = SIZE**2

n = int(next(f))


def get_path(visited, board):
    r = []
    node = board

    while True:
        next_node = visited[node]
        if next_node:
            node, s = next_node
        else:
            break
        r.append(s)

    return "".join(r)


def swap(node, to_swap, swap_target):
    def to_index(x_y):
        return x_y[1] * SIZE + x_y[0]
    l = list(node)
    i = to_index(to_swap)
    j = to_index(swap_target)
    l[i], l[j] = l[j], l[i]
    return tuple(l)


def find_next(node):
    x, y = hole_coord(node)
    if x > 0:
        op = 'R'
        swap_target = x - 1, y
        yield swap(node, (x, y), swap_target), op
    if x < (SIZE - 1):
        op = 'L'
        swap_target = x + 1, y
        yield swap(node, (x, y), swap_target), op
    if y > 0:
        op = 'D'
        swap_target = x, y - 1
        yield swap(node, (x, y), swap_target), op
    if y < (SIZE - 1):
        op = 'U'
        swap_target = x, y + 1
        yield swap(node, (x, y), swap_target), op


def hole_coord(node):
    i = node.index(0)
    x, y = i % SIZE, i // SIZE
    return x, y


# http://mathworld.wolfram.com/15Puzzle.html
def get_permutation_parity(perm):
    count = 0
    for k in range(TILES):
        i = perm[k]
        if i == 0:
            continue

        for j in range(k + 1, TILES):
            if perm[j] == 0:
                continue
            if perm[j] < i:
                count += 1
    return count

assert get_permutation_parity((13, 10, 11, 6, 5, 7, 4, 8, 1, 12, 14, 9, 3, 15, 2, 0)) == 59


def is_solvable(start_board):
    x, y = hole_coord(start_board)
    e = get_permutation_parity(start_board)
    return (e + y  + 1) % 2 == 0


def solve():
    end_state = tuple((i + 1) % TILES for i in range(TILES))
    visited = {}

    start_board = yield

    q = collections.deque()
    q.append(end_state)
    visited[end_state] = None

    while len(q) > 0:
        while not is_solvable(start_board):
            print("This puzzle is not solvable.")
            start_board = yield

        while start_board in visited:
            print(get_path(visited, start_board))
            start_board = yield

        node = q.popleft()

        for c, s in find_next(node):
            if c in visited:
                continue
            else:
                visited[c] = node, s
                q.append(c)

            if c == start_board:
                print(get_path(visited, start_board))
                start_board = yield

    return None


solver = solve()
next(solver)

for i in range(n):
    board = []
    for j in range(SIZE):
        board.extend(map(int, next(f).split()))
    solver.send(tuple(board))

solver.close()