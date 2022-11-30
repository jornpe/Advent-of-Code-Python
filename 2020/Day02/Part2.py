import re

with open("input.txt") as f:
    lines = [i for i in f]

count = 0

for line in lines:
    first, second, char, password = re.split(r'[\W]+', line, 3)
    if (password[int(first) - 1] == char) ^ (password[int(second) - 1] == char):
        count+=1

print(count)