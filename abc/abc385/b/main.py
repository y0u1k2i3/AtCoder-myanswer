from collections import defaultdict

H, W, X, Y = map(int, input().split())
X = X - 1
Y = Y - 1
grid = []
pass_check = defaultdict(bool)
for i in range(H):
    for j in range(W):
        pass_check[(i, j)] = False

for i in range(H):
    S = list(input())
    grid.append(S)

T = list(input())
ans = 0

for i in range(len(T)):
    if T[i] == "U":
        if 0 <= X - 1 < H and 0 <= Y < W:
            if grid[X - 1][Y] != "#":
                X -= 1
                if grid[X][Y] == "@":
                    if pass_check[(X, Y)] == False:
                        ans += 1
                        pass_check[(X, Y)] = True

    elif T[i] == "D":
        if 0 <= X + 1 < H and 0 <= Y < W:
            if grid[X + 1][Y] != "#":
                X += 1
                if grid[X][Y] == "@":
                    if pass_check[(X, Y)] == False:
                        ans += 1
                        pass_check[(X, Y)] = True

    elif T[i] == "L":
        if 0 <= X < H and 0 <= Y - 1 < W:
            if grid[X][Y - 1] != "#":
                Y -= 1
                if grid[X][Y] == "@":
                    if pass_check[(X, Y)] == False:
                        ans += 1
                        pass_check[(X, Y)] = True

    elif T[i] == "R":
        if 0 <= X < H and 0 <= Y + 1 < W:
            if grid[X][Y + 1] != "#":
                Y += 1
                if grid[X][Y] == "@":
                    if pass_check[(X, Y)] == False:
                        ans += 1
                        pass_check[(X, Y)] = True

print(X + 1, Y + 1, ans)