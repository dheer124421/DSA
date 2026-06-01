# Function to count maximum consecutive 1's

def max_consecutive_ones(arr):

    count = 0
    max_count = 0

    for i in range(len(arr)):

        if arr[i] == 1:
            count += 1

            if count > max_count:
                max_count = count

        else:
            count = 0

    return max_count


# User input
size = int(input("Enter size of array: "))

arr = []

for i in range(size):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

# Function call
result = max_consecutive_ones(arr)

# Output
print("Array:", arr)
print("Maximum consecutive 1's:", result)