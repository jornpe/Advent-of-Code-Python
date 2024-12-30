from pathlib import Path
import time
from itertools import permutations, pairwise


start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    paths = {(line.split()[0], line.split()[2]): int(line.split()[4]) for line in f.read().split('\n')}

cities = list(set([c for p in paths.keys() for c in p]))
shortest = 1000000
longest = 0

for path in permutations(cities):
    cost = 0
    for c1, c2 in pairwise(path):
        if (c1, c2) in paths:
            cost += paths[(c1, c2)]
        elif (c2, c1) in paths:
            cost += paths[(c2, c1)]
        else:
            break
    if cost < shortest:
        shortest = cost
    if cost > longest:
        longest = cost

print(f'⭐ Part 1: {shortest} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {longest} ; run time: {int((time.time() - start_time) * 1000)}ms')
