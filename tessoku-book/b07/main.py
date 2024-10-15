t = int(input())
n = int(input())
a = [0] * t
for i in range(n):
    l, r = map(int, input().split())
    a[l] += 1
    if r < t:
        a[r] -= 1

b = [0] * t
for i in range(t):
    if i == 0:
        b[i] = a[i]
    else:
        b[i] = a[i] + b[i - 1]
    print(b[i])