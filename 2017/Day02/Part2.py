from itertools import combinations, permutations
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [[int(x) for x in line.split()] for line in f]

answer = 0

for line in lines:
    combs = permutations(line, 2)
    for n1, n2 in combs:
        if n1 % n2 == 0:
            answer += int(n1 / n2)
            break

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
