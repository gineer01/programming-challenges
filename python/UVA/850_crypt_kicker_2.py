import fileinput

f = fileinput.input()

cases = int(next(f))
next(f)

known_plaintext = "the quick brown fox jumps over the lazy dog"
known_length = len(known_plaintext)


def find_key(ciphers):
    for c in ciphers:
        if len(c) == known_length:
            key = check_key(c)
            if key:
                return key


def check_key(cipher):
    key = {}
    for i in range(known_length):
        plain_c = known_plaintext[i]
        cipher_c = cipher[i]

        if cipher_c == ' ':
            if plain_c == ' ':
                continue
            else:
                return None

        if cipher_c in key:
            if key[cipher_c] != plain_c:
                return None
        else:
            if plain_c == ' ':
                return None
            else:
                key[cipher_c] = plain_c

    if len(key) == 26:
        return key


def decrypt(ciphers):
    key = find_key(ciphers)

    if key:
        for c in ciphers:
            print("".join(key.get(i, i) for i in c))
    else:
        print("No solution.")


def process_case(f):
    ciphers = []
    for l in f:
        cipher = l.strip()
        if cipher:
            ciphers.append(cipher)
        else:
            break

    decrypt(ciphers)

process_case(f)
for i in range(1, cases):
    print()
    process_case(f)

