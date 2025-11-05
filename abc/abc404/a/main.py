from collections import defaultdict

S = input()
list_S =list(S)
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cnt_alphabets = defaultdict(int)

for alphabet in alphabets:
    cnt_alphabets[alphabet] = 0

for s in list_S:
    cnt_alphabets[s] += 1

for alphabet in alphabets:
    if cnt_alphabets[alphabet] == 0:
        print(alphabet)
        exit()
