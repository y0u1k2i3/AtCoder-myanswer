n, k = map(int, input().split())

# (a + b) % k == 0 and (b + c) % k == 0 and (c + a) % k == 0
# a % k == b % k == c % k == (0 or k // 2)
# kが奇数の場合、a % k == b % k == c % k == 0
# kが偶数の場合、a % k == b % k == c % k == 0 or k // 2
# k = 5 -> 

ans = 0
m1 = 0
for i in range(1, n + 1):
    if i % k == 0:
        m1 += 1

ans = m1 ** 3

if k % 2 == 0:
    m2 = 0
    for i in range(1, n + 1):
        if i % k == k // 2:
            m2 += 1
    ans += m2 ** 3

print(ans)