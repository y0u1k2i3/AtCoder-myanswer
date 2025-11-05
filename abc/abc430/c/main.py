import bisect

N, A, B = map(int, input().split())
S = input()

a_cnt = []
b_cnt = []
# a，bの個数を累積和で管理
for ch in S:
    if ch == "a":
        a_cnt.append(a_cnt[-1] + 1 if a_cnt else 1)
        b_cnt.append(b_cnt[-1] if b_cnt else 0)
    elif ch == "b":
        a_cnt.append(a_cnt[-1] if a_cnt else 0)
        b_cnt.append(b_cnt[-1] + 1 if b_cnt else 1)

ans = []
for l in range(N):
    a_r =
