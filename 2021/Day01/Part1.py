from itertools import pairwise

with open("input.txt") as f:
    inputs = [int(i) for i in f]

pairs = [a < b for a, b in pairwise(inputs)]

print(pairs.count(True))
