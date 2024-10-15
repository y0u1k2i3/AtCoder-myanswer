n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

# n = 4(i <= 2)
# (i = 1, (1, 4)) -> (x, y) = (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)
# (i = 2, (2, 3)) -> (x, y) = (2, 2), (2, 3), (3, 2), (3, 3)
for i in range(1, n // 2 + 1):
    limit = n + 1 - i
    # # iを固定
    # x = i
    # for y in range(i, limit + 1):
    #     col = grid[x - 1][y - 1]
    #     grid[y - 1][n - x] = col
    
    # # limitを固定
    # y = limit
    # for x in range(i, limit + 1):
    #     col = grid[x - 1][y - 1]
    #     grid[y - 1][n - x] = col

    

for i in range(n):
    print(''.join(grid[i]))