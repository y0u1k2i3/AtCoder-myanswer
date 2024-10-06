from itertools import product

n = int(input())
len_n = len(str(n))
def sum_357(x):
    if x <= 2:
        return 0
    nums = [3, 5, 7]
    combinations = product(nums, repeat=x)
    num_357 = [''.join(map(str, comb)) for comb in combinations]
    ans = 0
    for num in num_357:
        if set(num) == set('357') and int(num) <= n:
            ans += 1
    return ans + sum_357(x - 1)

print(sum_357(len_n))