import time as t


N = [i for i in range(10_000_000)]
start = t.time()

#Search a peak in an array. b is a peak iff b >= a and b >= c
def search(array, left, right):
    while left <= right:
        try:
            mid = left + (right - left) // 2
            if array[mid] < N[mid - 1]:
                right = mid
            elif array[mid] < array[mid + 1]:
                left = mid
            else:
                return array[mid]
        except:
            return array[mid]

print(search(N, 0, len(N)))
print(t.time() - start)

