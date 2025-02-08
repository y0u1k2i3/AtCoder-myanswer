X = int(input())
grid = [[None] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        grid[i][j] = (i + 1) * (j + 1)

ans = 0
for i in range(9):
    for j in range(9):
        if grid[i][j] != X:
            ans += grid[i][j]

print(ans)