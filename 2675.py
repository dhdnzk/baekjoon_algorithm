for i in range(0, int(input())):
    raw_data = input().split(" ")
    for j in range(0, raw_data[1].__len__()):
        for k in range(0, int(raw_data[0])):
            print(raw_data[1][j], end="")

    print("")
