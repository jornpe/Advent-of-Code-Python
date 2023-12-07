from pathlib import Path
import re

with open(Path(__file__).with_name('input.txt')) as f:
    cards = [line.split(':')[1] for line in f.read().split('\n')]

score = 0

for card_idx, card in enumerate(cards):
    winning = set(re.findall(r'\d+', card.split('|')[0]))
    numbers = set(re.findall(r'\d+', card.split('|')[1]))
    overlapping = winning.intersection(numbers)

    if overlapping:
        score += pow(2, len(overlapping) - 1)


print(f'⭐ Part 1: {score}')