from pathlib import Path
import time
from collections import defaultdict


start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    papers = {(row, col): 1 if c == '@' else 0 for row, line in enumerate(f.read().split('\n')) for col, c in enumerate(line)}


def paper_roll(papers: dict) -> int:
    removed = []
    dd = defaultdict(int, papers)
    for r, c in list(papers.keys()):
        if papers[(r, c)] != 0 and dd[(r+1,c)] + dd[(r+1,c+1)] + dd[(r,c+1)] + dd[(r-1,c+1)] + dd[(r-1,c)] + dd[(r-1,c-1)] + dd[(r,c-1)] + dd[(r+1,c-1)] < 4:
            removed.append((r,c))
    for item in removed:
        papers[item] = 0
    return len(removed)


answer = 0
while (removed_paper := paper_roll(papers)) != 0:
    answer += removed_paper

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
