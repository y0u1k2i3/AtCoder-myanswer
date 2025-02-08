n = list(input())

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0

for i in range(len(n)):
    if n[i] == '1':
        cnt_1 += 1
    elif n[i] == '2':
        cnt_2 += 1
    elif n[i] == '3':
        cnt_3 += 1

if cnt_1 == 1 and cnt_2 == 2 and cnt_3 == 3:
    print('Yes')
else:
    print('No')