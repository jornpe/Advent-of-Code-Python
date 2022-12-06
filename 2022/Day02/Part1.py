import os.path

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    draws = [i.strip() for i in f]

score = 0

for draw in draws:
    opponent, yourself = draw.split()

    if (
            opponent == 'A' and yourself == 'X' or
            opponent == 'B' and yourself == 'Y' or 
            opponent == 'C' and yourself == 'Z' 
        ): 
        score += 3
    elif (
            opponent == 'A' and yourself == 'Y' or
            opponent == 'B' and yourself == 'Z' or 
            opponent == 'C' and yourself == 'X' 
        ): 
        score += 6
    
    if yourself == 'X': score += 1
    if yourself == 'Y': score += 2
    if yourself == 'Z': score += 3


print(score)