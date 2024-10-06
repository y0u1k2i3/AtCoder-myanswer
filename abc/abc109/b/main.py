from collections import defaultdict
n = int(input())
pre = None
s_cnt = defaultdict(int)

for i in range(n):
    s = input()
    s_cnt[s] += 1
    if s_cnt[s] > 1:
        print('No')
        exit()
    if i != 0:
        if pre[-1] != s[0]:
            print('No')
            exit()
    pre = s

print('Yes')