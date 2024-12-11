from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    stones = list(map(int, f.read().split()))

for _ in range(25):
    changedStones = []
    for idx, stone in enumerate(stones):
        if stone == 0:
            changedStones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            changedStones.append(int(s[:int(len(s)/2)]))
            changedStones.append(int(s[int(len(s)/2):]))
        else:
            changedStones.append(stone * 2024)
    stones = changedStones

answer = len(stones)
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
