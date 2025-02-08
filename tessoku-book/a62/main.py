import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

n, m = map(int, input().split())

def dfs(pos, graph, visit_info):
    visit_info[pos] = True
    for i in graph[pos]:
        if not visit_info[i]:
            dfs(i, graph, visit_info)

edges = [list(map(int, input().split())) for _ in range(m)]
G = [list() for _ in range(n + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (n + 1)
dfs(1, G, visited)

for i in range(1, n + 1):
    if not visited[i]:
        print('The graph is not connected.')
        exit()

print('The graph is connected.')

