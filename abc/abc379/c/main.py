n, m = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
if sum(X) != n:
    print(-1)
    exit()

elif X[-1] == n:
    if A[-1] > 1:
        print(-1)
        exit()

for i in range(m):
    if i < m - 1:
        dis = X[i + 1] - X[i]
        if A[i] - 1 < dis - 1:
            print(-1)
            exit()
        else:
            ans += (dis + 1) * dis // 2
            A[i] -= dis
            if A[i] > 1:
                ans += (A[i] - 1) * dis
                A[i + 1] += A[i] - 1
    else:
        if X[i] == n:
            if A[i] > 1:
                print(-1)
                exit()
        else:
            dis = n - X[i]
            if A[i] - 1 != dis:
                print(-1)
                exit()

print(ans)