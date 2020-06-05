import time
import random


def is_suitable(num, m, prev_numbers_sum, next_numbers_sum):
    if prev_numbers_sum + num > m:
        return False
    if prev_numbers_sum + next_numbers_sum < m:
        return False
    return True

def find_solutions(nums, m, next_nums_sum, cur_sum=0, i=0, chosen_nums=[]):
    if cur_sum == m:
        yield chosen_nums
    if i < len(nums):
        cur_num = nums[i]
        if is_suitable(cur_num, m, cur_sum, next_nums_sum):
            yield from find_solutions(nums, m,
                                      next_nums_sum - cur_num,
                                      cur_sum + cur_num,
                                      i + 1, chosen_nums + [cur_num])
            yield from find_solutions(nums, m,
                                      next_nums_sum - cur_num, cur_sum,
                                      i + 1, chosen_nums)

if __name__ == "__main__":
    w = [random.randint(1, 100_000) for _ in range(100)]
    m = 1_000_000
    start = time.time()
    print(next(find_solutions(w, m, sum(w))))
    print(time.time() - start)

