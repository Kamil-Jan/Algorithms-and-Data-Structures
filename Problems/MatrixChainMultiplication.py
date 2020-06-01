from random import randint
import numpy as np
import time


def multiply(*matrices):
    sizes = [len(matrices[0])]
    for matrix in matrices:
        sizes.append(len(matrix[0]))
    s = create_order(len(matrices), sizes)
    output_matrix = _multiply(s, 1, len(matrices), matrices)
    return output_matrix

def _multiply(s, n, m, matrices):
    if n == m:
        new_matrix = matrices[n - 1]
    else:
        matrix1 = _multiply(s, n, s[n][m], matrices)
        matrix2 = _multiply(s, s[n][m] + 1, m, matrices)
        new_matrix = matrix1.dot(matrix2)
    return new_matrix

def create_order(n, p):
    n += 1
    inf = float("inf")

    m = [[0 if i == j else inf for j in range(n + 1)] for i in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for d in range(1, n):
        for i in range(1, n - d):
            j = i + d
            for k in range(1, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return s

for _ in range(3):
    matrices = []
    for _ in range(100):
        matrices.append(np.array([[randint(1, 100) for col in range(100)] for row in range(100)]))

    start = time.time()
    matrix = multiply(*matrices)
    my_func = time.time() - start
    print(f"My method: {my_func}")

    start = time.time()
    new_matrix = matrices[0].dot(matrices[1])
    for i in range(2, len(matrices)):
        new_matrix = new_matrix.dot(matrices[i])
    rglr_multiplication = time.time() - start
    print(f"Regular multiplication: {rglr_multiplication}")
    print(f"difference: {rglr_multiplication - my_func}")

