import fileinput
import collections

f = fileinput.input()

my_dict = set()
for l in f:
    if l.strip():
        my_dict.add(l.strip())
    else:
        break


def print_path(visited, dest):
    result = []
    node = dest

    while node:
        result.append(node)
        node = visited[node]

    result.reverse()
    for r in result:
        print(r)


def find_word_at(word, i):
    import string
    w = list(word)
    for new_c in string.ascii_lowercase:
        w[i] = new_c
        new_w = ''.join(w)
        if new_w in my_dict:
            yield new_w


def find_word(c):
    for i in range(len(c)):
        for w in find_word_at(c, i):
            yield w


def find_path(src, dest):
    visited = {}

    q = collections.deque()
    q.append(src)
    visited[src] = None

    while len(q) > 0:
        node = q.popleft()

        for c in find_word(node):
            if c in visited:
                continue
            else:
                visited[c] = node
                q.append(c)

            if c == dest:
                print_path(visited, dest)
                return

    print("No solution.")

src, dest = next(f).strip().split()
find_path(src, dest)

for l in f:
    print()
    src, dest = l.strip().split()
    find_path(src, dest)

