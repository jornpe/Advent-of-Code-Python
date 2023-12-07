from pathlib import Path
import re

with open(Path(__file__).with_name('input.txt')) as f:
    inputs = [line for line in f.read().split('\n\n')]

seedranges = list(map(int, re.findall(r'\d+', inputs[0])))
maps = [[list(map(int, re.findall(r'\d+', m_numbers))) for m_numbers in m.split('\n')[1:]] for m in inputs[1:]]


def get_location(r: tuple) -> int:
    # seed_start, seed_end

    ranges = [r]
    for m in maps:
        updatedRanges = []
        for rangechange in m:
            dest_start, source_start, length = rangechange
            source_end = source_start + length - 1

            nextRanges = ranges.copy()
            ranges = []

            while nextRanges:
                seed_start, seed_end = nextRanges[0]

                # whole range inside
                if source_start <= seed_start and source_end >= seed_end:
                    seed_start = seed_start + (dest_start - source_start)
                    seed_end = seed_end + (dest_start + length - 1 - source_end)
                    updatedRanges.append((seed_start, seed_end))
                    nextRanges.pop(0)

                # whole range outside
                elif source_start > seed_end or source_end < seed_start:
                    ranges.append((seed_start, seed_end))
                    nextRanges.pop(0)

                # range has to be split on the left side
                elif seed_start < source_start and seed_end <= source_end:
                    nextRanges.append((seed_start, source_start - 1))
                    nextRanges.append((source_start, seed_end))
                    nextRanges.pop(0)

                # range has to be split on the right side
                elif seed_start >= source_start and seed_end > source_end:
                    nextRanges.append((seed_start, source_end))
                    nextRanges.append((source_end + 1, seed_end))
                    nextRanges.pop(0)

                # range is split in 3 left side, middle and right side of the source
                elif seed_start < source_start and seed_end > source_end:
                    nextRanges.append((seed_start, source_start - 1))
                    nextRanges.append((source_start, source_end))
                    nextRanges.append((source_end + 1, seed_end))
                    nextRanges.pop(0)

        ranges.extend(updatedRanges)

    return min([number for number, _ in ranges])


locations = []
for s, r in zip(seedranges[::2], seedranges[1::2]):
    locations.append(get_location((s, s + r - 1)))

answer = min(locations)
print(f'⭐⭐ Part 2: {answer}')
