user_input = input().split(" ")
result = ""

if user_input[0] == "1":
    result = "ascending"
    for i in range(0, user_input.__len__()):
        if user_input[i] != str(i + 1):
            result = "mixed"
            break

elif user_input[0] == "8":
    result = "descending"
    for i in range(0, user_input.__len__()):
        if user_input[i] != str(user_input.__len__() - i):
            result = "mixed"
            break


print(result)
