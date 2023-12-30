from pathlib import Path
import time
import re
import sympy
from sympy import Eq

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    hails = [line for line in f.read().split('\n')]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for idx, hail in enumerate(hails[:3]):
    t = sympy.symbols(f't{idx}')
    xh, yh, zh, vxh, vyh, vzh = list(map(int, re.findall(r'(-?\d+)', hail)))
    equations.append(Eq(xh + t * vxh, xr + t * vxr))
    equations.append(Eq(yh + t * vyh, yr + t * vyr))
    equations.append(Eq(zh + t * vzh, zr + t * vzr))

solution = sympy.solve(equations)[0]
answer = solution[xr] + solution[yr] + solution[zr]

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

