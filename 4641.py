while True:
    data = input("")

    if data == "-1":
        break

    data = data.split(" ")
    data = [int(i) for i in data]
    data.sort()

    counter = 0

    if data[0] == 0:
        counter -= 1

    for i in data:
        for j in data:
            if i == j * 2:
                counter += 1

    print(counter)
