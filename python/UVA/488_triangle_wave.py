import fileinput

f = fileinput.input()

t = int(next(f))


def print_wave(amplitude):
    for i in range(amplitude):
        k = i + 1
        print(str(k) * k)
    for i in range(amplitude - 1):
        k = amplitude - 1 - i
        print(str(k) * k)


def solve(amplitude, frequency):
    for i in range(frequency):
        print_wave(amplitude)
        if i + 1 != frequency:
            print()


for i in range(t):
    next(f)
    amplitude = int(next(f))
    frequency = int(next(f))

    solve(amplitude, frequency)
    if i + 1 != t:
        print()
