import sys

sys.setrecursionlimit(10**6)  # 再帰の上限を増やす

N, M = map(int, input().split())
gragh = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    gragh[u - 1].append(v - 1)
    gragh[v - 1].append(u - 1)

visited = [False] * N
# 閉路数をカウント
cnt = 0

# DFSで閉路検出
def dfs(v):
    visited[v] = True
    for nv in gragh[v]:
        if not visited[nv]:
            dfs(nv)

for i in range(N):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(M - (N - cnt))
