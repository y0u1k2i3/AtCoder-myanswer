N, S = map(int, input().split())
A = list(map(int, input().split()))

if min(A) > S:
    print("No")
    exit()

