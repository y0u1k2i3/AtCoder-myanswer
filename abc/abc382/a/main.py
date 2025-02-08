N, D = map(int, input().split())
S = list(input())

cnt_cukky = 0
cnt_empty = 0
for i in range(N):
    if S[i] == '@':
        cnt_cukky += 1
    elif S[i] == '.':
        cnt_empty += 1

print(D + cnt_empty)