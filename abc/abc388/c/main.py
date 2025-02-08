import bisect

N = int(input())
A = list(map(int, input().split()))
if A[0] > A[-1] // 2:
    print(0)
    exit()

ans = 0
for i in range(1, len(A)):
    i_ans = bisect.bisect(A, A[i] // 2)
    ans += i_ans

print(ans)