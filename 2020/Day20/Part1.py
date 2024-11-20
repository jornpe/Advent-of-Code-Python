from pathlib import Path
import time
from pprint import pprint
import re

start_time = time.time()
with open(Path(__file__).with_name('test.txt')) as f:
    input_tiles = [line.split('\n') for line in f.read().split('\n\n')]

tiles = {}
for tile in input_tiles:
    tile_h = list(zip(*tile[1::]))
    id = int(re.findall(r'\d+', tile[0])[0])
    edges = [tile[1], tile[1][::-1]]
    edges.append(''.join(tile_h[-1]))
    edges.append(''.join(tile_h[-1][::-1]))
    edges.extend([tile[-1], tile[-1][::-1]])
    edges.append(''.join(tile_h[0]))
    edges.append(''.join(tile_h[0][::-1]))
    tiles[id] = edges

startid = list(tiles.keys())[0]
grid = {startid: ((0, 0), tiles[startid])}

while tiles:
    for g_id, ((row, col), g_tile) in list(grid.items()):
        for id, tile in list(tiles.items()):
            if g_id != id:
                # over
                if tile[4] in g_tile[0:1] or tile[5] in g_tile[0:1]:
                    grid[id] = ((row - 1, col), tile)
                    tiles.pop(id)
                # right
                if tile[6] in g_tile[2:3] or tile[7] in g_tile[2:3]:
                    grid[id] = ((row, col + 1), tile)
                    tiles.pop(id)
                # under
                if tile[0] in g_tile[4:5] or tile[1] in g_tile[4:5]:
                    grid[id] = ((row + 1, col), tile)
                    tiles.pop(id)
                # left
                if tile[2] in g_tile[6:7] or tile[3] in g_tile[6:7]:
                    grid[id] = ((row, col - 1), tile)
                    tiles.pop(id)

pprint(grid)


answer = 0
print(f'⭐ Part 1: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
print(f'⭐⭐ Part 2: {answer}, run time: {int((time.time() - start_time) * 1000)}ms')
