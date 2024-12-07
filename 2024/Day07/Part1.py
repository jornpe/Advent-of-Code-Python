from pathlib import Path
import time
from itertools import product

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    calibrations = [line for line in f.read().split('\n')]


def correct(input: str) -> int:
    check = int(input.split(':')[0])
    numbers = list(map(int, input.split(':')[1].split()))
    for ops in product(['+', '*'], repeat=len(numbers)-1):
        result = numbers[0]
        for op, n in zip(ops, numbers[1:]):
            result = result + n if op == '+' else result * n
        if result == check:
            return check
    return 0


total = 0
for clb in calibrations:
    total += correct(clb)

answer = total
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
