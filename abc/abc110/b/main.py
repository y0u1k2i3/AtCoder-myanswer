n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x = sorted(x)
y = sorted(y)

Z = list(range(X + 1, Y + 1))
for z in Z:
    if x[-1] < z <= y[0]:
        print('No War')
        exit()

print('War')