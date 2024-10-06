M = int(input())
n = 0
a = []
m = M

while m > 0 and n <= 20:
    ai = 0
    while M - 3 ** (ai + 1) >= 0 and m - 3 ** (ai + 1) >= 0:
        # if M - 3 ** (ai + 1) >= 0 and m - 3 ** (ai + 1) >= 0:
        #     break
        ai += 1
    m -= 3 ** (ai)
    a.append(ai)
    n += 1

print(n)
for i in range(len(a)):
    if i == len(a) - 1:
        print(a[i])
    else:
        print(a[i], end=" ")