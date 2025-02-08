from collections import defaultdict

a = list(map(int, input().split()))
cnt = defaultdict(int)
ans = 0

for i in range(4):
    cnt[a[i]] += 1
    if cnt[a[i]] % 2 == 0:
        ans += 1

print(ans)