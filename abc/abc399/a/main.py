N = int(input())
S = input()
T = input()
list_S = list(S)
list_T = list(T)

ans = 0
for i in range(N):
    if list_S[i] != list_T[i]:
        ans += 1

print(ans)
