N = int(input())
grid_S = [list(input()) for _ in range(N)]
grid_T = [list(input()) for _ in range(N)]

cnt_original = 0
for i in range(N):
    for j in range(N):
        if grid_S[i][j] != grid_T[i][j]:
            cnt_original += 1

# grid_Sを90度回転させる
grid_S_reverse1 = [[] * N for _ in range(N)]
cnt_reverse1 = 1
for j in range(N):
    for i in reversed(range(N)):
        grid_S_reverse1[j].append(grid_S[i][j])

for i in range(N):
    for j in range(N):
        if grid_S_reverse1[i][j] != grid_T[i][j]:
            cnt_reverse1 += 1

# grid_Sを180度回転させる
grid_S_reverse2 = [[] * N for _ in range(N)]
cnt_reverse2 = 2
for j in range(N):
    for i in reversed(range(N)):
        grid_S_reverse2[j].append(grid_S_reverse1[i][j])

for i in range(N):
    for j in range(N):
        if grid_S_reverse2[i][j] != grid_T[i][j]:
            cnt_reverse2 += 1

# grid_Sを270度回転させる
grid_S_reverse3 = [[] * N for _ in range(N)]
cnt_reverse3 = 3
for j in range(N):
    for i in reversed(range(N)):
        grid_S_reverse3[j].append(grid_S_reverse2[i][j])

for i in range(N):
    for j in range(N):
        if grid_S_reverse3[i][j] != grid_T[i][j]:
            cnt_reverse3 += 1

print(min(cnt_original, cnt_reverse1, cnt_reverse2, cnt_reverse3))
