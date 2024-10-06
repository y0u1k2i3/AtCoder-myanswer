a = list(map(int, input().split()))
ans = 10000
for i in range(len(a)):
    if i == 0:
        a1 = abs(a[i] - a[1]) + abs(a[1] - a[2])
        a2 = abs(a[i] - a[2]) + abs(a[2] - a[1])
    elif i == 1:
        a1 = abs(a[i] - a[0]) + abs(a[0] - a[2])
        a2 = abs(a[i] - a[2]) + abs(a[2] - a[0])
    else:
        a1 = abs(a[i] - a[0]) + abs(a[0] - a[1])
        a2 = abs(a[i] - a[1]) + abs(a[1] - a[0])
    pre_ans = min(a1, a2)
    ans = min(ans, pre_ans)

print(ans)