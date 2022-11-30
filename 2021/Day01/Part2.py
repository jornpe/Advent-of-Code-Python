from itertools import pairwise

with open("input.txt") as f:
    inputs = [int(i) for i in f]

treeLevel = [(inputs[i-2] + inputs[i-1] + inputs[i]) for i in range(2, len(inputs))]
pairs = [a < b for a, b in pairwise(treeLevel)]

print(pairs.count(True))
