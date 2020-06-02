def knapsack_problem(profits, weights, n, W):
    V = [[0 for col in range(W + 1)] for row in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            product_weight = weights[i - 1]
            if product_weight <= w:
                new_weight = V[i - 1][w - product_weight] + profits[i - 1]
                V[i][w] = max(V[i - 1][w], new_weight)
            else:
                V[i][w] = V[i - 1][w]
    return V[n][w]

