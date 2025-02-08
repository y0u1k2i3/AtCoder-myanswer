N, M = map(int, input().split())
grid_N = []
for i in range(N):
    grid_N.append(list(input()))
grid_M = []
for i in range(M):
    grid_M.append(list(input()))

for j in range(N - M + 1):
    new_grid = []
    for i in range(N):
        new_grid.append(grid_N[i][j : j + M])
    if new_grid == grid_M:
        row, colum = i + 1, j + 1
        break

print(row, colum)
