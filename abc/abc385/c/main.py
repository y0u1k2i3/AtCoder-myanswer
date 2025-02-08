from collections import defaultdict

N = int(input())
H = list(map(int, input().split()))
if len(set(H)) == 1:
    print(N)
    exit()
elif len(set(H)) == N:
    print(1)
    exit()

ans = 0

for i in range(N):
    cnt = 1
    for k in range(1, N - i + 1):
        pre = H[i]
        j = i
        while j + k < N:
            j += k
            if H[j] == pre:
                cnt += 1
        ans = max(ans, cnt)

print(ans)