import re

with open("input.txt") as f:
    lines = [i for i in f]

count = 0

for line in lines:
    min, max, char, password = re.split(r'[\W]+', line, 3)
    if int(min) <= password.count_rocks(char) <= int(max):
        count+=1

print(count)