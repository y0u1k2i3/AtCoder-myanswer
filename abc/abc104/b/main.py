from sys import orig_argv


s = input()
if s[0] != 'A' or s[1].isupper():
    print('WA')
    exit()

large_c = 0
for i in range(2, len(s) - 1):
    if s[i] == 'C':
        large_c += 1
        if large_c > 1:
            print('WA')
            exit()
    else:
        if s[i].isupper():
            print('WA')
            exit()

if large_c == 0:
    print('WA')
    exit()

if s[-1] == 'C' or s[-1].isupper():
    print('WA')
    exit()
else:
    print('AC')