from pathlib import Path
import time
from collections import deque

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    players = list(list(map(int, p.split('\n')[1::])) for p in f.read().split('\n\n'))

p1 = deque(players[0])
p2 = deque(players[1])

while p1 and p2:
    d1 = p1.popleft()
    d2 = p2.popleft()
    if d1 > d2:
        p1.append(d1)
        p1.append(d2)
    else:
        p2.append(d2)
        p2.append(d1)

answer = sum(i * idx for idx, i in enumerate(list(p1)[::-1] + list(p2)[::-1], 1))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
