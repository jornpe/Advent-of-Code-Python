from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    lines = [line for line in f.read().split('\n\n')]

locks = [l for l in lines if l.startswith('#')]
keys = [k for k in lines if k.startswith('.')]

fits = 0
for lock in locks:
    l = list(zip(*list(lock.split('\n'))[::-1]))
    for key in keys:
        k = list(zip(*list(key.split('\n'))[::-1]))
        if all(7 >= n for n in [sum(1 for kkk in kk if kkk == '#') + sum(1 for lll in ll if lll == '#') for kk, ll in zip(k, l)]):
            fits += 1


answer = fits
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')
