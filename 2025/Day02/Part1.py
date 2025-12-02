from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in f.read().split(',')]

answer = 0

for f, l in ranges:
    for n in range(f, l + 1):
        ns = str(n)
        if len(ns) % 2 == 0:
            if ns[:len(ns) // 2] == ns[len(ns) // 2:]:
                answer += int(ns)

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
