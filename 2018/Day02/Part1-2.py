from itertools import combinations
from pathlib import Path
import time
from collections import Counter

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    ids = [line for line in f.read().split('\n')]

twos = 0
trees = 0

for id in ids:
    t = Counter(id)
    twos += 1 if 2 in Counter(id).values() else 0
    trees += 1 if 3 in Counter(id).values() else 0
answer1 = twos * trees

common = ''
for id1, id2 in combinations(ids, 2):
    if sum([a != b for a, b in zip(id1, id2)]) == 1:
        common = ''.join([a for a, b in zip(id1, id2) if a == b])


print(f'⭐ Part 1: {answer1}, run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {common}, run time: {int((time.time() - start_time) * 1000)}ms')
