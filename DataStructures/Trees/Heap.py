class MaxHeap:
    """
    A Max Heap Data Structure.
    ABT's operations: insert, extract_root
    Functions: Heapify, Build_Heap, Heap_Sort
    """
    @classmethod
    def Heapify(cls, arr, n, i):
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
            cls.Heapify(arr, n, largest) # look at a child

    @classmethod
    def Build_Heap(cls, array):
        for i in range(len(array) // 2, -1, -1):
            cls.Heapify(array, len(array), i)

    @classmethod
    def Heap_Sort(cls, array):
        cls.Build_Heap(array)
        for i in range(len(array) - 1, -1, -1):
            array[0], array[i] = array[i], array[0]
            cls.Heapify(array, i, 0)

    @classmethod
    def insert(cls, x, arr):
        arr.append(x)
        i = (len(arr) - 2) // 2
        while i >= 0 and arr[i] < x:
            cls.Heapify(arr, len(arr), i)
            i = (i - 1) // 2

    @classmethod
    def extract_root(cls, arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        cls.Heapify(arr, len(arr) - 1, 0)


class MinHeap(MaxHeap):
    """
    A Min Heap Data Structure.
    ABT's operations: insert, extract_root
    Functions: Heapify, Build_Heap, Heap_Sort
    """
    @classmethod
    def Heapify(cls, arr, n, i):
        l = 2 * i + 1 # left child
        r = 2 * i + 2 # right child
        minimal = i
        left = l < n
        right = r < n

        # check if child bigger than parent
        if left and arr[l] <= arr[minimal]:
            minimal = l

        if right and arr[r] < arr[minimal]:
            minimal = r

        if minimal != i:
            arr[i], arr[minimal] = arr[minimal], arr[i] # swap parent with largest child
            cls.Heapify(arr, n, minimal)

    @classmethod
    def insert(cls, x, arr):
        arr.append(x)
        i = (len(arr) - 2) // 2
        while i >= 0 and arr[i] > x:
            cls.Heapify(arr, len(arr), i)
            i = (i - 1) // 2

