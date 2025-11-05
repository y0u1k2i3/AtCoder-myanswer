from collections import defaultdict

N, M = map(int, input().split())
# gragh = [[0] * N for _ in range(N)]
# for i in range(M):
#     u, v = map(int, input().split())
#     gragh[u - 1][v - 1] += 1
# ans = 0
# for i in range(N):
#     for j in range(i, N):
#         # if gragh[i][j] == gragh[j][i] == 1:
#         #     ans += 1
#         edges = gragh[i][j] + gragh[j][i]
#         if edges > 1:
#             ans += edges - 1

edges = defaultdict(int)
for i in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    edges[(u, v)] += 1

ans = 0
for (u, v), edge in edges.items():
    if u != v:
        if edge > 1:
            ans += edge - 1
    else:
        if edge > 0:
            ans += edge

print(ans)
