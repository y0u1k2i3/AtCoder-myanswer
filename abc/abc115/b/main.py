n = int(input())
P = []
for i in range(n):
    P.append(int(input()))

print(sum(P) - max(P) // 2)