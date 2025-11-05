from collections import deque, defaultdict
from operator import le

N = int(input())
A = list(map(int, input().split()))
# left_que = deque()
# right_que = deque()
left_hash = defaultdict(int)
right_hash = defaultdict(int)
for i in range(N):
    # left_hash[A[i]] = 0
    # right_hash[A[i]] = 0
    if i == 0:
        # left_que.append(A[i])
        left_hash[A[i]] += 1
    else:
        # right_que.append(A[i])
        right_hash[A[i]] += 1

ans = len(left_hash) + len(right_hash)
ans_i = len(left_hash) + len(right_hash)
for i in range(1, N - 1):
    left_hash[A[i]] += 1
    right_hash[A[i]] -= 1
    if left_hash[A[i]] == 1:
        ans_i += 1
    if right_hash[A[i]] == 0:
        ans_i -= 1
    ans = max(ans, ans_i)

print(ans)
