import time


def BinSearch(array, n, key):
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2
        if key == array[mid]:
            return mid
        elif key < array[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return -1

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        print(f"Running time: {time.time() - start}")
        return value
    return wrapper

@timer
def main(arr):
    print(BinSearch(arr, len(arr), 12))

if __name__ == "__main__":
    arr = [i for i in range(100_000)]
    main(arr)

