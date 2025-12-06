from itertools import pairwise
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [int(n) for n in f.read()]

sum = 0 if input[0] != input[-1] else input[0]
for a, b in pairwise(input):
    if a == b:
        sum += a

answer = sum
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
