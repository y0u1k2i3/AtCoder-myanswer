S = input()
list_S = list(S)
ans = 0
for i in range(len(list_S)):
    for k in range(1, (len(list_S) - (i + 1)) // 2 + 1):
        if (list_S[i] == "A") and (list_S[i + k] == "B") and (list_S[i + 2 * k] == "C"):
            ans += 1

print(ans)

# 111111
