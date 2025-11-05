from collections import  defaultdict

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
dice_sides = []

dices_dict = []
for i in range(N):
    dice_i = dices[i]
    k = dice_i[0]
    dice_sides.append(dice_i[0])
    dice_i = dice_i[1:]
    cnt = defaultdict(int)
    for j in range(len(dice_sides)):
        cnt[dice_sides[j]] += 1
    dices_dict.append(cnt)


