import math
from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rules, myticket, tickets = [line for line in f.read().split('\n\n')]

possibillities = {}
departure_ranges = {}
myticket = [int(v) for v in myticket.split('\n')[1].split(',')]

# Get all values for each rule
for rule in rules.split('\n'):
    numbers = list(map(int, re.findall(r'\d+', rule)))
    valid_values = set()
    for m1, m2 in zip(numbers[::2], numbers[1::2]):
        for v in range(m1, m2 + 1):
            valid_values.add(v)
    departure_ranges[rule.split(':')[0]] = valid_values

# get all valid tickets list of ints
nearby_tickets = [myticket]
valid_values = set().union(*departure_ranges.values())
for ticket in tickets.split('\n')[1::]:
    numbers = list(map(int, re.findall(r'\d+', ticket)))
    if all(n in valid_values for n in numbers):
        nearby_tickets.append(numbers)

# get all possibilities for each ticket collumn
for rule, dr in departure_ranges.items():
    for idx, r in enumerate(zip(*nearby_tickets)):
        if all(v in dr for v in r):
            if idx in possibillities:
                possibillities[idx].append(rule)
            else:
                possibillities[idx] = [rule]

# get the only possible outcome where each collumn has 1 type
values = []
while len(values) != 6:
    r = next((idx, *p) for idx, p in possibillities.items() if len(p) == 1)
    for k, v in possibillities.items():
        possibillities[k] = [x for x in v if x != r[1]]
    if r[1].startswith('departure'):
        values.append(myticket[r[0]])

answer = math.prod(values)
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

