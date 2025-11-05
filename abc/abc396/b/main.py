from collections import deque

Q = int(input())
cards = deque()
for i in range(Q):
    cards.append(0)

for i in range(Q):
    query = input()
    if query == "2":
        print(cards.pop())
    else:
        query, card_num = query.split()
        cards.append(card_num)
