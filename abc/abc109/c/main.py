from math import gcd
n, x = map(int, input().split())
x_list = list(map(int, input().split()))
dif_x = [None] * n

for i in range(n):
    dif_x[i] = abs(x_list[i] - x)

print(gcd(*dif_x))