n = int(input())
ans = 0
n_list = list(str(n))
n_list.reverse()
for i in range(len(n_list)):
    ans += int(n_list[i]) * 2 ** i

print(ans)