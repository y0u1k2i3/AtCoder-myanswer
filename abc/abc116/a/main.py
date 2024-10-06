triangles = list(map(int, input().split()))
triangles.sort()
print(triangles[0] * triangles[1] // 2)