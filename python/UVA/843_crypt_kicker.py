import fileinput

import functools

f = fileinput.input()

n = int(next(f))

words = {next(f).strip() for i in range(n)}

# print(words)

def print_result(line, result):
    result[' '] = ' '
    plain_text = ''.join([result.get(c, '*') for c in line.strip()])
    print(plain_text)

@functools.lru_cache()
def get_match(regex):
    import re
    compiled_regex = re.compile(regex, re.A | re.I)
    return [w for w in words if compiled_regex.match(w)]

def get_regex(assignment, c):
    regex = ''.join([assignment.get(i, '.') for i in c])
    return "^" + regex + "$"


def select_var(assignment, cypher_text):
    domain = {c : get_match(get_regex(assignment, c)) for c in cypher_text}
    var = min(domain, key=lambda k: len(domain[k]))
    return var, domain[var]


def solve_assignment(assignment, cypher_text):
    if len(cypher_text) == 0:
        return assignment

    var, values = select_var(assignment, cypher_text)

    for val in values:
        assignment_copy = assignment.copy()
        cypher_text_copy = cypher_text.copy()

        result = update_assignment(assignment_copy, cypher_text_copy, var, val)
        if not result:
            continue

        result = solve_assignment(assignment_copy, cypher_text_copy)
        if result:
            return result

    return False


def update_assignment(assignment, cypher_text, var, val):
    for i in range(len(var)):
        k = var[i]
        v = val[i]
        if k in assignment:
            if assignment[k] != v:
                return False
        else:
            assignment[k] = v

    if len(assignment) != len(set(assignment.values())):
        return False

    cypher_text.remove(var)
    return True


def solve(l):
    cypher_text = l.strip().split()
    #print(cypher_text)

    assignment = {}

    result = solve_assignment(assignment, cypher_text)

    if result:
        print_result(l, result)
    else:
        print_result(l, {})


for l in f:
    solve(l)

# Testing

# print(get_match({}, 'pnetfn'))
#
# a = {}
# c = ['pnetfn']
# update_assignment(a, c, 'pnetfn', 'yertle')
# print(a, c)