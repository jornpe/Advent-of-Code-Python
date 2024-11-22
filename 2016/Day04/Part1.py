import re
from collections import Counter
from pathlib import Path
import time


start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rooms = [line for line in f.read().split('\n')]

sectors = 0

for room in rooms:
    id, sector, checksum = re.match(r"^([a-z,-]+)-(\d+)\[(.+)]", room).groups()
    counts = Counter(list(id.replace('-', ''))).most_common()
    counts.sort(key=lambda x: (-x[1], x[0]))
    tocheck = ''.join([key for key, _ in list(counts)[:5]])
    if tocheck == checksum:
        sectors += int(sector)

answer = sectors
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
