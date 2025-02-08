X = int(input())
# print(2432902008176640000 // (3 * (10 ** 18)))
MAX = 3 * (10 ** 18)
ans = 1
for i in range(2, MAX + 1):
    ans *= i
    if ans == X:
        print(i)
        break