from pathlib import Path
import time
from pprint import pprint
from collections import Counter

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [list(line) for line in f.read().split('\n')]

part1 = []
part2 = []

for line in list(zip(*lines[::-1])):
    part1.append(Counter(line).most_common()[0][0])
    part2.append(Counter(line).most_common()[-1][0])

answer1 = ''.join(part1)
answer2 = ''.join(part2)
print(f'⭐ Part 1: {answer1} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer2} ; run time: {int((time.time() - start_time) * 1000)}ms')
