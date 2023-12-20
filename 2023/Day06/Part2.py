from pathlib import Path
import re
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

t = int(''.join(re.findall(r'\d+', lines[0])))
record = int(''.join(re.findall(r'\d+', lines[1])))

waystowin = 0
for chargingtime in range(t + 1):
    distance = (t - chargingtime) * chargingtime
    if distance > record:
        waystowin += 1

print(f'⭐⭐ Part 2: {waystowin}, run time: {int((time.time() - start_time) * 1000)}ms')
