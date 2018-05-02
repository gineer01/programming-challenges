import fileinput

f = fileinput.input()

lines = ["`1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./"]
m = {}
for l in lines:
    for i in range(len(l) - 1):
        m[l[i + 1]] = l[i]

def decode(c):
    return m.get(c, c)

def solve(l):
    return "".join(decode(c) for c in l)


for l in f:
    print(solve(l), end='')
