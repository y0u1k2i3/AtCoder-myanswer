from sys import orig_argv


n = int(input())
h = list(map(int, input().split()))

def grow_flowers(l):
    if len(l) == 1:
        return l[0]
    
    mid = l.index(min(l))
    l = [x - l[mid] for x in l]
    if mid == 0:
        left = l[:mid + 1]
        right = l[mid + 1:]
    elif mid == len(l) - 1:
        left = l[:mid - 1]
        right = l[mid - 1:]
    else:
        left = l[:mid]
        right = l[mid:]

    return grow_flowers(left) + grow_flowers(right)
    
print(grow_flowers(h))