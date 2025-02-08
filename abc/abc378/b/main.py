N = int(input())
Qs = []
Rs = []
for i in range(N):
    q, r = map(int, input().split())
    Qs.append(q)
    Rs.append(r)

Q = int(input())
for i in range(Q):
    t, d = map(int, input().split())
    q_i, r_i = Qs[t - 1], Rs[t - 1]
    if d <= r_i:
        print(r_i)
    else:
        # d以上になるまでに必要なq_iの追加回数を計算
        num_increments = (d - r_i + q_i - 1) // q_i
        r_i += num_increments * q_i
        print(r_i)
