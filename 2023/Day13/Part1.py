from pathlib import Path
from itertools import pairwise
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    patterns = [line.split() for line in f.read().split('\n\n')]


def get_pattern_value(pattern: list, multiplier: int) -> int:
    for row, lines in enumerate(pairwise(pattern)):
        if lines[0] == lines[1]:
            if all([pattern[l1] == pattern[l2] for l1, l2 in zip(range(row - 1, -1, -1), range(row + 2, len(pattern)))]):
                return (row + 1) * multiplier
    return 0


answer = 0
for pattern in patterns:
    vertical = get_pattern_value(list(zip(*pattern[::-1])), 1)
    horizontal = get_pattern_value(pattern, 100)
    answer += vertical + horizontal


print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
