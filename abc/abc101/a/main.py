s = input()

ans = 0

for i in range(len(s)):
    if s[i] == '+':
        ans += 1
    elif s[i] == '-':
        ans -= 1

print(ans)