# Function to left rotate the array by one position

def left_rotate_by_one(arr):

    n = len(arr)

    # Store first element
    first_element = arr[0]

    # Shift all elements one position to the left
    for i in range(n - 1):
        arr[i] = arr[i + 1]

    # Place first element at the end
    arr[n - 1] = first_element

    return arr


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
left_rotate_by_one(arr)

# Output
print("Array after left rotation by one:")
print(arr)