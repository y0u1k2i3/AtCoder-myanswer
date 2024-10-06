n = int(input())
K = list(map(int, input().split()))
sum_K = sum(K)

ans = float('inf')
for i in range(1 << n):
    ans_i = sum_K
    for j in range(n):
        if i & (1 << j):
            ans_i -= K[j]
    ans_i = max(ans_i, sum_K - ans_i)
    ans = min(ans, ans_i)
    
print(ans)