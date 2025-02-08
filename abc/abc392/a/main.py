A = list(map(int, input().split()))
num1 = A[0] * A[1]
num2 = A[1] * A[2]
num3 = A[2] * A[0]
if (num1 == A[2]) or (num2 == A[0]) or (num3 == A[1]):
    print("Yes")
else:
    print("No")
