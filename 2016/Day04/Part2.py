import re
from collections import Counter
from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    rooms = [line for line in f.read().split('\n')]


def getRoomName(input: str, shift: int) -> str:
    output = []
    for c in list(input):
        output.append(chr(((ord(c) - 96 + shift) % 26) + 96))
        pass

    return ''.join(output)


def getSector(input: list) -> int:
    for room in input:
        id, sector, checksum = re.match(r"^([a-z,-]+)-(\d+)\[(.+)]", room).groups()
        counts = Counter(list(id.replace('-', ''))).most_common()
        counts.sort(key=lambda x: (-x[1], x[0]))
        tocheck = ''.join([key for key, _ in list(counts)[:5]])
        if tocheck == checksum:
            name = getRoomName(id.replace('-', ''), int(sector))
            if 'north' in name:
                return int(sector)


answer = getSector(rooms)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
