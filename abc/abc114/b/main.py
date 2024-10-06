s = input()
ans = float('inf')
for i in range(len(s) - 2):
    x = int(s[i:i + 3])
    ans = min(ans, abs(x - 753))

print(ans)