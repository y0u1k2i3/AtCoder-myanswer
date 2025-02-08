from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hash_A = defaultdict(int)
for i in range(N):
    hash_A[A[i]] = A.index(A[i])

sorted_A = sorted(A)
for i in range(M):
    if sorted_A[0] <= B[i] <= sorted_A[N - 1]:
        print(-1)
    else:
        