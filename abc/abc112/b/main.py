N, T = map(int, input().split())
min_cost = float('inf')
route_t = None
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        min_cost = min(min_cost, c)
        route_t = t

if route_t is None:
    print('TLE')
else:
    print(min_cost)