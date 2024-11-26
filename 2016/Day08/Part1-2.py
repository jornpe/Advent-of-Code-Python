import re
from pathlib import Path
import time
from collections import defaultdict
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    cmds = [line for line in f.read().split('\n')]

grid = [['.' for _ in range(50)] for _ in range(6)]


def printGrid():
    for row in range(len(grid)):
        line = ''
        for col in range(len(grid[0])):
            line += grid[row][col]
        print(line)


def rect(cols: int, rows: int):
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = '#'


def rotate(row: list, idx: int):
    return row[len(row) - idx:] + row[:len(row) - idx]


for cmd in cmds:
    n1, n2 = map(int, re.match(r"\D+(\d+)\D+([0-9]+)", cmd).groups())
    if cmd.startswith("rect"):
        rect(n1, n2)
    if cmd.startswith("rotate column"):
        grid = list(map(list, zip(*grid)))
        grid[n1] = rotate(grid[n1], n2)
        grid = list(map(list, zip(*grid)))
    if cmd.startswith("rotate row"):
        grid[n1] = rotate(grid[n1], n2)

answer = sum([1 for line in grid for v in line if v == '#'])
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2:')

printGrid()
