import fileinput


def solve(n, m):
    accuml = []
    for i in range(n + 1):
        accuml.append([0] * (n + 1))
    # print(accuml)

    for c in range(n):
        for r in range(n):
            accuml[r + 1][c + 1] = accuml[r][c + 1] + sum(m[r*n : r*n + c + 1])


    #Calculate the sum of a sub-rectangle from col1, col2, row1, row2
    def cal_sum(col1, col2, row1, row2):
        return accuml[row2][col2] + accuml[row1 - 1][col1 - 1] - accuml[row2][col1 - 1] - accuml[row1 - 1][col2]


    #Use dynamic programming to find max sub-rectangle between col1 and col2 in O(n)
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    def find_max(col1, col2):
        A = [cal_sum(col1 + 1, col2 + 1, row + 1, row + 1) for row in range(0, n)]
        # print(A)
        max_ending_here = max_so_far = A[0]

        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # print(accuml)
    # print(cal_sum(1, 2, 2, 4))
    # print(find_max(0, 1))
    max_val = 0
    for col1 in range(0, n - 1):
        for col2 in range(col1 + 1, n):
            val = find_max(col1, col2)
            if val > max_val:
                max_val = val
                # print(col1, col2, row1, row2)

    return max_val



def main():
    f = fileinput.input()
    n = int(next(f))
    m = []
    for l in f:
        m.extend(int(x) for x in l.split())

    # print(n, m)
    print(solve(n, m))


main()
