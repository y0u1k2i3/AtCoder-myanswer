from operator import index


N, D = map(int, input().split())
S = list(input())
S.reverse()

for i in range(D):
    cukky_idx = S.index("@")
    S[cukky_idx] = "."

S.reverse()

for i in range(N):
    if i != N - 1:
        print(S[i], end="")
    else:
        print(S[i])