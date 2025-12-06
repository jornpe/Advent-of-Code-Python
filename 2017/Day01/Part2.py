from itertools import pairwise
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [int(n) for n in f.read()]

sum = 0

for i, n in enumerate(input):
    if n == input[(i + len(input) // 2) % len(input)]:
        sum += n

answer = sum
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
