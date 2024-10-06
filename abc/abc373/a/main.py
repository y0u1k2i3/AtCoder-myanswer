ans = 0
for i in range(1, 13):
    s = input()
    len_s = len(s)
    if len_s == i:
        ans += 1

print(ans)