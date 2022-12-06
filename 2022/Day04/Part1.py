import os.path
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    pairs = [list(map(int, re.split(r'[,|-]+', i.strip(), 3))) for i in f]

sum = 0

for p in pairs:
    if (
        p[0] >= p[2] and p[1] <= p[3] or
        p[2] >= p[0] and p[3] <= p[1]
    ):
        sum += 1

print(sum)
