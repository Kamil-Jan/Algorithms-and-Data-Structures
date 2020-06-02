def knapsack_problem(profits, weights, W):
    profit_weight_list = list(map(list, zip(profits, weights)))

    # Sort objects by their p/w value.
    profit_weight_list.sort(key=lambda x: x[0] / x[1], reverse=True)
    best_profit = 0
    i = 0
    for item in profit_weight_list:
        i += 1
        profit, weight = item[0], item[1]
        if W - weight >= 0:
            W -= weight
            best_profit += profit
        else:
            best_profit += round((W * profit) / weight, 2)
            W = 0
            break
    return best_profit

