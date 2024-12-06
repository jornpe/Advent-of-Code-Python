from itertools import pairwise
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rules, updates = [line for line in f.read().split('\n\n')]

middlenumbers = []
order = {}
for rule in rules.split('\n'):
    r, l = map(int, rule.split('|'))
    if r in order:
        order[r].append(l)
    else:
        order[r] = [l]


def isValid(input: list) -> bool:
    for l, r in pairwise(input):
        if r in order and l in order[r]:
            return False
    return True


for update in [list(map(int, x.split(','))) for x in updates.split('\n')]:
    if isValid(update):
        middlenumbers.append(update[len(update) // 2])


answer = sum(middlenumbers)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
