from pathlib import Path
import time
from pprint import pprint
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

bags = {}

for line in lines:
    bag, *contains = re.findall(r'(\d+)?\s?(\w+\s\w+)\sbag', line)
    bags[bag[1]] = contains

numbersofbags = 0
queue = ['shiny gold']
while queue:
    b = queue.pop(0)
    if b == 'no other':
        continue
    for n, bag in bags[b]:
        n = int(n) if n != '' else 0
        numbersofbags += n
        for _ in range(n):
            queue.append(bag)


answer = numbersofbags
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
