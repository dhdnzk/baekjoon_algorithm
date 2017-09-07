def calc(a, b):

    if a % 10 == 0:
        return 10

    first_num_list = list()
    cur_a = int(a)

    while True:
        tmp_final_num = int(str(cur_a)[str(cur_a).__len__() - 1])

        if first_num_list.__len__() > 0:
            if first_num_list[0] == tmp_final_num:
                break

        first_num_list.append(int(tmp_final_num))
        cur_a *= a

    idx = (b % first_num_list.__len__()) - 1
    return first_num_list[idx]


count = int(input())

for i in range(0, count):
    raw_data = input().split(" ")
    print(calc(int(raw_data[0]), int(raw_data[1])))


