# Function to find missing number using sum method

def find_missing_number(arr, n):

    # Sum of first n natural numbers
    expected_sum = n * (n + 1) // 2

    # Actual sum of array elements
    actual_sum = sum(arr)

    # Missing number
    return expected_sum - actual_sum


# User input
n = int(input("Enter the value of N: "))

arr = []

print(f"Enter {n-1} elements:")

for i in range(n - 1):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
missing_number = find_missing_number(arr, n)

# Output
print("Missing Number:", missing_number)