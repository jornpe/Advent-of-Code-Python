import math

with open("input.txt") as f:
    numbers = [line for line in f.read().split('\n')]

answer = 0
for n in numbers:
    answer += math.floor(int(n) / 3) - 2


print(f'⭐ Part 1: {answer}')
