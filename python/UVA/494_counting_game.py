import fileinput
import re

f = fileinput.input()

split_regex = re.compile(r"[A-Za-z]+")

for l in f:
    words = split_regex.findall(l.strip())
    print(len(words))
