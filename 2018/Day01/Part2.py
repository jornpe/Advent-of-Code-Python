from pathlib import Path

with open(Path(__file__).with_name('input.txt')) as f:
    input = [int(x) for x in f]

frequencies = set()
frequence = 0

while True:
    for i in input:
        frequence += i
        if frequence in frequencies:
            print(f'⭐ Part 2: {frequence}')
            exit()
        frequencies.add(frequence)