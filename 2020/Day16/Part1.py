from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rules, _, tickets = [line for line in f.read().split('\n\n')]

values = []
valid_values = set()

for rule in rules.split('\n'):
    numbers = list(map(int, re.findall(r'\d+', rule)))
    for m1, m2 in zip(numbers[::2], numbers[1::2]):
        for v in range(m1, m2 + 1):
            valid_values.add(v)

for ticket in tickets[1::].split('\n'):
    numbers = list(map(int, re.findall(r'\d+', ticket)))
    for n in numbers:
        if n not in valid_values:
            values.append(n)

answer = sum(values)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
