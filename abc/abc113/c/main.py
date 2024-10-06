from collections import defaultdict

n, m = map(int, input().split())
P = []
Y = []
bth_year = [[] for _ in range(n)]
for i in range(m):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)
    bth_year[p - 1].append(y)

idx_dict = defaultdict(int)
for i in range(n):
    bth_year[i].sort()
    for j in range(len(bth_year[i])):
        idx_dict[(i + 1, bth_year[i][j])] = j + 1

for i in range(m):
    p = P[i]
    y = Y[i]
    idx = idx_dict[(p, y)]
    print(f'{p:06}{idx:06}')