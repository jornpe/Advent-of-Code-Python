from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [[int(n1), int(n2)] for n1, n2 in [line.split() for line in f.read().split('\n')]]

left, right = zip(*lines)
distance = 0

for l, r in zip(sorted(left), sorted(right)):
    distance += max(l, r) - min(l, r)

answer = distance
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
