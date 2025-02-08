H, W, K = map(int, input().split())
grid = [list(input()) for _ in range(H)]

vistied = [[False] * W for _ in range(H)]
ans = 0

def dfs(i, j, k):
    global ans
    if k == K:
        ans += 1
        return
    vistied[i][j] = True
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '.'  and not vistied[ni][nj]:
            dfs(ni, nj, k + 1)
    vistied[i][j] = False

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            dfs(i, j, 0)

print(ans)


