import re
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

result = 0

for line in lines:
    multiplications = re.findall(r'mul\((\d+),(\d+)\)', line)
    for m1, m2 in multiplications:
        result += int(m1) * int(m2)
        pass

answer = result
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
