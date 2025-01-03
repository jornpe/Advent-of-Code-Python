from pathlib import Path
import time
from itertools import pairwise

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    reports = [list(map(int, line.split())) for line in f.read().split('\n')]

safe = 0


def isSafe(report: list, direction: bool) -> int:
    for n1, n2 in pairwise(report):
        if (n1 > n2) != direction or 1 > abs(n1 - n2) or abs(n1 - n2) > 3:
            return 0
    return 1


for report in reports:
    safe += isSafe(report, report[0] > report[1])

answer = safe
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
