from collections import defaultdict

X, Y = map(int, input().split())
# phenomenon_X = {2: }
# phenomenon_Y = {}
phenomenon = defaultdict(int)
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) >= X or abs(i - j) >= Y:
            phenomenon[(i, j)] = 1

ans = len(phenomenon) / 36
if ans == 0.0:
    print(0)
else:
    print(len(phenomenon) / 36)
