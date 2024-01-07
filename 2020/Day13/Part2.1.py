from itertools import pairwise
from pathlib import Path
import time
from pprint import pprint
from sympy import symbols, Eq, solve

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    lines = [line for line in f.read().split('\n')]

busses = [(idx, int(b)) for idx, b in enumerate(lines[1].split(',')) if b.isdigit()]


def gcd(a, b, c):
    if a <= c:
        return b
    return gcd(b % a, a, c)


def lcm(a, b, c):
    return (a // gcd(a, b, c)) * b


lcmvalue = busses[0][0]
for idx, buss in busses[1::]:
    lcmvalue = lcm(buss, lcmvalue, idx)


answer = lcmvalue
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
