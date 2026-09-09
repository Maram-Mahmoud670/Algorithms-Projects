def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def get_sorted_array(message):
    while True:
        arr = list(map(int, input(message).split()))

        if is_sorted(arr):
            return arr

        print("The array is not sorted.")
        print("Please enter the array again in sorted order.\n")


def find_median_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged = []

    # Merge the two sorted arrays
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    # Calculate the median
    length = len(merged)

    if length == 0:
        return None

    if length % 2 == 1:
        return merged[length // 2]

    return (merged[length // 2 - 1] + merged[length // 2]) / 2


# Input
arr1 = get_sorted_array(
    "Enter the first sorted array (numbers separated by spaces): "
)

arr2 = get_sorted_array(
    "Enter the second sorted array (numbers separated by spaces): "
)

# Find and print the median
median = find_median_sorted_arrays(arr1, arr2)

if median is None:
    print("Both arrays are empty. Median cannot be calculated.")
else:
    print("Median:", median)