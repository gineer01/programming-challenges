import fileinput

f = fileinput.input()

cases = int(next(f))
next(f)

def check_horizontal(grid, m, n, i, j, word):
    l = len(word)
    if j + l <= n:
        if grid[i][j:j + l] == word:
            return True

    if j + 1 - l >= 0:
        if grid[i][j:j - l:-1] == word:
            return True

def check_vertical(grid, m, n, i, j, word):
    l = len(word)
    if i + l <= m:
        if "".join(grid[r][j] for r in range(i, i + l)) == word:
            return True

    if i + 1 - l >= 0:
        if "".join(grid[r][j] for r in range(i, i - l, -1)) == word:
            return True

    return False

def check_diagonal(grid, m, n, i, j, word):
    l = len(word)
    if i + l <= m and j + l <= n:
        if "".join(grid[i + r][j + r] for r in range(l)) == word:
            return True

    if i + 1 - l >= 0 and j + 1 - l >= 0:
        if "".join(grid[i - r][j - r] for r in range(l)) == word:
            return True
    return False

def check_rdiagonal(grid, m, n, i, j, word):
    l = len(word)
    if i + l <= m and j + 1 - l >= 0:
        if "".join(grid[i + r][j - r] for r in range(l)) == word:
            return True

    if i + 1 - l >= 0 and j + l <= n:
        if "".join(grid[i - r][j + r] for r in range(l)) == word:
            return True

    return False


directions = [check_horizontal, check_vertical, check_diagonal, check_rdiagonal]
def find(grid, m, n, word):
    first_c = word[0]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == first_c:
                for d in directions:
                        if d(grid, m, n, i, j, word):
                            return (i, j)

    return None

def solve(m, n, grid, k, words):
    # print(grid, words)
    result = []
    for w in range(k):
        word = words[w]
        result.append(find(grid, m, n, word))

    for r in result:
        if r:
            print(r[0] + 1, r[1] + 1)
        else:
            raise Exception("Couldn't find a word")


def process_case(f):
    m, n = list(map(int, next(f).split()))
    grid = [next(f).strip().upper() for i in range(m)]
    k = int(next(f))
    words = [next(f).strip().upper()  for i in range(k)]

    solve(m, n, grid, k, words)


process_case(f)
for i in range(1, cases):
    next(f)
    print()
    process_case(f)

