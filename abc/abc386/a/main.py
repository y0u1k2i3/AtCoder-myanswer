A = list(map(int, input().split()))
if len(set(A)) == 2:
    print("Yes")
    exit()

print("No")