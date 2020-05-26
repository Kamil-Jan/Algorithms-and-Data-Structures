"""

Quick Sort algorithm.

"""


def Partition(arr, l, h):
    pivot = arr[h]
    i = l
    for j in range(l, h):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[h] = arr[h], arr[i]
    return i

def QuickSort(arr, l, h):
    if l < h:
        j = Partition(arr, l, h)
        QuickSort(arr, l, j - 1)
        QuickSort(arr, j + 1, h)

