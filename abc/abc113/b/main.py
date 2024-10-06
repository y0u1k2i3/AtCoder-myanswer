n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ave_t = float('inf')
ave_h_idx = 0
for i in range(n):
    ave = t - h[i] * 0.006
    if abs(a - ave) < abs(a - ave_t):
        ave_t = ave
        ave_h_idx = i + 1

print(ave_h_idx)