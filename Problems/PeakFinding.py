#Search a peak in an array. b is a peak iff b >= a and b >= c
def search(array, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] < array[mid - 1]:
            right = mid - 1
        elif array[mid] < array[mid + 1]:
            left = mid + 1
        else:
            return mid - 1, mid + 1
