from pathlib import Path
import re

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

time = int(''.join(re.findall(r'\d+', lines[0])))
record = int(''.join(re.findall(r'\d+', lines[1])))

waystowin = 0
for chargingtime in range(time + 1):
    distance = (time - chargingtime) * chargingtime
    if distance > record:
        waystowin += 1

print(f'⭐⭐ Part 2: {waystowin}')
