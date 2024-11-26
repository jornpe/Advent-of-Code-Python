from pathlib import Path
import time
import re

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

supported = 0


def getAbas(input: str) -> list:
    if len(input) < 3:
        return []
    abas = []
    for a1, b1, a2 in [list(input[idx:idx+3]) for idx in range(0, len(input) - 2)]:
        if a1 == a2 and a1 != b1:
            abas.append(a1 + b1 + a2)
    return abas


def isSupported(input: str) -> bool:
    hypernets = re.findall(r"\[([a-z]+)]", input)
    abas = []
    for hypernet in hypernets:
        input = input.replace(hypernet, '')
        abas += getAbas(hypernet)

    parts = re.findall(r"([a-z]+)", input)
    for part in parts:
        for aba in abas:
            if aba[1] + aba[0] + aba[1] in part:
                return True
    return False


for ip in lines:
    if isSupported(ip):
        supported += 1

answer = supported
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
