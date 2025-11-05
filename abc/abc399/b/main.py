from collections import defaultdict

N = int(input())
P = list(map(int, input().split()))

scores = list(set(P))
scores = sorted(scores, reverse=True)
# key: score value: person
score_to_person = defaultdict(list)
# key: person value: rank
ranking = defaultdict(int)

for i in range(N):
    # ある得点を持つ人をリストアップ
    score_to_person[P[i]].append(i)

# # 得点の高い順にソート
# score_to_person = sorted(score_to_person.items(), key=lambda x: x[0], reverse=True)

prev_num = 1
prev_rank = 1
for i in range(len(scores)):
    persons = score_to_person[scores[i]]
    for person in persons:
        ranking[person] = prev_rank
    prev_num = len(persons)
    prev_rank = prev_rank + prev_num

for i in range(N):
    print(ranking[i])
