n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points = sorted(points, key=lambda x: x[2], reverse=True)

for cx in range(101):
    for cy in range(101):
        valid = True
        H = None
        for x, y, h in points:
            if h > 0:
                est_H = h + abs(x - cx) + abs(y - cy)
                if H is None:
                    H = est_H
                if H != est_H:
                    valid = False
                    break
            else:
                if H is not None and H - abs(x - cx) - abs(y - cy) > 0:
                    valid = False
                    break
        if valid:
            print(cx, cy, H)
            exit()

