import fileinput
import bisect

f = fileinput.input()

t = int(next(f))



def solve(n, r, coords):
    sort_x = sorted(coords, key=lambda x: x[1])
    sort_y = sorted(coords, key=lambda x: x[2])
    key_x = [c[1] for c in sort_x]
    key_y = [c[2] for c in sort_y]
    # print(n, r, coords, sort_x, sort_y)

    def get_sets(n, key, sort_coords):
        result = []
        for x in key:
            left = bisect.bisect_left(key, x)
            right = bisect.bisect_right(key, x + r)
            result.append(set(c[0] for c in sort_coords[left:right]))

            if right == n:
                break
        return result

    squares = []
    for x_set in get_sets(n, key_x, sort_x):
        for y_set in get_sets(n, key_y, sort_y):
            squares.append(x_set & y_set)

    if len(squares) == 1:
        return len(squares[0])

    squares.sort(key=lambda x: len(x), reverse=True)
    # print(squares)
    max_size = 0
    for i in range(len(squares)):
        len_i = len(squares[i])

        for j in range(i + 1, len(squares)):
            l = len(squares[i] | squares[j])
            if max_size < l:
                max_size = l

            estimate = len_i + len(squares[j])
            if estimate <= max_size:
                break
            if max_size == n:
                return max_size
    return max_size




for i in range(t):
    n, r = map(int, next(f).split())
    coords = []
    for j in range(n):
        coords.append((j,) + tuple(map(int, next(f).split())))
    print("Case #{}: {}".format(i + 1, solve(n, r, coords)))

