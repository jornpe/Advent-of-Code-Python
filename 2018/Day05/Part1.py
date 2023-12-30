from itertools import pairwise
from pathlib import Path
import time
import sys

sys.setrecursionlimit(1000000)

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    puzzle = list(f.read())


def get_polymer(polymer: list) -> list:
    for idx, (c1, c2) in enumerate(pairwise(polymer)):
        if c1.upper() == c2.upper() and c1 != c2:
            polymer.pop(idx)
            polymer.pop(idx)
            return get_polymer(polymer)
    return polymer


answer = len(get_polymer(list(puzzle)))
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
