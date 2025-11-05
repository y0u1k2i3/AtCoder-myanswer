from itertools import combinations

A = list(map(int, input().split()))
two_flag = []
three_flag = []
A_variations = list(set(A))
A_comb = list(combinations(A_variations, 2))

for i, j in A_comb:
    i_num = A.count(i)
    j_num = A.count(j)
    if (i_num >= 2 and j_num >= 3) or (i_num >= 3 and j_num >= 2) or (i_num >= 3 and j_num >= 3):
        print("Yes")
        exit()

print("No")
