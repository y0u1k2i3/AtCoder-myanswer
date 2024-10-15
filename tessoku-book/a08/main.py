h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(map(int, input().split())))

new_grid = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        new_grid[i][j] = grid[i - 1][j - 1] + new_grid[i][j - 1]

for j in range(w + 1):
    for i in range(h + 1):
        new_grid[i][j] = new_grid[i][j] + new_grid[i - 1][j]

q = int(input())
for i in range(q):
    a, b, c, d = map(int, input().split())
    print(new_grid[c][d] + new_grid[a - 1][b - 1] - new_grid[c][b - 1] - new_grid[a - 1][d])
