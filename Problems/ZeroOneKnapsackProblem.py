def knapsack_problem(items, profits, weights, W):
    n = len(profits)
    V = [[(0, 0, row, col) for col in range(W + 1)] for row in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            product_weight = weights[i - 1]
            if product_weight <= w:
                new_weight = V[i - 1][w - product_weight][0] + profits[i - 1]
                prev_weight = V[i - 1][w][0]
                if prev_weight > new_weight:
                    V[i][w] = (prev_weight, 0, i - 1, w)
                else:
                    V[i][w] = (new_weight, 1, i - 1, w - product_weight)
            else:
                V[i][w] = (V[i - 1][w][0], 0, i - 1, w)

    _, is_item_taken, i, j = V[n][w]
    items_dict = dict()
    for k in range(n - 1, -1, -1):
        items_dict[items[k]] = is_item_taken
        _, is_item_taken, i, j = V[i][j]
    return V[n][w][0], items_dict

if __name__ == "__main__":
    items = ["red","grey","blue","green","yellow"]
    p = [1,2,2,4,10]
    w = [1,1,2,12,4]
    W = 15
    print(knapsack_problem(items, p, w, W))

