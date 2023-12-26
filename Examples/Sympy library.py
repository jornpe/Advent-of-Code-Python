# from advent of code 2023 day 24 part 2
# Sympy is a library that can solve equations. In this example there is manu hails starting at a position and moving
# in a direction x, y, z. We need to find a x, y, z for a start position of a rock that can be thrown so hit all
# hails when moving.
# To do this we generate first the unknown symbols, then import each hail, then create the equations.
# this has to be done for at leat 3 hails, here we do it for all. Then we get the rock position and speed.

from pathlib import Path
import time
import re
import sympy
from sympy import Eq

start_time = time.time()
with open(Path(__file__).with_name('sympy-test.txt')) as f:
    hails = [line for line in f.read().split('\n')]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

# Her we build up all the equations needed. This only needs to be doe for the 3 first.
# The equations start's with this (where r = rock and h = hail):
#
# xh + t*vxh = xr + t*vxr
# yh + t*vyh = yr + t*vyr
# zh + t*vzh = zr + t*vzr
#

for idx, hail in enumerate(hails[:3]):
    t = sympy.symbols(f't{idx}')
    xh, yh, zh, vxh, vyh, vzh = list(map(int, re.findall(r'(-?\d+)', hail)))
    equations.append(Eq(xh + t * vxh, xr + t * vxr))
    equations.append(Eq(yh + t * vyh, yr + t * vyr))
    equations.append(Eq(zh + t * vzh, zr + t * vzr))

solution = sympy.solve(equations)[0]
answer = solution[xr] + solution[yr] + solution[zr]

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

