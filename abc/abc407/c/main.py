S = input()
t = ""
# 0を10と考えると，Bを押す回数は最も小さなSの値に依存する
min_num = float("inf")
s_cnt = set()
for s in list(map(int, S)):
    if s == 0:
        s_cnt.add(0)
        continue
    else:
        s_cnt.add(s)
        min_num = min(min_num, s)

if len(s_cnt) == 1 and list(s_cnt)[0] == 0:
    print(len(S))
    exit()

# Bボタンを押す回数ごとの結果
ans = [0] * (min_num + 1)

for btn_b_num in range(min_num + 1):
    for s in S:
        if s == "0":
            if btn_b_num == 0:
                ans[btn_b_num] += 1
            else:
                ans[btn_b_num] += 11 - btn_b_num
        else:
            ans[btn_b_num] += (int(s) + 1) - btn_b_num

for i in range(min_num + 1):
    ans[i] += i

print(min(ans))
