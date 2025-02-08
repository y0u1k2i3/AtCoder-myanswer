n = int(input())
MAX_SIZE = 1500
xy = [[0] * (MAX_SIZE + 1) for _ in range(MAX_SIZE + 1)]
# 0 0 0 0 0
# 0 1 0 -1 0
# 0 0 0 0 0
# 0 -1 0 1 0
# 0 0 0 0 0

for i in range(n):
    a, b, c, d = map(int, input().split())
    xy[a][b] += 1
    xy[c][d] += 1
    xy[a][d] -= 1
    xy[c][b] -= 1

# 累積和の計算
xy_area = [[0] * (MAX_SIZE + 1) for _ in range(MAX_SIZE + 1)]
for i in range(MAX_SIZE + 1):
    for j in range(MAX_SIZE + 1):
        if j == 0:
            xy_area[i][j] = xy[i][j]
        else:
            xy_area[i][j] = xy[i][j] + xy_area[i][j - 1]

for j in range(MAX_SIZE + 1):
    for i in range(MAX_SIZE + 1):
        if i == 0:
            xy_area[i][j] = xy_area[i][j]
        else:
            xy_area[i][j] = xy_area[i][j] + xy_area[i - 1][j]

# 面積の計算
ans = 0
for j in range(MAX_SIZE + 1):
    for i in range(MAX_SIZE + 1):
        if xy_area[i][j] >= 1:
            ans += 1

print(ans)