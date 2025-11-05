N = int(input())
S = input()
list_S = list(S)

# 1の個数を数える
cnt_1 = S.count("1")
now_1 = 0
ans = 0

for i in range(len(list_S)):
    if list_S[i] == "1":
        now_1 += 1
    else:
        ans += min(now_1, cnt_1 - now_1)

print(ans)
