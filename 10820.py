while True:
    capital_letter = 0
    small_letter = 0
    numeric_letter = 0
    space = 0

    raw_data = input("")

    if raw_data == "":
        break

    for i in range(0, len(raw_data)):
        if raw_data[i] == " ":
            space += 1
        elif raw_data[i].isnumeric():
            numeric_letter += 1
        elif raw_data[i].isupper():
            capital_letter += 1
        else:
            small_letter += 1

    print(str(small_letter) +
          " " + str(capital_letter) +
          " " + str(numeric_letter) +
          " " + str(space))
