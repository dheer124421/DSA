# Function to reverse a portion of the array

def reverse(arr, start, end):

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# Function to rotate array to the right by k steps

def rotate_array(arr, k):

    n = len(arr)

    # Handle cases where k > n
    k = k % n

    # Step 1: Reverse entire array
    reverse(arr, 0, n - 1)

    # Step 2: Reverse first k elements
    reverse(arr, 0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(arr, k, n - 1)

    return arr


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

k = int(input("Enter value of k: "))

# Function call
rotate_array(arr, k)

# Output
print("Rotated Array:")
print(arr)