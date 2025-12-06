from pathlib import Path
import time
from collections import defaultdict

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

papers = defaultdict(int)

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == '@':
            papers[(row, col)] = 1

answer = 0
for c, r in list(papers.keys()):
    if papers[(c+1,r)] + papers[(c+1,r+1)] + papers[(c,r+1)] + papers[(c-1,r+1)] + papers[(c-1,r)] + papers[(c-1,r-1)] + papers[(c,r-1)] + papers[(c+1,r-1)] < 4:
        answer += 1

print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
