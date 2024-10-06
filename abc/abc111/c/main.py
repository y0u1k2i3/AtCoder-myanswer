from audioop import reverse
from collections import defaultdict

n = int(input())
v = list(map(int, input().split()))

# 奇数番号と偶数番号で分ける？
odd_cnt = defaultdict(int)
even_cnt = defaultdict(int)

for i in range(n):
    if i % 2 == 0:
        odd_cnt[v[i]] += 1
    else:
        even_cnt[v[i]] += 1

odd_cnt = sorted(odd_cnt.items(), key=lambda x: x[1], reverse=True)
even_cnt = sorted(even_cnt.items(), key=lambda x: x[1], reverse=True)
len_odd = len(odd_cnt)
len_even = len(even_cnt)

odd_ans = float('inf')
even_ans = float('inf')
odd_flag = False
even_flag = False
i = 0
j = 0

if len_odd == 1 and len_even == 1:
    if odd_cnt[0][0] == even_cnt[0][0]:
        print(n - max(odd_cnt[0][1], even_cnt[0][1]))
        exit()
    else:
        print(0)
        exit()

if odd_cnt[0][0] != even_cnt[0][0]:
    print(n - odd_cnt[0][1] - even_cnt[0][1])
else:
    ans1 = n - odd_cnt[0][1] - even_cnt[1][1]
    ans2 = n - odd_cnt[1][1] - even_cnt[0][1]
    print(min(ans1, ans2))
