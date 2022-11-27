from itertools import pairwise

with open("input.txt") as f:
    input = [ int(i) for i in f]

treeLevel = [(input[i-2] + input[i-1] + input[i]) for i in range(2, len(input))]    
pairs = [a < b for a, b in pairwise(treeLevel)]

print(pairs.count(True))