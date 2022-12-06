import os.path

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    draws = [i.strip() for i in f]

score = 0

for draw in draws:
    opponent, yourself = draw.split()

    if yourself == 'Z':
       score += 6
       if opponent == 'A': score += 2
       if opponent == 'B': score += 3
       if opponent == 'C': score += 1

    elif yourself == 'Y':
       score += 3
       if opponent == 'A': score += 1
       if opponent == 'B': score += 2
       if opponent == 'C': score += 3
    else:
       if opponent == 'A': score += 3
       if opponent == 'B': score += 1
       if opponent == 'C': score += 2
    


print(score)