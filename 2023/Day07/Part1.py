from pathlib import Path
from collections import Counter
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]

hands = []

fiveofakind = []
fourofakind = []
fullhouse = []
treeofakind = []
twopairs = []
onepair = []
highcard = []

for line in lines:
    cards = []
    hand = line.split(' ')[0]
    bid = int(line.split(' ')[1])

    for card in list(hand):
        if card.isdigit():
            cards.append(int(card))
            continue
        else:
            match card:
                case 'T':
                    cards.append(10)
                case 'J':
                    cards.append(11)
                case 'Q':
                    cards.append(12)
                case 'K':
                    cards.append(13)
                case 'A':
                    cards.append(14)

    hands.append([tuple(cards), bid])



# Get hands
for hand in hands:
    cards = hand[0]
    cardcount = Counter(cards).values()

    # five of a kind
    if 5 in cardcount:
        fiveofakind.append(hand)
        continue

    # four of a kind
    if 4 in cardcount:
        fourofakind.append(hand)
        continue

    # full house
    if 3 in cardcount and 2 in cardcount:
        fullhouse.append(hand)
        continue

    if 3 in cardcount:
        treeofakind.append(hand)
        continue

    if 2 in Counter(cardcount).values():
        twopairs.append(hand)
        continue

    if 2 in cardcount:
        onepair.append(hand)
        continue

    highcard.append(hand)

rank = 1
answer = 0

fiveofakind.sort(key=lambda x: x[0])
fourofakind.sort(key=lambda x: x[0])
fullhouse.sort(key=lambda x: x[0])
treeofakind.sort(key=lambda x: x[0])
twopairs.sort(key=lambda x: x[0])
onepair.sort(key=lambda x: x[0])
highcard.sort(key=lambda x: x[0])

for hand in highcard:
    answer += rank * hand[1]
    rank += 1
for hand in onepair:
    answer += rank * hand[1]
    rank += 1
for hand in twopairs:
    answer += rank * hand[1]
    rank += 1
for hand in treeofakind:
    answer += rank * hand[1]
    rank += 1
for hand in fullhouse:
    answer += rank * hand[1]
    rank += 1
for hand in fourofakind:
    answer += rank * hand[1]
    rank += 1
for hand in fiveofakind:
    answer += rank * hand[1]
    rank += 1

print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
