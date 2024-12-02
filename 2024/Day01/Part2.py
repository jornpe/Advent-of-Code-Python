from pathlib import Path
import time
from collections import Counter

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [[int(n1), int(n2)] for n1, n2 in [line.split() for line in f.read().split('\n')]]

left, right = zip(*lines)
multipliers = Counter(right)
similarity = 0

for l in left:
    if l in multipliers:
        similarity += l * multipliers[l]

answer = similarity
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
