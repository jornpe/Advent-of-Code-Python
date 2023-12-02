from pathlib import Path
import re

with open(Path(__file__).with_name('input.txt')) as f:
    games = [line for line in f.read().split('\n')]

part1 = 0
part2 = 0

for game_id, game in enumerate(games, 1):
    draws = game.split(':')[1]
    colors = re.findall(r'(\d+) (blue|red|green)', draws)

    red = max([int(r[0]) for r in colors if r[1] == 'red'])
    blue = max([int(r[0]) for r in colors if r[1] == 'blue'])
    green = max([int(r[0]) for r in colors if r[1] == 'green'])

    if red <= 12 and green <= 13 and blue <= 14:
        part1 += game_id

    part2 += red * blue * green


print(f'⭐ Part 1: {part1}')
print(f'⭐⭐ Part 2: {part2}')
