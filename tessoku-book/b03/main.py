n = int(input())
a = list(map(int, input().split()))

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if a[i] + a[j] >= 1000:
            continue
        for k in range(j + 1, n):
            if a[i] + a[j] + a[k] == 1000:
                print('Yes')
                exit()

print('No')