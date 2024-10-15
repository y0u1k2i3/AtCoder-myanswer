n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
    if i == 0:
        b[i] = a[i]
    else:
        b[i] = a[i] + b[i - 1]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    if l == 1:
        atari = b[r - 1]
        hazure = r - b[r - 1]
        if atari > hazure:
            print('win')
        elif atari == hazure:
            print('draw')
        else:
            print('lose')
    else:
        atari = b[r - 1] - b[l - 2]
        hazure = (r - l + 1) - atari
        if atari > hazure:
            print('win')
        elif atari == hazure:
            print('draw')
        else:
            print('lose')