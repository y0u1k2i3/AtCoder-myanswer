from collections import defaultdict

K = int(input())
S = input()
T = input()

cnt_S_same = defaultdict(int)
# cnt_S_diff = defaultdict(int)
cnt_T = defaultdict(int)
ans = 0

for i in range(len(T)):
    cnt_T[T[i]] += 1

for i in range(len(S)):
    if S[i] in cnt_T:
        cnt_S_same[S[i]] += 1
    else:
        # cnt_S_diff[S[i]] += 1
        ans += 1

for k, v in cnt_S_same.items():
    ans += abs(v - cnt_T[k])

if 0 <= ans <= K:
    print("Yes")
else:
    print("No")
    