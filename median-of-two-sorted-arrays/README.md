# Median of Two Sorted Arrays

> A Python implementation of the **Median of Two Sorted Arrays** problem using the **Two-Pointer Technique**, with input validation and an enhanced version that automatically sorts unsorted input.

---

##  Overview

This project solves the problem of finding the **median of two arrays**.

The project was developed in two stages:

### Basic Version

The program requires the user to enter both arrays in **sorted order**.
If an array is not sorted, the program asks the user to enter it again.

### Enhanced Version

The program accepts arrays in any order. If an array is not sorted, the program informs the user and **automatically sorts it** before continuing.

This project demonstrates:

* Array manipulation
* Input validation
* Two-pointer technique
* Array merging
* Algorithm design
* Pseudocode
* Time and space complexity analysis
* Improving an existing solution while analyzing the effect on performance

---

#  Problem Statement

Given two arrays, find the **median of the combined elements**.

The median is:

* The middle element when the total number of elements is odd.
* The average of the two middle elements when the total number of elements is even.

### Example 1 — Odd Number of Elements

```text
arr1 = [1, 3]
arr2 = [2]

Combined array = [1, 2, 3]

Median = 2
```

### Example 2 — Even Number of Elements

```text
arr1 = [1, 2]
arr2 = [3, 4]

Combined array = [1, 2, 3, 4]

Median = (2 + 3) / 2 = 2.5
```

---

#  Solution Approach

The solution uses the **Two-Pointer Technique**.

Instead of combining the two arrays and sorting the result, the program takes advantage of the fact that the arrays are already sorted in the Basic Version.

Two pointers are used:

* `i` → points to the current element in the first array.
* `j` → points to the current element in the second array.

At each step, the program compares:

```text
arr1[i]
arr2[j]
```

The smaller value is added to the merged array, and its pointer is moved forward.

This continues until one of the arrays has been completely processed.

Finally, the remaining elements are added to the merged array and the median is calculated.

---

#  Algorithm

## Step-by-Step

1. Read the first array.
2. Check whether the array is sorted.
3. If it is not sorted, ask the user to enter it again.
4. Read the second array.
5. Check whether the array is sorted.
6. If it is not sorted, ask the user to enter it again.
7. Initialize two pointers:

   * `i = 0`
   * `j = 0`
8. Create an empty `merged` array.
9. Compare the current elements of both arrays.
10. Add the smaller element to `merged`.
11. Move the corresponding pointer forward.
12. Continue until one array is exhausted.
13. Add the remaining elements.
14. Calculate the median:

    * Odd length → return the middle element.
    * Even length → return the average of the two middle elements.
15. Display the result.

---

# Pseudocode — Basic Version

```text
FUNCTION isSorted(array)

    FOR each pair of consecutive elements
        IF current element > next element
            RETURN False

    RETURN True


FUNCTION findMedian(arr1, arr2)

    Check if arr1 is sorted
    IF not sorted
        Ask user to enter arr1 again

    Check if arr2 is sorted
    IF not sorted
        Ask user to enter arr2 again

    Set i = 0
    Set j = 0
    Create empty merged array

    WHILE i < length(arr1) AND j < length(arr2)

        IF arr1[i] <= arr2[j]
            Add arr1[i] to merged
            Increase i

        ELSE
            Add arr2[j] to merged
            Increase j

    Add remaining elements of arr1
    Add remaining elements of arr2

    IF merged is empty
        Return no median

    IF length(merged) is odd
        Return middle element

    ELSE
        Return average of the two middle elements

END FUNCTION
```

---

#  Time Complexity — Basic Version

Let:

* `n` = number of elements in the first array
* `m` = number of elements in the second array

### 1. Input Validation

Checking whether the first array is sorted:

```text
O(n)
```

Checking whether the second array is sorted:

```text
O(m)
```

Therefore:

```text
O(n + m)
```

### 2. Merging

Each element is processed once during the merge:

```text
O(n + m)
```

### 3. Median Calculation

