from math import lcm

n = int(input())
a = list(map(int, input().split()))

m = lcm(*a) - 1
ans = 0
for i in range(n):
    ans += m % a[i]

print(ans)
