from copy import deepcopy


A = list(map(int, input().split()))
ans = deepcopy(A)
ans.sort()
cnt = 0
for i in range(4):
    B = deepcopy(A)
    tmp = B[i]
    B[i] = B[i + 1]
    B[i + 1] = tmp
    if ans == B:
        print("Yes")
        exit()

else:
    print("No")
