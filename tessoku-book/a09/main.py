h, w, n = map(int, input().split())
snow = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    snow[a][b] += 1
    snow[c + 1][d + 1] += 1
    snow[a][d + 1] -= 1
    snow[c + 1][b] -= 1

sum_snow = [[0] * (w + 2) for _ in range(h + 2)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        sum_snow[i][j] = snow[i][j] + sum_snow[i][j - 1]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        sum_snow[i][j] =sum_snow[i][j] + sum_snow[i - 1][j]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if j == w:
            print(sum_snow[i][j])
        else:
            print(sum_snow[i][j], end=' ')