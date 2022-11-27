from itertools import pairwise

with open("input.txt") as f:
    input = [ int(i) for i in f]

pairs = [a < b for a, b in pairwise(input)]

print(pairs.count(True))