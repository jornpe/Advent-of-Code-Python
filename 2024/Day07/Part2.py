from pathlib import Path
import time
from itertools import product

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    calibrations = [line for line in f.read().split('\n')]


def correct(input: str) -> int:
    check = int(input.split(':')[0])
    numbers = list(map(int, input.split(':')[1].split()))
    if len(numbers) == 1:
        return check if numbers[0] == check else 0
    for ops in product(['+', '*', '||'], repeat=len(numbers)-1):
        result = numbers[0]
        for op, n in zip(ops, numbers[1:]):
            if op == '||':
                result = int(str(result) + str(n))
            elif op == '+':
                result += n
            else:
                result *= n
        if result == check:
            return check
    return 0


total = 0
for clb in calibrations:
    total += correct(clb)

answer = total
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
