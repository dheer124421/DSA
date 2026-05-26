# Function to find second largest element

def find_second_largest(arr):

    # Check array size
    if len(arr) < 2:
        return "Second largest element does not exist"

    # Initial assignment using first two elements
    if arr[0] > arr[1]:
        largest = arr[0]
        second_largest = arr[1]
    else:
        largest = arr[1]
        second_largest = arr[0]

    # Loop from start to end
    for i in range(len(arr)):

        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
result = find_second_largest(arr)

# Output
print("Array:", arr)
print("Second largest element is:", result)