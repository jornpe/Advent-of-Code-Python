from pathlib import Path
import time
from pprint import pprint
import re
from bitarray.util import int2ba, ba2int

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

mask = []
values = {}

for line in lines:
    if line.startswith('mask'):
        mask = [(idx, int(b)) for idx, b in enumerate(line[7::]) if b in ['0', '1']]
    else:
        address, value = map(int, re.findall(r'\d+', line))
        bit = int2ba(value, length=36)
        for pos, b in mask:
            bit[pos] = b
        values[address] = ba2int(bit)

answer = sum(values.values())
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')

