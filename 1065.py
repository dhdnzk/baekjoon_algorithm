def calc_hansu(n):
    num_list = list(str(n))
    num_list = [int(i) for i in num_list]

    if num_list.__len__() == 1:
        return 1

    interval = num_list[0] - num_list[1]

    for i in range(0, num_list.__len__()):
        if i == num_list.__len__() - 1:
            break

        if num_list[i] - num_list[i + 1] != interval:
            return 0

    return 1


def calc_hansus(n):
    hansus_count = 0
    for i in range(0, int(n)):
        hansus_count += calc_hansu(i + 1)

    return hansus_count

print(calc_hansus(input()))


