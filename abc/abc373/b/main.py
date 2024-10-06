s = input()
# 大文字アルファベットのリスト
alphabet = [chr(i) for i in range(65, 65+26)]
pre_idx = s.index('A')
ans = 0
for chr in alphabet:
    now_idx = s.index(chr)
    ans += abs(pre_idx - now_idx)
    pre_idx = now_idx

print(ans)
