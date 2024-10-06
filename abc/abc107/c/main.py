n, k = map(int, input().split())
x = list(map(int, input().split()))
# 6 3
# -30 -10 0 10 20 50

ans = float('inf')
for i in range(n - k + 1):
    time = 0
    x_l = x[i]
    x_r = x[i + k - 1]
    if x_r < 0:
        time = abs(x_l)
    elif x_l >= 0:
        time = x_r
    elif x_l < 0 and x_r >= 0:
        if abs(x_l) > x_r:
            time = abs(x_l) + x_r * 2
        else:
            time = abs(x_l) * 2 + x_r
    ans = min(ans, time)

print(ans)