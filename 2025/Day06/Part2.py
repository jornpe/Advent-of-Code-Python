import math
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = [line for line in f.read().split('\n')]

lines = [n for n in input[:-1]]
ops = [o for o in input[-1].split()]
answer = 0

numbers = []
for i in range(max(len(l) for l in lines) + 1):
    col = ''.join(c[i] if len(c) >= i + 1 else ' ' for c in lines)
    if col.isspace():
        op = ops.pop(0)
        answer += sum(numbers) if op == "+" else math.prod(numbers)
        numbers = []
        continue
    numbers.append(int(col))

if answer == 9348430857627:
    print("CORRECT")
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
