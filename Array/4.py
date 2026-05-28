# Function to remove duplicates from a sorted array in-place

def remove_duplicates(arr):

    # If array is empty
    if len(arr) == 0:
        return 0

    # Pointer for unique elements
    j = 0

    # Traverse array from second element
    for i in range(1, len(arr)):

        # If current element is different
        if arr[i] != arr[j]:

            j += 1
            arr[j] = arr[i]

    # Number of unique elements
    return j + 1


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
new_length = remove_duplicates(arr)

# Output
if new_length == 0:
    print("Array does not exist")
else:
    print("Array after removing duplicates:")

    for i in range(new_length):
        print(arr[i], end=" ")