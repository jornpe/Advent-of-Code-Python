from itertools import groupby
import re

with open(r"D:\Repos\Private\Advent-of-Code-Python\2020\Day04\input.txt") as f:
    lines = f.read()

ids = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
validPassports = 0

passports = [" ".join(p.split()) for p in lines.split('\n\n')]

for passport in passports:
    hasAll = all(x in passport for x in ids)
    if not hasAll:
        continue

    isValid = True
    fields = passport.split()

    for field in fields:
        id, value = field.split(':')
        
        match id:
            case 'byr':
                isValid = 1920 <= int(value) <= 2002
            case 'iyr':
                isValid = 2010 <= int(value) <= 2020
            case 'eyr':
                isValid = 2020 <= int(value) <= 2030
            case 'hgt':
                if value.endswith('in'):
                    inches = value.replace('in', '')
                    isValid = 59 <= int(inches) <= 76
                elif value.endswith('cm'):
                    cm = value.replace('cm', '')
                    isValid = 150 <= int(cm) <= 193
                else:
                    isValid = False
            case 'hcl':
                isValid = re.match('^#[0-9a-z]{6}$', value)
            case 'ecl':
                isValid = any(x in value for x in eyeColor) and len(value) == 3
            case 'pid':
                isValid = re.match('^[0-9]{9}$', value)
        
        if not isValid:
            break

    if isValid:
        validPassports += 1
        

print(validPassports)
