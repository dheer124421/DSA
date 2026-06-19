# Function to find union of two sorted arrays

def find_union(arr1, arr2):

    i = 0
    j = 0

    union = []

    while i < len(arr1) and j < len(arr2):

        # If elements are equal
        if arr1[i] == arr2[j]:

            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])

            i += 1
            j += 1

        # If arr1 element is smaller
        elif arr1[i] < arr2[j]:

            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])

            i += 1

        # If arr2 element is smaller
        else:

            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])

            j += 1

    # Remaining elements of arr1
    while i < len(arr1):

        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])

        i += 1

    # Remaining elements of arr2
    while j < len(arr2):

        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])

        j += 1

    return union


# User input for first array
n = int(input("Enter size of first array: "))

arr1 = []

for i in range(n):
    value = int(input(f"Enter element {i+1} of first array: "))
    arr1.append(value)

# User input for second array
m = int(input("Enter size of second array: "))

arr2 = []

for i in range(m):
    value = int(input(f"Enter element {i+1} of second array: "))
    arr2.append(value)

# Function call
result = find_union(arr1, arr2)

# Output
print("Union of arrays:")
print(result)