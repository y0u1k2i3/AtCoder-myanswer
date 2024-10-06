h, w = map(int, input().split())
meiro = []
for i in range(h):
    line = input()
    if line != '.' * w:
        meiro.append(line)

del_cnt = []
for col in range(w):
    cnt = 0
    for row in range(len(meiro)):
        if meiro[row][col] == '.':
            cnt += 1
    if cnt == len(meiro):
        del_cnt.append(col)

for row in range(len(meiro)):
    new_line = ''
    for i in range(w):
        if i not in del_cnt:
            new_line += meiro[row][i]
    meiro[row] = new_line

for line in meiro:
    print(''.join(line))
