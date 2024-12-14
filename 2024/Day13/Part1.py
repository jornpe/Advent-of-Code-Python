import re
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    machines = [section for section in f.read().split('\n\n')]


def calculate(machine: str):
    ax, ay = map(int, re.findall(r'\d+', machine.split('\n')[0]))
    bx, by = map(int, re.findall(r'\d+', machine.split('\n')[1]))
    x, y = map(int, re.findall(r'\d+', machine.split('\n')[2]))

    for b in range(0, int(x / min(ax, bx))):
        axx = (x - b * bx) / ax
        ayy = (y - b * by) / ay
        if axx % 1 == 0 and axx == ayy:
            return int(axx), b
    return 0, 0


tokens = 0
for machine in machines:
    a, b = calculate(machine)
    tokens += 3 * a + b

answer = tokens
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
