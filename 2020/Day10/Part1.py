from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    adapters = [int(n) for n in f.read().split('\n')]

diffs = [3]
joltage = 0
while adapters:
    ad = min(adapters)
    adapters.remove(ad)
    diff = ad - joltage
    if diff <= 3:
        diffs.append(diff)
        joltage = ad

answer = sum(1 for a in diffs if a == 1) * sum(1 for a in diffs if a == 3)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
