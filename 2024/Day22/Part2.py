from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    buyers = [int(line) for line in f.read().split('\n')]


def calculatesecretnumber(number: int) -> dict:
    sequence = {}
    pricechanges = []
    lastprice = number % 10
    for idx in range(2000):
        number = ((number * 64) ^ number) % 16777216
        number = (int(number / 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216
        price = number % 10
        pricechanges.append(price - lastprice)
        if idx >= 3:
            if tuple(pricechanges) not in sequence:
                sequence[tuple(pricechanges)] = price
            pricechanges.pop(0)
        lastprice = price

    return sequence


def mostbananas(seq: list) -> int:
    bananas = 0

    for i in range(len(seq)):
        while seq[i]:
            s, v = seq[i].popitem()
            r = sum(sequence[s] for sequence in seq if s in sequence) + v
            if r > bananas:
                bananas = r
    return bananas



sequences = []
for b in buyers:
    sequences.append(calculatesecretnumber(b))

answer = mostbananas(sequences)
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')

# too high: 1517 530890ms
