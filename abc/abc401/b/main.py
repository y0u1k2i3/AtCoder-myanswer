N = int(input())
login_flg = False
err_cnt = 0
for i in range(N):
    S = input()
    if S == "login":
        login_flg = True
    elif S == "logout":
        login_flg = False

    if not login_flg and S == "private":
        err_cnt += 1

print(err_cnt)
