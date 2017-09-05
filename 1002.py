def calc(x1, y1, r1, x2, y2, r2):
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        if distance(x1, y1, x2, y2) > r1 + r2:
            return 0
        elif distance(x1, y1, x2, y2) == r1 + r2:
            return 1
        elif distance(x1, y1, x2, y2) < r1 + r2:
            small_r = r1 if r1 < r2 else r2
            big_r = r1 if r1 > r2 else r2

            if distance(x1, y1, x2, y2) + small_r == big_r:
                return 1
            elif distance(x1, y1, x2, y2) + small_r < big_r:
                return 0
            elif distance(x1, y1, x2, y2) + small_r > big_r:
                return 2


def distance(x1, y1, x2, y2):
    length_x = abs(x2 - x1)
    length_y = abs(y2 - y1)

    return (length_x * length_x + length_y * length_y)**0.5


count = int(input(""))

for i in range(0, count):
    raw_data = input("").split(" ")

    x1 = float(raw_data[0])
    y1 = float(raw_data[1])
    r1 = float(raw_data[2])

    x2 = float(raw_data[3])
    y2 = float(raw_data[4])
    r2 = float(raw_data[5])

    print(calc(x1, y1, r1, x2, y2, r2))
