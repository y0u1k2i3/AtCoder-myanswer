from collections import defaultdict

N = int(input())
# 人iは人Piを見つめている
P = list(map(int, input().split()))
# 人iは数Qiが書かれたゼッケンを着けている
Q = list(map(int, input().split()))

# people = defaultdict(int)
# key: ゼッケンiを着ている人, value: ゼッケンiの番号
person_zekken = defaultdict(int)
# key: ゼッケンiの番号, value: ゼッケンiを着ている人
zekken_person = defaultdict(int)
watched_zekkens = []

for i in range(N):
    person_zekken[i + 1] = Q[i]
    zekken_person[Q[i]] = i + 1

for i in range(N):
    # ゼッケンi + 1を着ている人
    person_i = zekken_person[i + 1]
    # ゼッケンi + 1を着ている人が見ている人
    watched_person_i = P[person_i - 1]
    # ゼッケンi + 1を着ている人が見ている人が着ているゼッケン
    watched_zekken_i = person_zekken[watched_person_i]
    watched_zekkens.append(watched_zekken_i)

for i in range(len(watched_zekkens)):
    if i != len(watched_zekkens) - 1:
        print(watched_zekkens[i], end=" ")
    else:
        print(watched_zekkens[i])
