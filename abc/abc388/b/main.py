N, D = map(int, input().split())
sneaks = []
for i in range(N):
    sneaks.append(list(map(int, input().split())))

for i in range(1, D + 1):
    new_sneaks = []
    for sneak in sneaks:
        new_sneaks.append(sneak[0] * (sneak[1] + i))
    print(max(new_sneaks))
