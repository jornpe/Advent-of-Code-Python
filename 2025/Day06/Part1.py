import math
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

numbers = [[int(x) for x in line.split()] for line in lines[:-1]]
ops = [o for o in lines[-1].split()]
answer = 0

for op, arranged_numbers in zip(ops, list(zip(*numbers[::-1]))):
    answer += sum(arranged_numbers) if op == "+" else math.prod(arranged_numbers)

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
