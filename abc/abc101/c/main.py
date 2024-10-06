n, k = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
ans = 0
len_a = len(a) - 1

for i in range(len(a)):
    len_a -= k - 1
    ans += 1
    if len_a <= 0:
        break

print(ans)