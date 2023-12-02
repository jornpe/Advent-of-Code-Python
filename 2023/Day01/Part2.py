from pathlib import Path

with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n')]
answer = 0

numbers = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'),
           ('eight', '8'), ('nine', '9')]


def get_digits(input_line: str):
    returnValue = ''
    for idx, char in enumerate(input_line):
        for number in numbers:
            if input_line[idx:].startswith(number):
                returnValue += number[1]
                continue

    return int(returnValue[0] + returnValue[-1])


for line in lines:
    answer += get_digits(line)

print(f'⭐⭐ Part 2: {answer}')
