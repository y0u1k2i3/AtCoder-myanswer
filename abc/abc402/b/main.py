from collections import deque

Q = int(input())
orders = deque()
for i in range(Q):
    query = input()
    if query == "2":
        print(orders.popleft())
    else:
        _, x = query.split()
        orders.append(x)
