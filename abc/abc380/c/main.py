n, k = map(int, input().split())
s = list(input())

# input:
# 15_3
# 010011100011001

# output:
# 01001110111110001

# expected:
# 010011111000001

cnt_1s = 0
num_1 = 0
flag_1 = False

ans_s = ''
sub_ans_s = ''

for i in range(len(s)):
    if not flag_1:
        if cnt_1s < k - 1:
            ans_s += s[i]
        elif cnt_1s == k - 1:
            if s[i] == '0':
                sub_ans_s = s[i]
            else:
                flag_1 = True
        else:
            sub_ans_s += s[i]
    else:
        if s[i] == '1':
            num_1 += 1
        else:
            sub_ans_s += s[i]
            flag_1 = False

print(ans_s + '1' * num_1 + sub_ans_s)

 