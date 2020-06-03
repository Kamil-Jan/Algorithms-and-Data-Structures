from OptimalMergePattern import MergeLists
from collections import deque


def design(devices, costs, reliabilities, C):
    costs_sum = sum(costs)
    money_for_next_devices = C
    remaining_cost = C - costs_sum
    assert remaining_cost > 0, f"incorrect C value - {C}"
    device_maximum_quantity = [remaining_cost // cost + 1 for cost in costs]

    s = [(1, 0, dict())]
    for i, device in enumerate(devices):
        device_list = deque()
        costs_sum -= costs[i]
        money_for_next_devices = C - costs_sum
        for device_quantity in range(1, device_maximum_quantity[i] + 1):
            stage_list = deque()
            for reliability, total_cost, prev_devices_quantity in s:
                # Calculate new total cost.
                new_total_cost = total_cost + device_quantity * costs[i]
                if new_total_cost > money_for_next_devices:
                    break

                # Calculate current reliability.
                unreliability = (1 - reliabilities[i]) ** device_quantity
                stage_reliability = 1 - unreliability
                new_reliability = reliability * stage_reliability

                new_devices_quantity = prev_devices_quantity.copy()
                new_devices_quantity[device] = device_quantity

                stage_list.append((new_reliability, new_total_cost, new_devices_quantity))
            device_list.append(stage_list)

        merge_com_func = lambda x, y: x[0] < y[0]
        s = MergeLists(device_list, merge_com_func)
        # check contradictions
        i = 0
        while i < len(s) - 1:
            # cost of every element should be less than
            # cost next element.
            if s[i][1] > s[i + 1][1]:
                del s[i]
                i -= 1
            i += 1
    return s[-1]

d = [1,2,3]
c = [30,15,20]
r = [0.9,0.8,0.5]
C = 105

print(design(d, c, r, C))

