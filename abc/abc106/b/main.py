from collections import defaultdict
n = int(input())
# 1 3 5 7 15 21 35 105
# 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
# 105 165 195
# 1 3 5 9 15 45
# 1 3 5 15 25 75
prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ans = 0
for i in range(1, n + 1, 2):
    divisors = defaultdict(int)
    for p in prime_nums:
        m = i
        divisors[p] = 0
        while m % p == 0:
            m = m // p
            divisors[p] += 1

    divisor_num = 1
    for key in divisors:
        if divisors[key] != 0:
            divisor_num *= divisors[key] + 1

    if divisor_num >= 8:
        ans += 1

print(ans)
