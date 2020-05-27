class MaxHeap:
    """
    A Max Heap Data Structure.
    ABT's operations: insert, extract_root
    Functions: Heapify, Build_Heap, Heap_Sort
    """
    @classmethod
    def Heapify(cls, arr, n, i, com_func):
        l = 2 * i + 1 # left child
        r = 2 * i + 2 # right child
        largest = i
        left = l < n
        right = r < n

        # check if a children are greater than parent
        if left and com_func(arr[l], arr[largest]):
            largest = l

        if right and com_func(arr[r], arr[largest]):
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # swap parent with largest child
            cls.Heapify(arr, n, largest, com_func) # look at a child

    @classmethod
    def Build_Heap(cls, array, com_func=lambda x, y: x > y):
        for i in range(len(array) // 2, -1, -1):
            cls.Heapify(array, len(array), i, com_func)

    @classmethod
    def Heap_Sort(cls, array, com_func=lambda x, y: x > y):
        cls.Build_Heap(array)
        for i in range(len(array) - 1, -1, -1):
            array[0], array[i] = array[i], array[0]
            cls.Heapify(array, i, 0, com_func)

    @classmethod
    def insert(cls, x, arr, com_func=lambda x, y: x > y):
        arr.append(x)
        i = (len(arr) - 2) // 2
        while i >= 0 and com_func(x, arr[i]):
            cls.Heapify(arr, len(arr), i, com_func)
            i = (i - 1) // 2

    @classmethod
    def extract_root(cls, arr, com_func=lambda x, y: x > y):
        arr[0], arr[-1] = arr[-1], arr[0]
        root = arr.pop()
        cls.Heapify(arr, len(arr), 0, com_func)
        return root


class MinHeap(MaxHeap):
    """
    A Min Heap Data Structure.
    ABT's operations: insert, extract_root
    Functions: Heapify, Build_Heap, Heap_Sort
    """
    @classmethod
    def Build_Heap(cls, array, com_func=lambda x, y: x < y):
        super().Build_Heap(array, com_func)

    @classmethod
    def Heap_Sort(cls, array, com_func=lambda x, y: x < y):
        super().Heap_Sort(array, com_func)

    @classmethod
    def insert(cls, x, arr, com_func=lambda x, y: x < y):
        super().insert(x, arr, com_func)

    @classmethod
    def extract_root(cls, arr, com_func=lambda x, y: x < y):
        return super().extract_root(arr, com_func)

