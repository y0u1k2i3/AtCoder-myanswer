n, q = map(int, input().split())
idx_L = 1
idx_R = 2
ans = 0

def move_to_t(n, from_, ng, to):
    if from_ > to:
        from_, to = to, from_
    
    if from_ < ng < to:
        return from_ + n - to 
    else:
        return to - from_

for i in range(q):
    h, t = map(str, input().split())
    t = int(t)
    if h == 'L':
        ans += move_to_t(n, idx_L, idx_R, t)
        idx_L = t
    else:
        ans += move_to_t(n, idx_R, idx_L, t)
        idx_R = t

print(ans + 1)