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

start_time = time.time()
with open(Path(__file__).with_name('sympy-test.txt')) as f:
    hails = [line for line in f.read().split('\n')]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

# Her we build up all the equations needed. This is probably not necessarry to do for all the hails as after a few
# there will most likly only be one solution.
# The equations start's with this (where r = rock and h = hail):
#
# xh + t*vxh = xr + t*vxr
# yh + t*vyh = yr + t*vyr
# zh + t*vzh = zr + t*vzr
#
# which means: t = (xr - xh) / (vxh - vxr) = (yr - yh) / (vyh - vyr) = (zr - zh) / (vzh - vzr)
#
# Since symby needs equations = 0, then we need to split into 2 equations:
#
# (xr - xh) / (vxh - vxr) - (yr - yh) / (vyh - vyr) = 0
# (xr - xh) / (vxh - vxr) - (zr - zh) / (vzh - vzr) = 0
#
# We do not need this: (yr - yh) / (vyh - vyr) - (zr - zh) / (vzh - vzr) = 0
# since it's given by the 2 other equations.

for hail in hails:
    xh, yh, zh, vxh, vyh, vzh = list(map(int, re.findall(r'(-?\d+)', hail)))
    equations.append((xr - xh) * (vyh - vyr) - (yr - yh) * (vxh - vxr))
    equations.append((xr - xh) * (vzh - vzr) - (zr - zh) * (vxh - vxr))

solution = sympy.solve(equations)[0]
answer = solution[xr] + solution[yr] + solution[zr]

print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

