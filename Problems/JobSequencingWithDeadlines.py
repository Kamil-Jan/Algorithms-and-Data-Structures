def Sequence(profits, deadlines):
    n = len(profits)
    profit_deadline_list = list(zip(range(1, n + 1), profits, deadlines))
    profit_deadline_list.sort(key=lambda x: x[1], reverse=True)

    sequence = [None for _ in range(max(deadlines))]
    best_profit = 0
    for queue_num, profit, deadline in profit_deadline_list:
        if not None in sequence:
            break
        i = deadline - 1
        while i >= 0:
            if not sequence[i]:
                sequence[i] = queue_num
                best_profit += profit
                break
            i -= 1
    return best_profit, sequence

