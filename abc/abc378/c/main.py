from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = [0] * n
idx_cnt = defaultdict(lambda: -1)

for i in range(n):
    if i == 0:
        b[i] = -1
        idx_cnt[a[i]] = i + 1
    else:
        if idx_cnt[a[i]] == -1:
            b[i] = -1
            idx_cnt[a[i]] = i + 1
        else:
            b[i] = idx_cnt[a[i]]
            idx_cnt[a[i]] = i + 1

for i in range(n):
    if i == n - 1:
        print(b[i])
    else:
        print(b[i], end=' ')

    