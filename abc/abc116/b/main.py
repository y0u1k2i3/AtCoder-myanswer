from collections import defaultdict
s = int(input())
cnt = defaultdict(int)
cnt[s] += 1
i = 2
ai = s
while True:
    if ai % 2 == 0:
        ai = ai // 2
    else:
        ai = 3 * ai + 1
    cnt[ai] += 1
    if cnt[ai] > 1:
        print(i)
        exit()
    i += 1