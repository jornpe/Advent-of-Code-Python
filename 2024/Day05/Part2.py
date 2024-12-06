from itertools import pairwise
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rules, updates = [line for line in f.read().split('\n\n')]

middlenumbers = []
order = {}
for rule in rules.split('\n'):
    r, l = map(int, (rule.split('|')))
    if r in order:
        order[r].append(l)
    else:
        order[r] = [l]


def isValid(input: str) -> bool:
    for l, r in pairwise(map(int, input.split(','))):
        if r in order and l in order[r]:
            return False
    return True


def ordercorrectly(input: str) -> list:
    numbers = list(map(int, input.split(',')))
    correctedlist = []

    while numbers:
        for n in numbers:
            if all(n not in order[x] for x in numbers if n != x and x in order):
                correctedlist.append(n)
                numbers.remove(n)
                break

    return correctedlist


for update in updates.split('\n'):
    if not isValid(update):
        corrected = ordercorrectly(update)
        middlenumbers.append(corrected[len(corrected) // 2])


answer = sum(middlenumbers)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
