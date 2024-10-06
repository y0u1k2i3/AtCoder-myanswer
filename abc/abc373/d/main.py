from collections import defaultdict

n, m = map(int, input().split())
U = []
V = []
W = []
X = defaultdict(int)
for i in range(m):
    u, v, w = map(int, input().split())
    U.append(u)
    V.append(v)
    W.append(w)
    X[i] = None

for i in range(m):
    u, v, w = U[i], V[i], W[i]
    if X[u] == None and X[v] == None:
        X[u] = 0
        X[v] = W
    elif X[u] == None:
        X[u] = X[v] - W
    elif X[v] == None:
        X[v] = X[u] + W

for i in range(m):
    if i != m - 1:
        print(X[i], end=' ') 
    else:
        print(X[i])