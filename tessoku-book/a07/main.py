d = int(input())
n = int(input())
attendences = [0] * d

for i in range(d):
    attendences[i] = 0
for i  in range(n):
    l, r = map(int, input().split())
    attendences[l - 1] += 1
    if r < d:
        attendences[r] -= 1

sum_atd = [0] * d
for i in range(d):
    if i == 0:
        sum_atd[i] = attendences[i]
    else:
        sum_atd[i] = attendences[i] + sum_atd[i - 1]
    print(sum_atd[i])