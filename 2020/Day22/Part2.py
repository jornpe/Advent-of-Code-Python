from pathlib import Path
import time
from pprint import pprint
from collections import deque

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    players = list(list(map(int, p.split('\n')[1::])) for p in f.read().split('\n\n'))

player1 = players[0]
player2 = players[1]


def combat(p1: list, p2: list) -> tuple:
    cache = set()
    while p1 and p2:
        t = (tuple(p1), tuple(p2))
        if t in cache:
            return True, p1
        cache.add(t)

        d1 = p1.pop(0)
        d2 = p2.pop(0)
        if d1 <= len(p1) and d2 <= len(p2):
            if combat(p1[:d1], p2[:d2])[0]:
                p1.extend([d1, d2])
            else:
                p2.extend([d2, d1])
        elif d1 > d2:
            p1.extend([d1, d2])
        else:
            p2.extend([d2, d1])
    return (True, p1) if p1 else (False, p2)


winner, cards = combat(players[0], players[1])
answer = sum(i*j for i, j in enumerate(reversed(cards), 1))
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
