"""

Insertion Sort algorithm.

"""


def InsertionSort(A):
    for i in range(1, len(A)):
        num = A[i]
        j = i - 1
        # check if previous number is bigger than num
        while j >= 0 and num <= A[j]:
            A[j + 1], A[j] = A[j], num # if it is swap a number with num
            j -= 1

