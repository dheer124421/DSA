# Function to find the element that appears only once

def find_single_number(arr):

    xor = 0

    # XOR all elements
    for num in arr:
        xor ^= num

    return xor


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
result = find_single_number(arr)

# Output
print("Element appearing only once is:", result)