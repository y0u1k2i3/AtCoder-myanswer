n = int(input())
list_n = list(str(n))
num1 = []
num1.append(list_n[1])
num1.append(list_n[2])
num1.append(list_n[0])

num2 = []
num2.append(list_n[2])
num2.append(list_n[0])
num2.append(list_n[1])

print(int(''.join(num1)), int(''.join(num2)))