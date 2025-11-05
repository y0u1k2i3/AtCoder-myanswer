N, M = map(int, input().split())
B = list(map(int, input().split()))
B.sort(reverse=True)
W = list(map(int, input().split()))
W.sort(reverse=True)

sum_ball = 0
sum_balls = [0]
last_idx = 0
query_num = min(len(B), len(W))
for i in range(query_num):
    b = B[i]
    w = W[i]
    last_idx = i
    if B[i] >= 0 and W[i] >= 0:
        sum_ball += B[i] + W[i]
    elif B[i] > 0 and W[i] < 0:
        sum_ball += B[i]
    elif B[i] < 0 and W[i] > 0:
        sum_ball += B[i] + W[i]
    elif B[i] < 0 and W[i] < 0:
        sum_ball += B[i] + W[i]

    sum_balls.append(sum_ball)
    if b < 0 and w < 0:
        break

if len(B) > len(W) and last_idx == len(W) - 1:
    for i in range(last_idx + 1, len(B)):
        sum_ball += B[i]
        sum_balls.append(sum_ball)
        if B[i] < 0:
            break

print(max(sum_balls))
