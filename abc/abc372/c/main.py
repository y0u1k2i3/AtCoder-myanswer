n, q = map(int, input().split())
s = list(input())

ans = 0
for i in range(0, n - 2):
    if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
        ans += 1

for i in range(q):
    x, c = input().split()
    x = int(x) - 1
    if s[x] == c:
        print(ans)
    else:
        for k in range(3):
            y = x - k
            if 0 <= y <= n - 3:
                if s[y] == 'A' and s[y + 1] == 'B' and s[y + 2] == 'C':
                    ans -= 1

        s[x] = c

        for k in range(3):
            y = x - k
            if 0 <= y <= n - 3:
                if s[y] == 'A' and s[y + 1] == 'B' and s[y + 2] == 'C':
                    ans += 1
        print(ans)