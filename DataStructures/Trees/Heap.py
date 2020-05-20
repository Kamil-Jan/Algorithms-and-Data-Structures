import time as t


class Heap:
    """
    A heap Data Structure.
    ABT's operations: insert, extract_max
    Functions: Max_Heapify, Build_Heap, Heap_Sort
    """
    @classmethod
    def Max_Heapify(cls, arr, n, i):
        l = 2 * i + 1 # left child
        r = 2 * i + 2 # right child
        largest = i
        left = l < n
        right = r < n

        # check if child bigger than parent
        if left and arr[l] >= arr[largest]:
            largest = l

        if right and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # swap parent with largest child
            cls.Max_Heapify(arr, n, largest)

    @classmethod
    def Build_Heap(cls, array):
        for i in range(len(array) // 2 + 1, -1, -1):
            cls.Max_Heapify(array, len(array), i)

    @classmethod
    def Heap_Sort(cls, array):
        cls.Build_Heap(array)
        for i in range(len(array) - 1, -1, -1):
            array[0], array[i] = array[i], array[0]
            cls.Max_Heapify(array, i, 0)

    @classmethod
    def insert(cls, x, arr):
        arr.append(x)
        i = (len(arr) - 2) // 2
        while i >= 0 and arr[i] < x:
            cls.Max_Heapify(arr, len(arr), i)
            i = (i - 1) // 2

    @classmethod
    def extract_max(cls, arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        cls.Max_Heapify(arr, len(arr) - 1, 0)

