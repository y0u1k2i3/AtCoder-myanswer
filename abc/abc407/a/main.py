A, B = map(int, input().split())
C1 = A / B
C2 = A // B
if C1 - C2 < 0.5:
    print(C2)
else:
    print(C2 + 1)
