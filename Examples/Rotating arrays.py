# Assuming 'space' is your original 2D array
from pprint import pprint

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the 'array' array: this is clockwise rotation
rotated_array = list(zip(*array[::-1]))

# Display the rotated array
print("Rotated Space:")
for row in rotated_array:
    print(row)

# Restore the 'rotated_array' array back to the original orientation: this is counter-clockwise rotation
restored_array = list(zip(*rotated_array))[::-1]

# Display the restored array
print("\nRestored Space:")
for row in restored_array:
    print(row)


def rotate45(input: list) -> list:
    array = []
    for ridx, r in enumerate(list(range(len(input))) + list(len(input) - 1 for _ in range(len(input) - 1))):
        line = []
        for cidx, c in enumerate(range(ridx - r, r+1, 1)):
            line.append(input[r - cidx][c])
        array.append(line)
    return array


rotated45_array = rotate45(array)
# Display the restored array
print("\n45 degrees rotated array:")
for row in rotated45_array:
    print(row)
