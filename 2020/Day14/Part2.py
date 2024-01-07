import itertools
from pathlib import Path
import time
import re
from bitarray.util import int2ba

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

mask = []
maskx = []
values = {}

for line in lines:
    if line.startswith('mask'):
        mask = [b for idx, b in enumerate(line[7::])]
        maskx = [idx for idx, b in enumerate(line[7::]) if b == 'X']
    else:
        add, value = map(int, re.findall(r'\d+', line))
        bit = int2ba(add, length=36)
        result = []
        for idx, a in enumerate(bit):
            r = str(a) if mask[idx] == '0' else '1' if mask[idx] == '1' else 'X'
            result.append(r)


        for comb in list(itertools.product(['0', '1'], repeat=len(maskx))):
            for idx in range(len(comb)):
                result[maskx[idx]] = comb[idx]
            values[''.join(result)] = value


answer = sum(values.values())
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
