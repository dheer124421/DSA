# Function to move all zeros to the end of the array

def move_zeros_to_end(arr):

    j = 0  # Position for next non-zero element

    # Move all non-zero elements to the front
    for i in range(len(arr)):

        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
move_zeros_to_end(arr)

# Output
print("Array after moving zeros to the end:")
print(arr)