min = int(input())
max = int(input())

num_list = list()

counter = 1
while True:
    target_num = counter * counter
    if min <= target_num <= max:
        num_list.append(target_num)
    elif target_num > max:
        break

    counter += 1

if num_list.__len__() == 0:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])

