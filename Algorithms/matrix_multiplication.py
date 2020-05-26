import numpy as np


def multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for col in range(cols_B)] for row in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(rows_B):
                C[i][j] += A[i][k] * B[k][j]
    return C

# A = np.array([])
# B = np.array([])
# C = multiply(A, B)
# C2 = A.dot(B)


