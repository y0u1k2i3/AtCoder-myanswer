n, c = map(int, input().split())
t = list(map(int, input().split()))
ans = 1
delay = t[0]
for i in range(1, n):
    if t[i] - delay >= c:
        ans += 1
        delay = t[i]

print(ans)