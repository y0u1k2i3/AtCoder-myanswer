k = int(input())
ans = 0
for i in range(1, k + 1):
    for j in range(i + 1, k + 1, 2):
        ans += 1

print(ans)