import sys

def decode(x):
    if x - 7 < 0x20:
        return x
    return x - 7

buffer = sys.stdin.buffer.read()

output = bytes(decode(x) for x in buffer)
sys.stdout.buffer.write(output)
