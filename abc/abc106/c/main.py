s = input()
k = int(input())

cnt_not1 = False
ans = 1
if k <= len(s):
    for i in range(len(s)):
        if s[i] != '1':
            if not cnt_not1:
                cnt_not1 = True
                ans = s[i]
        if i == k - 1:
            if cnt_not1:
                print(ans)
                exit()
            else:
                print(1)
                exit()

else:
    for i in range(len(s)):
        if s[i] != '1':
            print(s[i])
            exit()