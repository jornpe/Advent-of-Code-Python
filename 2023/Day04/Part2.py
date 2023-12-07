from pathlib import Path
import re

with open(Path(__file__).with_name('input.txt')) as f:
    cards = [line.split(':')[1] for line in f.read().split('\n')]

cardcopies = [1 for x in cards]

for card_idx, card in enumerate(cards):
    winning = set(re.findall(r'\d+', card.split('|')[0]))
    numbers = set(re.findall(r'\d+', card.split('|')[1]))
    overlapping = winning.intersection(numbers)

    for n in range(card_idx, card_idx + len(overlapping)):
        if n < len(cards):
            cardcopies[n + 1] += cardcopies[card_idx]

answer = sum(cardcopies)
print(f'⭐ Part 1: {answer}')
