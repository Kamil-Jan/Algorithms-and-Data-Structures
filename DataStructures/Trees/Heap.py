class MaxHeap:
    """
    A Max Heap Data Structure.
    ABT's operations: insert, extract_root
    Functions: heapify, build, sort
    """
    @classmethod
    def heapify(cls, arr, n, i, com_func):
        l = 2 * i + 1 # left child
        r = 2 * i + 2 # right child
        largest = i
        left = l < n
        right = r < n

        # check if children are greater than parent
        if left and com_func(arr[l], arr[largest]):
            largest = l

        if right and com_func(arr[r], arr[largest]):
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # swap parent with largest child
            cls.heapify(arr, n, largest, com_func) # check a new parent

    @classmethod
    def build(cls, array, com_func=lambda x, y: x > y):
        for i in range(len(array) // 2, -1, -1):
            cls.heapify(array, len(array), i, com_func)

    @classmethod
    def sort(cls, array, com_func=lambda x, y: x > y):
        cls.build(array)
        for i in range(len(array) - 1, -1, -1):
            array[0], array[i] = array[i], array[0]
            cls.heapify(array, i, 0, com_func)

    @classmethod
    def insert(cls, x, arr, com_func=lambda x, y: x > y):
        arr.append(x)
        i = (len(arr) - 2) // 2
        while i >= 0 and com_func(x, arr[i]):
            cls.heapify(arr, len(arr), i, com_func)
            i = (i - 1) // 2

    @classmethod
    def extract_root(cls, arr, com_func=lambda x, y: x > y):
        arr[0], arr[-1] = arr[-1], arr[0]
        root = arr.pop()
        cls.heapify(arr, len(arr), 0, com_func)
        return root


class MinHeap(MaxHeap):
    """
    A Min Heap Data Structure.
    ABT's operations: insert, extract_root
    Functions: heapify, build, sort
    """
    @classmethod
    def build(cls, array, com_func=lambda x, y: x < y):
        super().build(array, com_func)

    @classmethod
    def sort(cls, array, com_func=lambda x, y: x < y):
        super().sort(array, com_func)

    @classmethod
    def insert(cls, x, arr, com_func=lambda x, y: x < y):
        super().insert(x, arr, com_func)

    @classmethod
    def extract_root(cls, arr, com_func=lambda x, y: x < y):
        return super().extract_root(arr, com_func)

