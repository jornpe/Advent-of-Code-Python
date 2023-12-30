from itertools import combinations
from pathlib import Path
import time
import re
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('test2.txt')) as f:
    input = [line for line in f.read().split('\n\n')]

scanners = {}

for scanner in input:
    number = re.findall(r'(\d+)', scanner)[0]
    s = []
    for beacon in scanner.splitlines()[1::]:
        b = []
        for beacon2 in scanner.splitlines()[1::]:
            if beacon != beacon2:
                bx, by, bz = list(map(int, beacon.split(',')))
                bx2, by2, bz2 = list(map(int, beacon2.split(',')))
                b.append(abs(bx - bx2) + abs(by - by2) + abs(bz - bz2))
        s.append(b)
    scanners[number] = s


detected = {}
for (sn1, s1), (sn2, s2) in combinations(scanners.items(), 2):
    detectedbyboth = 0
    for b1 in s1:
        for b2 in s2:
            detectedbyboth += 1 if len(set(b1).intersection(set(b2))) >= 11 else 0
    detected[(sn1, sn2)] = detectedbyboth

pprint(detected)
#pprint([(k, v) for k, v in detected.items() if v > 0])
print(sum(detected.values()))

answer = 0
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
