import math

n = int(input())
sum_N = 0
xy = [(0, 0)] * (n + 1)
for i in range(n):
    x, y = map(int, input().split())
    xy[i + 1] = (x, y)
    sum_N += math.sqrt((x - xy[i][0]) ** 2 + (y - xy[i][1]) ** 2)

sum_N += math.sqrt((xy[n][0] - xy[0][0]) ** 2 + (xy[n][1] - xy[0][1]) ** 2)
print(sum_N)
