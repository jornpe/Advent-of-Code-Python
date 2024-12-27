import re
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    switches = [line for line in f.read().split('\n')]

lights = [[False for c in range(1000)] for _ in range(1000)]
for switch in switches:
    op = re.findall(r'(on|off|toggle)', switch)[0]
    x1, y1, x2, y2 = map(int, re.findall(r'(\d+)', switch))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] = not lights[x][y] if op == 'toggle' else True if op == 'on' else False

answer = sum(1 if l else 0 for lightrow in lights for l in lightrow)

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')