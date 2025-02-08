S = list(input())
ans = 0
p = 0

while p < len(S):
    ans += 1
    if p < len(S) - 1 and S[p] == "0" and S[p + 1] == "0":
        p += 2
    else:
        p += 1

print(ans)
