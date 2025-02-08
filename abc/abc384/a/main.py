N, c1, c2 = map(str, input().split())
N = int(N)
S = list(input())

for i in range(len(S)):
    if S[i] != c1:
        S[i] = c2

print(''.join(S))