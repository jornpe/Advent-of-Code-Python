from pathlib import Path
import time
from pprint import pprint
import re

from more_itertools import flatten

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    products = [line for line in f.read().split('\n')]

allergens = {}
all_ingredients = []

for product in products:
    ings = re.findall(r'\w+', product.split('(')[0])
    algs = re.findall(r'\w+', product.split('(')[1])[1::]
    for a in algs:
        if a in allergens:
            allergens[a] = allergens[a].intersection(ings)
        else:
            allergens[a] = set(ings)
    all_ingredients.extend(ings)

while any(len(i) > 1 for a, i in allergens.items()):
    correctAllegens = set(flatten(i for i in allergens.values() if len(i) == 1))
    for a, i in list((a, i) for a, i in allergens.items() if len(i) > 1):
        allergens[a] = allergens[a].difference(correctAllegens)

used_ingredients = list((a, list(i)[0]) for a, i in allergens.items())
answer = ','.join([i for a, i in sorted(used_ingredients)])

print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
