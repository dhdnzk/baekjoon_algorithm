def distance(x1, y1, x2, y2):
    length_x = abs(x2 - x1)
    length_y = abs(y2 - y1)
    return (length_x * length_x + length_y * length_y)**0.5


def cross_calc(x1, y1, x2, y2, star_list):

    cross_counter = 0

    for i in star_list:
        if distance(x1, y1, i[0], i[1]) > i[2] and distance(x2, y2, i[0], i[1]) > i[2]:
            cross_counter += 0
        elif distance(x1, y1, i[0], i[1]) < i[2] and distance(x2, y2, i[0], i[1]) < i[2]:
            cross_counter += 0
        else:
            cross_counter += 1

    return int(cross_counter)


count = int(input(""))

for i in range(0, count):

    raw_data = input("").split(" ")
    start_x = int(raw_data[0])
    start_y = int(raw_data[1])
    destination_x = int(raw_data[2])
    destination_y = int(raw_data[3])

    star_infos = []

    num_of_stars = int(input(""))

    for j in range(0, num_of_stars):

        star_info = input("").split(" ")
        star_info = [int(i) for i in star_info]
        star_infos.append(star_info)

    print(cross_calc(start_x, start_y,
                     destination_x, destination_y,
                     star_infos))

