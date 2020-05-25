"""

Merge Sort algorithm.

"""


def MergeSort(arr, left, right):
    """
    Merge Sort using recursion.
    """
    if left >= right:
        return
    mid = (left + right) // 2
    MergeSort(arr, left, mid)
    MergeSort(arr, mid + 1, right)
    Merge(arr, left, right, mid)

def TwoWayMergeSort(arr, n):
    """
    Iterative method for Merge Sort.
    """
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            left = i
            right = i + 2 * step - 1
            mid = i + step - 1
            Merge(arr, left, right, mid)
        step *= 2

def Merge(arr, left, right, mid):
    """
    Merging two sorted lists.
    """
    L = arr[left: mid + 1]
    R = arr[mid + 1: right + 1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

