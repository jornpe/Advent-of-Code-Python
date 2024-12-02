import re
from pathlib import Path
import time
from pprint import pprint

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    input = f.read()


def decompress(section: str) -> int:
    if section.startswith('('):
        seq, number, repeats, *_ = re.search(r'(\((\d+)x(\d+)\))', section).groups()
        body = section[len(seq):len(seq) + int(number)]
        remainer = section[len(seq) + int(number):]
        return decompress(body) * int(repeats) + decompress(remainer)
    elif '(' in section:
        idx = section.index('(')
        return decompress(section[idx:]) + idx
    else:
        return len(section)


answer = decompress(input)

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
