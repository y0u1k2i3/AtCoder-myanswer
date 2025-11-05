from collections import defaultdict

X = int(input())

# 良い整数は、必ず偶数
# for n in range(2, N + 1, 2):
max_a = 0
n = 2
while n <= X:
    max_a += 1
    n *= 2


ans = 0
count_X = defaultdict(bool)

b = 1
x = 2**1
while x <= X:
    if count_X[x]:
        break
    count_X[x] = True
    ans += 1
    b += 1
    x = (2**1) * (b**2)

for a in range(2, max_a + 1):
    while (2 ** a) * (b ** 2) > X:
        b -= 1
    ans += b - 1

print(ans)
