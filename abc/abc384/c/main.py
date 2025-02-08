from collections import defaultdict
a, b, c, d, e = map(int, input().split())
scores = defaultdict(int)
scores["A"] = a
scores["B"] = b
scores["C"] = c
scores["D"] = d
scores["E"] = e

user_scores = defaultdict(int)
users = ["A", "B", "C", "D", "E", "AB", "AC", "AD", "AE", "BC", "BD", "BE", "CD", "CE", "DE", "ABC", "ABD", "ABE", "ACD", "ACE", "ADE", "BCD", "BCE", "BDE", "CDE", "ABCD", "ABCE", "ABDE", "ACDE", "BCDE", "ABCDE"]

for user in users:
    user = list(user)
    user_score = 0
    for alphabet in user:
        user_score += scores[alphabet]
    user = ''.join(user)   
    user_scores[user] = user_score

user_scores = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)

if len(set(score for _, score in user_scores)) == len(users):
    for user_score in user_scores:
        print(user_score[0])

else:
    former_score = 0
    same_score_users = []
    for i, user_score in enumerate(user_scores):
        if i == 0:
            former_score = user_score[1]
            same_score_users.append(user_score[0])
            continue
        if user_score[1] != former_score:
            same_score_users = sorted(same_score_users)
            for same_score_user in same_score_users:
                print(same_score_user)
            same_score_users = []
            same_score_users.append(user_score[0])
            former_score = user_score[1]
        else:
            same_score_users.append(user_score[0])
        if i == len(user_scores) - 1:
            same_score_users = sorted(same_score_users)
            for same_score_user in same_score_users:
                print(same_score_user)
