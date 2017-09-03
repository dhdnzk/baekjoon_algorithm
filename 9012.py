def is_valid(x):

    start_parenthesis = 0
    end_parenthesis = 0

    for i in range(0, len(x)):
        if x[i] == "(":
            start_parenthesis += 1
        else:
            end_parenthesis += 1

        if end_parenthesis > start_parenthesis:
            print("NO")
            return

    if start_parenthesis != end_parenthesis:
        print ("NO")
        return

    print("YES")
    return


count = input("")

for i in range(0, int(count)):
    is_valid(input(""))
