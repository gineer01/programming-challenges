import fileinput

f = fileinput.input()


def solve(n, k):
    if k >= 2*n:
        return 0


    max_line = 2*n - 1

    def search(diagonal, r_diagonal, start, t):
        def find_placement():
            for i in range(start, max_line - t + 1):
                for y in range(0, n):
                    x = i - y
                    if x < 0:
                        break
                    if x >= n:
                        continue
                    if r_diagonal[x - y]:
                        continue
                    yield x, y

        if t == 1:
            for pos in find_placement():
                # yield (pos,)
                nonlocal count
                count += 1
            return

        for pos in find_placement():
            new_diagonal = diagonal.copy()
            new_r_diagonal = r_diagonal.copy()
            new_diagonal[pos[0] + pos[1]] = True
            new_r_diagonal[pos[0] - pos[1]] = True

            search(new_diagonal, new_r_diagonal, pos[0] + pos[1] + 1, t - 1)

    count = 0
    search([False] * max_line, [False] * max_line, 0, k)
    return count

assert solve(2, 1) == 4


for l in f:
    n, k = map(int, l.split())
    if n == 0 and k == 0:
        break
    print(solve(n, k))

