from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

bags = {}

for line in lines:
    bag, *contains = re.findall(r'(\w+\s\w+)\sbag', line)
    bags[bag] = contains

visited = []
queue = ['shiny gold']
while queue:
    b = queue.pop(0)
    if b == 'no other':
        continue
    bs = [key for key, v in bags.items() if b in v]
    for bag in bs:
        if bag not in visited:
            visited.append(bag)
            queue.append(bag)


answer = len(visited)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
