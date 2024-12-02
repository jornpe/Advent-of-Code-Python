from pathlib import Path
import time
from itertools import pairwise
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    reports = [list(map(int, line.split())) for line in f.read().split('\n')]

safe = 0


def isSafe(report: list, direction: bool) -> bool:
    for n1, n2 in pairwise(report):
        if (n1 > n2) != direction or 1 > abs(n1 - n2) or abs(n1 - n2) > 3:
            return False
    return True


def withProblemDampener(report: list):
    if isSafe(report, report[0] > report[1]):
        return 1
    for idx in range(len(report)):
        damped = report[:idx] + report[idx + 1:]
        if isSafe(damped, damped[0] > damped[1]):
            return 1
    return 0


for report in reports:
    safe += withProblemDampener(report)

answer = safe
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')

