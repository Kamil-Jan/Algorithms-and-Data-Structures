"""

Merge Sort algorithm.

"""


def MergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    MergeSort(arr, left, mid)
    MergeSort(arr, mid + 1, right)
    Merge(arr, left, right, mid)

def Merge(arr, left, right, mid):
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

