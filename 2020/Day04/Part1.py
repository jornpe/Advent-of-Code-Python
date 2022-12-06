from itertools import groupby

with open("test.txt") as f:
    lines = [i.strip() for i in f]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validPassports = 0

passports = [" ".join(list(g)) for k, g in groupby(lines, key=bool) if k]

for passport in passports:
    if all(x in passport for x in fields):
        validPassports += 1

print(validPassports)