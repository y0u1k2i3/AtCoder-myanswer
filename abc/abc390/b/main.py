N = int(input())
A = list(map(int, input().split()))

kouhi = A[1] / A[0]

# for i in range(N - 1):
#     if A[i + 1] / A[i] == kouhi:
#         kouhi = A[i + 1] / A[i]
#     else:
#         print("No")
#         exit()

# print("Yes")

B = [A[0]]
for i in range(1, N):
    B.append(A[i - 1] * kouhi)

if A == B:
    print("Yes")
else:
    print("No")