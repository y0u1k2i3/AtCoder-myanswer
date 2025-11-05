S = input()
list_S = list(S)
ans = ""
for i in range(len(list_S)):
    if list_S[i].isupper():
        ans += list_S[i]

print(ans)
