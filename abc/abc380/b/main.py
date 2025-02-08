s = list(input())
a = []

cnt = 0
for i in range(len(s)):
    if s[i] == '|':
        if i != 0:
            a.append(cnt)
        cnt = 0
    if s[i] == '-':
        cnt += 1

for i in range(len(a)):
    if i != len(a) - 1:
        print(a[i], end=' ')
    else:
        print(a[i])
