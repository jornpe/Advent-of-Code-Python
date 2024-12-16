import re
from math import floor
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

width, height = 101, 103
robots = []


def drawxmastree(input: list) -> int:
    blinks = 0
    while blinks < 10000:
        blinks += 1
        for line in lines:
            col, row, vcol, vrow = map(int, re.findall(r'-?\d+', line))
            nr = (row + blinks * vrow) % height
            nc = (col + blinks * vcol) % width
            robots.append((nr, nc))

        q1 = sum(1 for r, c in robots if r < floor(height / 2) and c < floor(width / 2))
        q2 = sum(1 for r, c in robots if r < floor(height / 2) and c > floor(width / 2))
        q3 = sum(1 for r, c in robots if r > floor(height / 2) and c < floor(width / 2))
        q4 = sum(1 for r, c in robots if r > floor(height / 2) and c > floor(width / 2))

        # Check for many trees located in one quadrant:
        threshold = 300
        if q1 > threshold or q2 > threshold or q3 > threshold or q4 > threshold:
            print(f"Xmas tree is at: {blinks}")
            for r in range(width):
                line = ''
                for c in range(height):
                    if (r, c) in robots:
                        line += 'x'
                    else:
                        line += '.'
                print(line)
            return blinks
        robots.clear()


answer = drawxmastree(lines)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
