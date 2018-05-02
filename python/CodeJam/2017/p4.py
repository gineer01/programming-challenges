import fileinput




def get_rdiag(r, c):
    return r - c


def solve(case_no, n, models):
    # print(n, m, l)
    rows = [False] * n
    cols = [False] * n
    diag = [False] * (2*n - 1)
    rdiag = [False] * (2*n - 1)

    def update_row(m, r):
        update_line(m, r, '+', rows)

    def update_col(m, c):
        update_line(m, c, '+', cols)

    def update_diag(m, d):
        update_line(m, d, 'x', diag)

    def update_rdiag(m, d):
        update_line(m, d, 'x', rdiag)

    def update_line(m, c, required_model='+', line=cols):
        if m != required_model:
            line[c] = True

    def update_grid(m, r, c):
        grid[r][c] = m
        update_row(m, r)
        update_col(m, c)
        update_diag(m, get_diag(r, c))
        update_rdiag(m, get_rdiag(r, c))

    grid = [[None] * n for i in range(n)]
    for model in models:
        r = int(model[1]) - 1
        c = int(model[2]) - 1
        m = model[0]
        update_grid(m, r, c)

    upgrades = []
    def add_upgrade(m, r, c):
        upgrades.append((m, r, c))
        update_grid(m, r, c)

    def check_upgrade(r, c):
        m = grid[r][c]
        if m:
            if m == 'o':
                return
            elif m == 'x':
                if not diag[get_diag(r, c)] and not rdiag[get_rdiag(r, c)]:
                    add_upgrade('o', r, c)
            else:
                if not rows[r] and not cols[c]:
                    add_upgrade('o', r, c)
        else:
            if not rows[r] and not cols[c] and not diag[get_diag(r, c)] and not rdiag[get_rdiag(r, c)]:
                add_upgrade('o', r, c)
            elif not rows[r] and not cols[c]:
                add_upgrade('x', r, c)
            elif not diag[get_diag(r, c)] and not rdiag[get_rdiag(r, c)]:
                add_upgrade('+', r, c)

    for r in range(n):
        for c in range(n):
            check_upgrade(r, c)

    val = 0
    for r in range(n):
        for c in range(n):
            m = grid[r][c]
            if m:
                if m == 'o':
                    val += 2
                else:
                    val += 1

    print("Case #%s:" % case_no, val, len(upgrades))
    for u in upgrades:
        print(u[0], u[1] + 1, u[2] + 1)

def get_diag(r, c):
    return r + c

# solve(3, 3, 4, [['+', '2', '3'], ['+', '2', '1'], ['x', '3', '1'], ['+', '2', '2']])

f = fileinput.input()
t = int(next(f))
for i in range(t):
    n, m = [int(s) for s in next(f).split()]
    l = []
    for j in range(m):
        l.append(next(f).split())
    solve(i + 1, n, l)