from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# Aの要素数をカウント
A_i_num = defaultdict(int)
for i in range(N):
    A_i_num[A[i]] += 1

# 要素数が1の数を持っている人をリストアップ
person_to_num = defaultdict(int)
min_num = float("inf")

for i in range(N):
    if A_i_num[A[i]] == 1:
        person_to_num[i + 1] = A[i]
    min_num = min(min_num, A_i_num[A[i]])

# 要素数が1の数を持っている人が1人もいない場合
if min_num > 1:
    print(-1)
    exit()

# 最大の要素を持っている人の番号を出力
max_num = 0
max_num_person = 0
for key, value in person_to_num.items():
    # max_num = max(max_num, value)
    # if max_num == value:
    #     max_num_person = key
    if value > max_num:
        max_num = value
        max_num_person = key

print(max_num_person)
