import sys
sys.path.insert(1, "..\\DataStructures\\Trees")
from BST import BST
from pprint import pprint


def create_tree(keys, s_frequencies, u_frequencies=None):
    if not u_frequencies:
        roots = create_tableS(len(keys), s_frequencies)
    else:
        roots = create_tableSU(len(keys), s_frequencies, u_frequencies)
    t = BST()
    insert_keys(t, keys, roots, 0, len(keys))
    return t

def insert_keys(t, keys, roots, i, j):
    if i == j:
        return
    root = roots[i][j]
    key = keys[root - 1]
    t.insert(key)
    insert_keys(t, keys, roots, i, root  - 1)
    insert_keys(t, keys, roots, root, j)

def create_tableS(n, frequencies):
    """
    Successful search only.
    """
    inf = float("inf")
    m = [[inf for col in range(n + 1)] for row in range(n + 1)]
    roots = [[None for col in range(n + 1)] for row in range(n + 1)]
    for d in range(n + 1):
        for i in range(n - d + 1):
            j = i + d
            if i == j:
                m[i][j] = 0
                continue
            for k in range(i + 1, j + 1):
                new_cost = m[i][k - 1] + m[k][j] + sum(frequencies[i: j])
                if new_cost < m[i][j]:
                    m[i][j] = new_cost
                    roots[i][j] = k
    return roots

def create_tableSU(n, s_frequencies, u_frequencies):
    """
    Successful and unsuccessful search.
    """
    inf = float("inf")
    m = [[inf for col in range(n + 1)] for row in range(n + 1)]
    weights = [[0 for col in range(n + 1)] for row in range(n + 1)]
    roots = [[None for col in range(n + 1)] for row in range(n + 1)]
    for d in range(n + 1):
        for i in range(n - d + 1):
            j = i + d
            if i == j:
                m[i][j] = 0
                weights[i][j] = u_frequencies[j]
                continue
            weight = weights[i][j - 1] + s_frequencies[j] + u_frequencies[j]
            weights[i][j] = weight
            for k in range(i + 1, j + 1):
                new_cost = m[i][k - 1] + m[k][j] + weight
                if new_cost < m[i][j]:
                    m[i][j] = new_cost
                    roots[i][j] = k
    return roots

print(create_tree([10,20,30,40], [0,3,3,1,1], [2,3,1,1,1]))
print(create_tree([10,20,30,40], [4,2,6,3]))


