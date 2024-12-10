from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    blocks = list(map(int, f.read()))

spanded = []
for i, n in enumerate(blocks):
    spanded += [i / 2 if i % 2 == 0 else '.' for _ in range(n)]

while '.' in spanded:
    n = spanded.pop()
    if n != '.':
        spanded[spanded.index('.')] = n
        pass


answer = sum(i * n for i, n in enumerate(spanded))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
