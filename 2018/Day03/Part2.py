from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    claims = [line for line in f.read().split('\n')]

nonoverlapping = set([i for i in range(1, len(claims) + 1)])
fabrics = {}
for claim in claims:
    id, left, top, width, height = list(map(int, re.findall(r'\d+', claim)))
    for col in range(left, left + width):
        for row in range(top, top + height):
            if (row, col) not in fabrics:
                fabrics[(row, col)] = id
                continue
            if fabrics[(row, col)] in nonoverlapping:
                nonoverlapping.remove(fabrics[(row, col)])
            if id in nonoverlapping:
                nonoverlapping.remove(id)


answer = nonoverlapping.pop()
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
