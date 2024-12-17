import re
from pathlib import Path
import time
import sympy
from sympy import Eq

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    machines = [section for section in f.read().split('\n\n')]


def calculate(machine: str):

    a, b = sympy.symbols("a, b")

    ax, ay = map(int, re.findall(r'\d+', machine.split('\n')[0]))
    bx, by = map(int, re.findall(r'\d+', machine.split('\n')[1]))
    x, y = map(int, re.findall(r'\d+', machine.split('\n')[2]))
    x, y = x + 10000000000000, y + 10000000000000

    eqs = []
    eqs.append(Eq(a, (y - b * by) / ay))
    eqs.append(Eq(a, (x - b * bx) / ax))

    s = sympy.solve(eqs)
    sa, sb = s[a], s[b]
    if sa.is_Integer and sb.is_Integer:
        return 3 * sa + sb
    return 0


tokens = 0
for machine in machines:
    tokens += calculate(machine)

answer = tokens
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
