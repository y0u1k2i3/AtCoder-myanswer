n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= i + 1
a = sorted(a)

if n % 2 == 1:
    mid = a[n // 2]
else:
    mid = (a[n // 2 - 1] + a[n // 2]) // 2
ans = 0

for i in range(n):
    ans += abs(a[i] - mid)

print(ans)

