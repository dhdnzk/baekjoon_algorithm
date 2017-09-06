def d(n):
    DUMMY_VALUE = 2
    new_num = int(n)
    for i in n:
        new_num += int(i)
        if new_num > 10000:
            return DUMMY_VALUE

    return new_num

num_list = [int(i + 1) for i in range(0, 10000)]
self_num_list = [d(str(i + 1)) for i in range(0, num_list.__len__())]

self_num_list = [i for i in set(self_num_list)]
self_num_list.sort()

for i in range(0, self_num_list.__len__()):
    num_list.pop(num_list.index(self_num_list[i]))

for i in num_list:
    print(i)


