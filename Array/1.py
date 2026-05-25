
# Function to find the largest number in an array

def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


# Taking array input from user
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Calling function
result = find_largest(arr)

# Printing result
print("Largest number is:", result)