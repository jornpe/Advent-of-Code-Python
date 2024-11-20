from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    cups = [int(i) for i in list(f.read())]

cups = cups + list(range(max(cups) + 1, 1_000_001))
pos = 0
for _ in range(10_000_000):
    length = len(cups)
    cur_cup = cups[pos]
    if pos < len(cups) - 3:
        pick_up = cups[pos+1:pos+4]
    else:
        pick_up = cups[pos+1::] + cups[0:pos+4-len(cups)]
    cups = [c for c in cups if c not in pick_up]

    dest = max(cups) if cur_cup <= min(cups) else max(c for c in cups if c < cur_cup)
    dest_index = cups.index(dest)
    cups = cups[0:dest_index+1] + pick_up + cups[dest_index+1:]
    while cups[pos] != cur_cup:
        cups = [cups[-1]] + cups[:-1]
    pos += 1
    pos %= len(cups)

one_index = cups.index(1)
answer = cups[one_index + 1] * cups[one_index + 2]
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
