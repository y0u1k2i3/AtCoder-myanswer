n, m = map(int, input().split())
ans = n * n

ans_grid = set()
dif = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

for i in range(m):
    a, b = map(int, input().split())
    ans_grid.add((a, b))
    for di, dj in dif:
        ans_grid.add((a + di, b + dj))

for i, j in ans_grid:
    if 1 <= i <= n and 1 <= j <= n:
        ans -= 1

print(ans)
