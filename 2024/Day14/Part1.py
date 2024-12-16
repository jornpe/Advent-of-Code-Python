import re
from math import floor
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

width, height, blinks = 101, 103, 100

robots = []
for line in lines:
    col, row, vcol, vrow = map(int, re.findall(r'-?\d+', line))
    nr = (row + blinks * vrow) % height
    nc = (col + blinks * vcol) % width
    robots.append((nr, nc))


q1 = sum(1 for r, c in robots if r < floor(height / 2) and c < floor(width / 2))
q2 = sum(1 for r, c in robots if r < floor(height / 2) and c > floor(width / 2))
q3 = sum(1 for r, c in robots if r > floor(height / 2) and c < floor(width / 2))
q4 = sum(1 for r, c in robots if r > floor(height / 2) and c > floor(width / 2))

answer = q1 * q2 * q3 * q4
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
