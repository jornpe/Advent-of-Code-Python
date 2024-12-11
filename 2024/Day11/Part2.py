from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    stones = list(map(int, f.read().split()))


def calculatestones(turn: int, stone: int, cache: dict) -> int:
    if turn == 75:
        return 1
    if (turn, stone) in cache:
        return cache[(turn, stone)]
    result = 0
    if stone == 0:
        result += calculatestones(turn + 1, 1, cache)
        cache[(turn, stone)] = result
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        result += calculatestones(turn + 1, int(s[:int(len(s) / 2)]), cache)
        result += calculatestones(turn + 1, int(s[int(len(s) / 2):]), cache)
    else:
        result += calculatestones(turn + 1, stone * 2024, cache)
    cache[(turn, stone)] = result
    return result


cache = {}
answer = sum(calculatestones(0, s, cache) for s in stones)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
