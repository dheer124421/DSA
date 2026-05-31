# Function for Linear Search

def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i   # Return index if found

    return -1          # Return -1 if not found


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Element to search
target = int(input("Enter element to search: "))

# Function call
result = linear_search(arr, target)

# Output
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")