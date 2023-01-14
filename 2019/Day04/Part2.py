import itertools as it

with open("input.txt") as f:
    start, end = map(int, f.read().split('-'))

passwords = 0

for number in range(start, end):
    has_adjacent_digits = False
    str_numb = str(number)
    for i in range(len(str(number))):
        if i == 0:
            if str_numb[i] == str_numb[i + 1] and str_numb[i] != str_numb[i + 2]:
                has_adjacent_digits = True
                break
        elif i <= len(str_numb) - 3:
            if str_numb[i] == str_numb[i + 1] and str_numb[i] != str_numb[i - 1] and str_numb[i] != str_numb[i + 2]:
                has_adjacent_digits = True
                break
        elif i == len(str_numb) - 2:
            if str_numb[i] == str_numb[i + 1] and str_numb[i] != str_numb[i - 1]:
                has_adjacent_digits = True
                break

    if has_adjacent_digits and all(int(a) <= int(b) for a, b in it.pairwise(str_numb)):
        passwords += 1

print(f'⭐ Part 1: {passwords}')

# 465 too high
