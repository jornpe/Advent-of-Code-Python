from pathlib import Path
import time
from pprint import pprint
from sympy import symbols, Eq, solve

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    lines = [line for line in f.read().split('\n')]

busses = [(idx, int(b)) for idx, b in enumerate(lines[1].split(',')) if b.isdigit()]
equations = []

t = symbols('t')

for idx, buss in busses:
    bt = symbols(f'x{idx}')
    equations.append(buss * bt - idx - t)

answer = solve(equations)
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
