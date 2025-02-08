A, B, C = map(int, input().split())
abc = [A, B, C]
abc.sort()

if A == B == C:
    print("Yes")
    exit()

if abc[0] + abc[1] == abc[2]:
    print("Yes")
    exit()

print("No")