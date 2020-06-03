import sys
sys.path.insert(1, "..\\DataStructures\\Trees")
from Heap import MinHeap as mh



def MergeLists(lists, merge_com_func=lambda x, y: x < y):
    com_func = lambda x, y: len(x) < len(y)

    mh.build(lists, com_func)
    cost = 0
    while len(lists) > 1:
        smallest_list = mh.extract_root(lists, com_func)
        second_smallest_list = mh.extract_root(lists, com_func)
        m = len(smallest_list)
        n = len(second_smallest_list)

        new_list = Merge(smallest_list, second_smallest_list,
                         m, n, merge_com_func)
        mh.insert(new_list, lists, com_func)
        cost += m + n
    return lists[0]

def Merge(A, B, m, n, merge_com_func):
    """
    Merging two sorted lists.
    """
    i = j = 0
    arr = []

    while i < m and j < n:
        if merge_com_func(A[i], B[j]):
            arr.append(A[i])
            i += 1
        else:
            arr.append(B[j])
            j += 1

    while i < m:
        arr.append(A[i])
        i += 1

    while j < n:
        arr.append(B[j])
        j += 1
    return arr

