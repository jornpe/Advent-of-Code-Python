import re
from pathlib import Path
import time
import ast

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [input for input in f.read().split('\n')]

answer = 0

for line in lines:
    a = 2
    for c in line:
        if c in ['\"', '\\']:
            a += 2
        else:
            a += 1
    answer += a - len(line)

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
