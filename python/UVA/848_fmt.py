import fileinput
import collections

LIMIT = 72

f = fileinput.input()


def break_line(buffer, q):
    pos = buffer.rfind(' ', 0, LIMIT + 1)
    if pos != -1:
        q.append(buffer[:pos].rstrip(' '))
        return buffer[pos:].lstrip()
    else:
        pos = buffer.find(' ', LIMIT)
        if pos == -1:
            q.append(buffer)
            return ""
        else:
            q.append(buffer[:pos].rstrip(' '))
            return buffer[pos:].lstrip()


def add_line(buffer, l, q):
    if buffer.endswith('\n'):
        if (buffer.strip()) and not l.startswith(('\n', ' ')):
            buffer = buffer[:-1] + ' '
        else:
            while len(buffer) > LIMIT:
                buffer = break_line(buffer, q)
            q.append(buffer)
            return l

    buffer += l
    buffer_l = len(buffer)
    if buffer_l <= LIMIT:
        return buffer

    while len(buffer) > 2 * LIMIT:
        buffer = break_line(buffer, q)

    return buffer


def format_line(f):
    q = collections.deque()
    buffer = ""

    for l in f:
        buffer = add_line(buffer, l, q)
        while len(q) > 0:
            yield q.popleft()

    if len(buffer) < LIMIT:
        yield buffer
    else:
        while len(buffer) > LIMIT:
            buffer = break_line(buffer, q)
        q.append(buffer)
        while len(q) > 0:
            yield q.popleft()

for l in format_line(f):
    print(l.rstrip())
