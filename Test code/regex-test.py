import re

# Example from https://adventofcode.com/2020/day/7
input = 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.'

matches = re.findall(r'(\d+)? ?(\w+ \w+) bags', input)
rules = {}
bag = []
for m1, m2 in matches[1:]:
    bag.append((m2, int(m1)))

rules[matches[0][1]] = bag

print(rules)
