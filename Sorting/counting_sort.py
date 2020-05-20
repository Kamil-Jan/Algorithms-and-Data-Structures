"""

Counting Sort algorithm.

"""


def counting_sort(arr):
    # Create empty lists for output and counting
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(10)]

    # Add the count of each elements into count array
    for num in arr:
        count[num] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    for num in arr:
        output[count[num] - 1] = num
        # Decrease count by 1 to place next data
        # at an index smaller than this index.
        count[num] -= 1
    return output