Accessing the middle element(s) takes:

```text
O(1)
```

### Overall Time Complexity

```text
O(n + m) + O(n + m) + O(1)
```

Therefore:

```text
╔══════════════════════╗
║ Time: O(n + m)       ║
╚══════════════════════╝
```

### Space Complexity

The merged array stores all elements:

```text
O(n + m)
```

Therefore:

```text
╔══════════════════════╗
║ Space: O(n + m)     ║
╚══════════════════════╝
```

---

#  Enhanced Version

## Why an Enhancement?

The Basic Version requires the user to manually enter sorted arrays.

For example:

```text
5 2 8
```

is rejected because it is not sorted.

To improve the user experience, the Enhanced Version allows the user to enter the array in any order.

The program detects whether the array is sorted.

If it is not sorted, the program displays a message and automatically sorts the array.

---

## Enhanced Workflow

```text
User Input
    │
    ▼
Check if Array is Sorted
    │
    ├── Yes ──────────────► Continue
    │
    └── No
         │
         ▼
   Display Message
         │
         ▼
   Sort Automatically
         │
         ▼
      Continue
```

---

#  Enhanced Example

### Input

```text
Enter the first array: 5 2 8

Enter the second array: 7 1 4
```

### Program Output

```text
First array is not sorted.
The program will sort it automatically.
Sorted First array: [2, 5, 8]

Second array is not sorted.
The program will sort it automatically.
Sorted Second array: [1, 4, 7]

Median: 4.5
```

---

#  Time Complexity — Enhanced Version

The Enhanced Version uses Python's built-in `sort()` method when an array is not sorted.

For the first array:

```text
O(n log n)
```

For the second array:

```text
O(m log m)
```

### Merging

After sorting, the two arrays are merged:

```text
O(n + m)
```

### Median Calculation

```text
O(1)
```

### Overall Time Complexity

```text
O(n log n + m log m + n + m)
```

The dominant terms are the sorting operations:

```text
╔════════════════════════════════════╗
║ Time: O(n log n + m log m)        ║
╚════════════════════════════════════╝
```

### Space Complexity

The merged array requires:

```text
O(n + m)
```

---

#  Basic vs Enhanced Version

| Feature                  | Basic Version | Enhanced Version       |
| ------------------------ | ------------- | ---------------------- |
| Sorted input required    | ✅ Yes         | ❌ No                   |
| Input validation         | ✅             | ✅                      |
| Automatic sorting        | ❌             | ✅                      |
| Two-pointer merge        | ✅             | ✅                      |
| Handles duplicate values | ✅             | ✅                      |
| Handles negative numbers | ✅             | ✅                      |
| Time Complexity          | `O(n + m)`    | `O(n log n + m log m)` |
| Space Complexity         | `O(n + m)`    | `O(n + m)`             |

---

#  Project Structure

```text
median-of-two-sorted-arrays/
│
├── README.md
│
├── .gitignore
│
├── basic_solution.py
│
└── enhanced_solution.py
```

### `basic_solution.py`

Contains the original solution where the user must provide sorted arrays.

### `enhanced_solution.py`

Contains the improved version where unsorted arrays are automatically sorted.

### `README.md`

Contains the problem description, algorithms, pseudocode, complexity analysis, examples, and project documentation.

### `.gitignore`

Prevents unnecessary files such as Python cache files, virtual environments, and IDE settings from being uploaded to GitHub.

---

#  Technologies Used

* **Python 3**
* Lists / Arrays
* Functions
* Loops
* Conditional Statements
* Two-Pointer Technique
* Python `sort()` method
* Algorithm Complexity Analysis

---

#  How to Run

## Requirements

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external Python libraries are required.

---

## Run the Basic Version

```bash
python basic_solution.py
```

Example:

```text
Enter the first sorted array (numbers separated by spaces): 1 3 5
Enter the second sorted array (numbers separated by spaces): 2 4 6

Median: 3.5
```

---

## Run the Enhanced Version

```bash
python enhanced_solution.py
```

Example:

