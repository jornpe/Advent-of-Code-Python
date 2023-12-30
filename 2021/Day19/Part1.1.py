from itertools import combinations
from pathlib import Path
import time
import re
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    input = [line for line in f.read().split('\n\n')]

scanners = {}

for scanner in input:
    number = int(re.findall(r'(\d+)', scanner)[0])
    s = []
    for beacon in scanner.splitlines()[1::]:
        b = []
        for beacon2 in scanner.splitlines()[1::]:
            if beacon != beacon2:
                bx, by, bz = list(map(int, beacon.split(',')))
                bx2, by2, bz2 = list(map(int, beacon2.split(',')))
                b.append((bx2 - bx, by2 - by, bz2 - bz))
        s.append(b)
    scanners[number] = s


def get_orientations(x, y, z) -> list:
    return [(x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y), (-x, y, -z), (-x, z, y), (-x, -y, z), (-x, -z, -y), (y, x, z), (y, z, -x), (y, -x, -z), (y, -z, x), (-y, x, -z), (-y, z, x), (-y, -x, z), (-y, -z, -x)]


def rotate_all(listinput) -> list:
    toreturn = []
    for p in listinput:
        toreturn.append(get_orientations(*p))
    return zip(*toreturn)


uniquebeacons = len([b for b in scanners[0]])
for (sn1, s1), (sn2, s2) in combinations(scanners.items(), 2):
    for b1 in s1:
        unique = []
        for b2 in s2:
            for b3 in rotate_all(b2):
                unique.append(len(set(b1).intersection(set(b3))))
        uniquebeacons += len(b1) - max(unique)


answer = uniquebeacons
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
