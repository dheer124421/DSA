# Function to check whether array is sorted or not

def check_sorted(arr):

    # Assume both conditions are true initially
    is_increasing = True
    is_decreasing = True

    # Traverse array
    for i in range(len(arr) - 1):

        # Check increasing condition
        if arr[i] > arr[i + 1]:
            is_increasing = False

        # Check decreasing condition
        if arr[i] < arr[i + 1]:
            is_decreasing = False

    # Final decision
    if is_increasing or is_decreasing:
        return True
    else:
        return False


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
result = check_sorted(arr)

# Output
print("Array:", arr)

if result:
    print("Array is sorted")
else:
    print("Array is not sorted")