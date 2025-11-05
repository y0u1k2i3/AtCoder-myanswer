N, M = map(int, input().split())
CONST = 10 ** 9
X = 0
for i in range(M + 1):
    X += N ** i

if X <= CONST:
    print(X)
else:
    print("inf")
