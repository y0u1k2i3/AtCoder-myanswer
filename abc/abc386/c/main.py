from collections import defaultdict

K = int(input())
S = input()
T = input()

if S == T:
    print("Yes")
    exit()

elif len(S) == len(T):
    diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff += 1
    if diff <= K:
        print("Yes")
    else:
        print("No")
    exit()

elif len(S) == len(T) - 1:
    fs = 0
    bs = 0
    for i in range(2):
        for j in range(len(S)):
            if i == 0:
                


elif len(S) == len(T) + 1:
    for i in range(len(S)):
        if i == 0:
            edited_S = S[1:]
        elif i == len(S) - 1:
            edited_S = S[:-1]
        else:
            edited_S = S[:i] + S[i + 1:]
        if edited_S == T:
            print("Yes")
            exit()
    print("No")
    
else:
    print("No")