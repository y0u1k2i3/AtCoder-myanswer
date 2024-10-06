s = input()
t = input()
if s == t:
    print(0)
for i in range(max(len(s), len(t))):
    if i >= len(s) or i >= len(t):
        print(i + 1)
        exit()
    else:
        if s[i] != t[i]:
            print(i + 1)
            exit()