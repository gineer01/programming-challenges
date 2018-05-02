import fileinput


def cross(a, b):
    dir = {
        '+x' : {
            '-y' : '-y',
            '+y' : '+y',
            '+z' : '+z',
            '-z' : '-z'
        },
        '-x' : {
            '-y' : '+y',
            '+y' : '-y',
            '+z' : '-z',
            '-z' : '+z'
        },
        '+y' : {
            '-y' : '+x',
            '+y' : '-x',
            '+z' : '+y',
            '-z' : '+y'
        },
        '-y' : {
            '-y' : '-x',
            '+y' : '+x',
            '+z' : '-y',
            '-z' : '-y'
        },
        '+z' : {
            '-y' : '+z',
            '+y' : '+z',
            '+z' : '-x',
            '-z' : '+x'
        },
        '-z' : {
            '-y' : '-z',
            '+y' : '-z',
            '+z' : '+x',
            '-z' : '-x'
        },
    }
    return dir[a][b]


def update_dir(dir, b):
    if b == 'No':
        return dir

    return cross(dir, b)


def solve(n, bends):
    dir = '+x'

    for b in bends:
        dir = update_dir(dir, b)

    return dir


def main():
    f = fileinput.input()
    for l in f:
        n = int(l)
        if n == 0:
            return

        bends = next(f).strip().split()
        print(solve(n, bends))

main()
