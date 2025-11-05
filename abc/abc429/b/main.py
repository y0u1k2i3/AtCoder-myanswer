N, M = map(int, input().split())
A = list(map(int, input().split()))
sum_A = sum(A)
for i in range(N):
    if sum_A - A[i] == M:
        print("Yes")
        exit()

print("No")
