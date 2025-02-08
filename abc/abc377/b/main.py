grid = []
for i in range(8):
    grid.append(input())

ans_grid = [[1] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if grid[i][j] == '#':
            for k in range(8):
                ans_grid[k][j] = 0
            for l in range(8):
                ans_grid[i][l] = 0

ans = 0
for i in range(8):
    for j in range(8):
        ans += ans_grid[i][j]

print(ans)