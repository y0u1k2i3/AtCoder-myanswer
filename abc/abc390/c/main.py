H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

min_H = float("inf")
min_W = float("inf")
max_H = 0
max_W = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            min_H = min(min_H, i)
            min_W = min(min_W, j)
            max_H = max(max_H, i)
            max_W = max(max_W, j)

for i in range(min_H, max_H + 1):
    for j in range(min_W, max_W + 1):
        if grid[i][j] == ".":
            print("No")
            exit()

print("Yes")