# Function to find the length of the longest subarray
# with sum equal to K (Positive numbers only)

def longest_subarray(arr, k):

    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):

        # Add current element
        current_sum += arr[right]

        # Shrink window if sum becomes greater than k
        while current_sum > k:

            current_sum -= arr[left]
            left += 1

        # Check if sum equals k
        if current_sum == k:

            length = right - left + 1

            if length > max_length:
                max_length = length

    return max_length


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

k = int(input("Enter value of K: "))

# Function call
result = longest_subarray(arr, k)

# Output
print("Length of Longest Subarray:", result)