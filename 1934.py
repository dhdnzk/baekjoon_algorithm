count = int(input(""))

for i in range(0, count):

    raw_data = input("").split(" ")

    a = int(raw_data[0])
    b = int(raw_data[1])

    LCM = a if a >= b else b

    while True:
        if LCM % a == 0 and LCM % b == 0:
            break
        LCM += 1

    print(LCM)
