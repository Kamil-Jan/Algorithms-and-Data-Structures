def LCS(string1, string2):
    n = len(string1)
    m = len(string2)
    table = [[(0, "") for col in range(m + 1)] for row in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                diagonal_cell_val, sequence = table[i - 1][j - 1]
                table[i][j] = (1 + diagonal_cell_val, sequence + string1[i - 1])
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][m]

