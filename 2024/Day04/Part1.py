from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [list(line) for line in f.read().split('\n')]


def numberofxmas(input: list) -> int:
    n = 0
    for line in input:
        s = ''.join(line)
        n += s.count('XMAS')
        n += s.count('SAMX')
    return n


def rotate45(input: list) -> list:
    array = []
    for ridx, r in enumerate(list(range(len(input))) + list(len(input) - 1 for _ in range(len(input) - 1))):
        line = []
        for cidx, c in enumerate(range(ridx - r, r+1, 1)):
            line.append(input[r - cidx][c])
        array.append(line)
    return array


xmas = numberofxmas(lines)
rot45 = rotate45(lines)
xmas += numberofxmas(rot45)
lines = list(zip(*lines[::-1]))
xmas += numberofxmas(lines)
rot45 = rotate45(lines)
xmas += numberofxmas(rot45)


answer = xmas
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