```text
Enter the first array (numbers separated by spaces): 5 2 8

First array is not sorted.
The program will sort it automatically.
Sorted First array: [2, 5, 8]

Enter the second array (numbers separated by spaces): 7 1 4

Second array is not sorted.
The program will sort it automatically.
Sorted Second array: [1, 4, 7]

Median: 4.5
```

---

#  Test Cases

The following cases can be used to verify the program.

### Test Case 1 — Odd Total Length

```text
Input:
arr1 = [1, 3]
arr2 = [2]

Expected Output:
2
```

### Test Case 2 — Even Total Length

```text
Input:
arr1 = [1, 2]
arr2 = [3, 4]

Expected Output:
2.5
```

### Test Case 3 — Different Array Sizes

```text
Input:
arr1 = [1, 2, 3]
arr2 = [4, 5]

Expected Output:
3
```

### Test Case 4 — Duplicate Values

```text
Input:
arr1 = [1, 2, 2]
arr2 = [2, 3, 4]

Expected Output:
2
```

### Test Case 5 — Negative Numbers

```text
Input:
arr1 = [-5, -3, -1]
arr2 = [-4, -2, 0]

Expected Output:
-2.5
```

### Test Case 6 — Unsorted Input

For the Basic Version:

```text
Input:
arr1 = [5, 2, 8]
```

Expected behavior:

```text
The array is not sorted.
Please enter the array again in sorted order.
```

For the Enhanced Version:

```text
Input:
arr1 = [5, 2, 8]
```

Expected behavior:

```text
The array is not sorted.
The program will sort it automatically.
Sorted First array: [2, 5, 8]
```

---

#  Edge Cases

The program considers several special cases:

### Empty Arrays

If both arrays are empty, there is no median to calculate.

### One Empty Array

If one array is empty, the median can still be calculated from the other array.

### Single Element

The program correctly handles arrays containing one element.

### Duplicate Values

Duplicate elements are allowed.

### Negative Numbers

Negative integers are supported.

### Different Lengths

The two arrays do not need to have the same number of elements.

---

#  Code Analysis

## `is_sorted()`

The function checks whether the elements of an array are in non-decreasing order.

```python
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
```

It compares every pair of neighboring elements.

---

## `find_median_sorted_arrays()`

This is the main algorithm.

It uses two pointers to merge the arrays without using another sorting operation.

The function then determines whether the merged array has an odd or even number of elements.

---

## `get_sorted_array()`

Used in the Basic Version.

It keeps asking the user for input until a sorted array is entered.

---

## `get_array()`

Used in the Enhanced Version.

It accepts any input order and automatically sorts the array if necessary.

---

#  What This Project Demonstrates

This project demonstrates practical understanding of:

* Algorithm design
* Pseudocode development
* Input validation
* Two-pointer algorithms
* Array merging
* Time complexity
* Space complexity
* Code organization
* Improving an existing algorithm
* Comparing performance before and after an enhancement

---

#  Possible Future Improvements

The current implementation stores the complete merged array.

A more advanced implementation could calculate the median without storing all elements.

Another possible improvement is implementing the optimal solution for the original **Median of Two Sorted Arrays** problem using binary search.

The target complexity for that approach is:

```text
O(log(min(n, m)))
```

Additional improvements could include:

* Automated unit tests
* More robust input validation
* Support for decimal numbers
* A command-line menu
* A graphical user interface
* Benchmarking different approaches
* Memory optimization

---

#  Learning Outcomes

Through this project, the following concepts were practiced:

1. Breaking a problem into smaller steps.
2. Writing language-independent pseudocode.
3. Implementing algorithms in Python.
4. Analyzing time complexity step by step.
5. Analyzing space complexity.
6. Improving an existing solution.
7. Understanding the performance impact of sorting.
8. Using the two-pointer technique to merge sorted arrays.

---

#  Author

**Maram Mahmoud**

Computer Science Student
Interested in **Data Science, Artificial Intelligence, Algorithms, and Problem Solving**.
