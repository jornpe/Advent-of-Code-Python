from more_itertools  import chunked
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in f.read().split(',')]

answer = 0

for f, l in ranges:
    for n in range(f, l + 1):
        ns = str(n)
        for nr in range(1, 1 + len(ns) // 2):
            if len(ns) % nr == 0:
                l2 = list(chunked(ns, nr))
                if all(x == l2[0] for x in l2):
                    answer += int(ns)
                    break

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
