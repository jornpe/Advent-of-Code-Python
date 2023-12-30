from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    claims = [line for line in f.read().split('\n')]

fabrics = {}
for claim in claims:
    id, left, top, width, height = list(map(int, re.findall(r'\d+', claim)))
    for col in range(left, left + width):
        for row in range(top, top + height):
            if (row, col) not in fabrics:
                fabrics[(row, col)] = 1
            else:
                fabrics[(row, col)] += 1


answer = sum(1 for f in fabrics.values() if f > 1)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
