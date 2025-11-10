from pathlib import Path
import time

start_time = time.time()
with open(Path(__file__).with_name('input.txt')) as f:
    initial, inputops = [line for line in f.read().split('\n\n')]

operations = {g.split()[4]: (g.split()[0], g.split()[1], g.split()[2]) for g in inputops.split('\n')}



def geteq(gate: str, ops: dict) -> str:
    if gate.startswith('y') or gate.startswith('x'):
        return gate
    A, op, B = ops[gate]
    A = geteq(A, ops)
    B = geteq(B, ops)

    return f'{min(A, B)} {op} {max(A, B)}'



eqs = {e: (len(geteq(e, operations)), geteq(e, operations)) for e in list(operations.keys())}

length = 0
for id, (v, eq) in sorted(eqs.items(), key=lambda item: len(item[1][1])):
    if id.startswith('z'):
        print(f'{id}: {v:04}, {v-length}; {eq}')
        length = v



# To solve this what is important is that each time



answer = ','.join(sorted(['vkq', 'mmk', 'qdq', 'z38', 'z11', 'z24', 'pvb', 'hqh']))
print(f'⭐ Part 1: {answer} ; run time: {int((time.time() - start_time) * 1000)}ms')

# vkq <-> z11
# mmk <-> z24
# qdq <-> pvb
# z38 <-> hqh

# z must end with AND XOR XOR
