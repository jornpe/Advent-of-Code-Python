from math import floor
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    blocks = list(f.read())

spanded = []
for i, n in enumerate(blocks):
    if i % 2 == 0:
        spanded.append([int(i / 2), int(n)])
    elif n != 0:
        spanded.append(['.', int(n)])

length = len(spanded)
for i, v in enumerate(list(spanded[::-1])):
    if v[0] == '.' or v not in spanded:
        continue
    index = spanded.index(v)
    ei = next((ii for ii, value in enumerate(spanded[:index]) if value[0] == '.' and value[1] >= v[1]), None)
    if ei:
        spanded[spanded.index(v)] = ['.', v[1]]
        if index != length - 1 and spanded[index + 1][0] == '.':
            spanded[index][1] += spanded[index + 1][1]
            spanded.pop(index + 1)
        if spanded[index - 1][0] == '.':
            spanded[index][1] += spanded[index - 1][1]
            spanded.pop(index - 1)
        replace = spanded[ei]
        spanded[ei] = v
        if replace[1] > v[1]:
            spanded.insert(ei + 1, ['.', replace[1] - v[1]])

answer = 0
index = 0
for s, nn in spanded:
    for _ in range(nn):
        if s != '.':
            answer += index * s
        index += 1

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
