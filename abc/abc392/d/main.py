from collections import  defaultdict

N = int(input())
qubes = [list(map(int, input().split())) for _ in range(N)]

qubes_dict = [defaultdict(int) for _ in range(N)]
for i in range(N):
