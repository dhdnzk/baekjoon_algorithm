user_input = input().split(" ")

n1 = int(user_input[0][::-1])
n2 = int(user_input[1][::-1])

print(n1 if n1 > n2 else n2)


