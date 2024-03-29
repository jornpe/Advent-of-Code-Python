from pathlib import Path
import re
import math
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

times = list(map(int, re.findall(r'\d+', lines[0])))
records = list(map(int, re.findall(r'\d+', lines[1])))
totalwaystowin = []

for t, record in zip(times, records):
    waystowin = 0
    for chargingtime in range(t + 1):
        distance = (t - chargingtime) * chargingtime
        if distance > record:
            waystowin += 1
    totalwaystowin.append(waystowin)

answer = math.prod(totalwaystowin)
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
