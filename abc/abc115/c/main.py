n, k = map(int, input().split())
trees = []
for i in range(n):
    trees.append(int(input()))

trees = sorted(trees)
ans = float('inf')
# 1 2 3 4 5
for i in range(n - k + 1):
    h_dif = trees[i + k - 1] - trees[i]
    ans = min(ans, h_dif)

print(ans)