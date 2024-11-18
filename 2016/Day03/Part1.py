from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    triangles = [(int(x), int(y), int(z)) for x, y, z in [line.split() for line in f.read().split('\n')]]

isvalid = 0

for x, y, z in triangles:
    if x + y > z and y + z > x and z + x > y:
        isvalid += 1


answer = isvalid
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')


# 933 is too low