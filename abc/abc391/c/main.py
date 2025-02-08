from collections import defaultdict

N, Q = map(int, input().split())
pigeons = defaultdict(int)
pigeons_area = defaultdict(int)
ans = 0

for i in range(N):
    pigeons[i] = 1
    pigeons_area[i] = i

for i in range(Q):
    inputs = input()
    if inputs == "2":
        print(ans)
    else:
        inputs = list(map(int, inputs.split(" ")))
        query = inputs[0]
        # p = 移動する鳩
        p = inputs[1] - 1
        # h = 鳩を移動させる場所
        h = inputs[2] - 1
        # 鳩を移動
        p_idx = pigeons_area[p]
        prev_p = pigeons[p_idx]
        pigeons[p_idx] -= 1
        if prev_p == 2 and pigeons[p_idx] < 2 and ans > 0:
            ans -= 1
        prev_h = pigeons[h]
        pigeons[h] += 1
        if prev_h == 1 and pigeons[h] >= 2:
            ans += 1
        pigeons_area[p] = h

# 5 10

# 1 1 1 1 1

# 2
# 1 4 3
# 1 4 5
# 2
# 1 3 1
# 2
# 1 2 3
# 1 2 5
# 1 1 3
# 2
