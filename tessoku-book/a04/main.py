n = int(input())
nums = []
while n != 0:
    nums.append(n % 2)
    n = n // 2

nums.reverse()
print(''.join(map(str, nums)).zfill(10))