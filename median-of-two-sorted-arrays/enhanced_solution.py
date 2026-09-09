
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def get_array(message, array_name):
    arr = list(map(int, input(message).split()))

    if not is_sorted(arr):
        print(f"\n{array_name} is not sorted.")
        print("The program will sort it automatically.")

        arr.sort()

        print(f"Sorted {array_name}: {arr}\n")

    return arr


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
arr1 = get_array(
    "Enter the first array (numbers separated by spaces): ",
    "First array"
)

arr2 = get_array(
    "Enter the second array (numbers separated by spaces): ",
    "Second array"
)

# Find and print the median
median = find_median_sorted_arrays(arr1, arr2)

if median is None:
    print("Both arrays are empty. Median cannot be calculated.")
else:
    print("Median:", median)