N, K = map(int, input().split())
A = [1] * (N + 1)
A_i_sum = 1 * K
LIMIT = 10**9
if N + 1 < K:
    print(1)
    exit()

for i in range(K, N + 1):
    A[i] = A_i_sum
    A_i_sum = (A_i_sum - A[i - K] + A[i]) % LIMIT

print(A[N])
