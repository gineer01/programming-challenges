import fileinput


def solve(case_id, row, col, grid):
    def solve_rect(start_row, end_row, start_col, end_col):
        def find_quadrant():
            new_row = end_row
            new_col = end_col
            kid = None

            r = start_row
            while r < new_row:
                for c in range(start_col, new_col):
                    if grid[r][c] == '?':
                        continue

                    if not kid:
                        kid = grid[r][c], r, c
                    else:
                        if c < kid[2]:
                            new_col = kid[2]
                            kid = grid[r][c], r, c
                        elif c == kid[2]:
                            new_row = r
                            break
                        elif c < new_col:
                            new_col = c
                            break

                r += 1

            return new_row, new_col, kid

        if start_row == end_row or start_col == end_col:
            return

        nr, nc, k = find_quadrant()
        for r in range(start_row, nr):
            for c in range(start_col, nc):
                if grid[r][c] == '?':
                    grid[r][c] = k[0]
                elif grid[r][c] != k[0]:
                    raise Exception("Wrong" + str(case_id))

        solve_rect(nr, end_row, start_col, nc)
        solve_rect(start_row, end_row, nc, end_col)

    # print("Case #%s:" % (case_id + 1))
    # for r in range(row):
    #     print("".join(grid[r]))

    solve_rect(0, row, 0, col)

    print("Case #%s:" % (case_id + 1))
    for r in range(row):
        print("".join(grid[r]))
    # print("-"*120)

# solve(0, 3, 3, [['G', '?', '?'], ['?', 'C', '?'], ['?', '?', 'J']])
# solve(0, 3, 4, [['C', 'O', 'D', 'E'], ['?', '?', '?', '?'], ['?', 'J', 'A', 'M']])

f = fileinput.input()
t = int(next(f))
for i in range(t):
    r, c = [int(s) for s in next(f).split()]
    grid = [list(next(f).strip()) for i in range(r)]
    # print(i, r, c, grid)
    solve(i, r, c, grid)

