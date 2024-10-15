n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
    if i == 0:
        b[i] = a[i]
        continue
    b[i] = a[i] + b[i - 1]
for i in range(q):
    l, r = map(int, input().split())
    if l == 1:
        print(b[r - 1])
    else:
        print(b[r - 1] - b[l - 2])