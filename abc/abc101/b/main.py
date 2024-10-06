n = int(input())
str_n = str(n)

s_n = 0
for i in range(len(str_n)):
    s_n += int(str_n[i])

if n % s_n == 0:
    print('Yes')
else:
    print('No')