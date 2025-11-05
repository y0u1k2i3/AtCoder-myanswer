from collections import defaultdict
import math

N = int(input())
A = list(map(int, input().split()))

num_cnt = defaultdict(int)

if len(set(A)) == 1:
    print(0)
    exit()

for a in A:
    num_cnt[a] += 1

ans = 0

for k, v in num_cnt.items():
    ans += math.comb(v, 2) * (N - v)

print(ans)
