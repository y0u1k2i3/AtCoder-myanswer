from collections import deque

Q = int(input())

sneaks = deque()
cnt_2_num = [0] * (3 * (10**5) + 1)
cnt_2 = 0
for i in range(Q):
    query = input()
    if query == "2":
        cnt_2 += 1
        cnt_2_num[cnt_2] = cnt_2_num[cnt_2 - 1] + sneaks[0][0]
        sneaks.popleft()
    else:
        query_num1, query_num2 = query.split()
        query_num2 = int(query_num2)
        if query_num1 == "1":
            # (長さ，座標，2が今までに何回出てきたか)を追加
            if len(sneaks) == 0:
                sneaks.append((query_num2, 0, cnt_2))
            else:
                sneaks.append((query_num2, sneaks[-1][0] + sneaks[-1][1], cnt_2))
        elif query_num1 == "3":
            if cnt_2 == 0:
                print(sneaks[query_num2 - 1][1])
            else:
                print(sneaks[query_num2 - 1][1] - (cnt_2_num[cnt_2]))
