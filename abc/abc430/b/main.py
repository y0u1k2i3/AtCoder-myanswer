N, M = map(int, input().split())
grids = [list(input()) for _ in range(N)]

ans = set()
for i in range(N):
    for j in range(N):
        extracted_grid = []
        if (0 <= i <= N - M) and (0 <= j <= N - M):
            for k in range(i, i + M):
                extracted_grid.append(grids[k][j : j + M])
            ans.add(tuple(map(tuple, extracted_grid)))

print(len(ans))
