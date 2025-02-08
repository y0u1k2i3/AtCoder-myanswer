N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if i == 0:
        if A[i] - (N - 1) >= 0:
            cnt += N - 1
            A[i] -= N - 1
        else:
            cnt += A[i]
            A[i] = 0
    else:
        A[i] += i
        if A[i] - (N - i - 1) >= 0:
            cnt += N - i - 1
            A[i] -= N - i - 1
        else:
            cnt += A[i]
            A[i] = 0

for i in range(N):
    if i != N - 1:
        print(A[i], end=" ")
    else:
        print(A[i])