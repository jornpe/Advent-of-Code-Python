# Assuming 'space' is your original 2D array
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
