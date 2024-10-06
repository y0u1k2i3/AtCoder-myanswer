n, k = map(int, input().split())
average = n // k
remainder = n % k
senbei = [0] * k

for i in range(k):
    senbei[i] = average

i = 0
while remainder > 0:
    senbei[i] += 1
    i += 1
    if i == k - 1:
        i = 0
    remainder -= 1

senbei.sort()
print(abs(senbei[0] - senbei[-1]))