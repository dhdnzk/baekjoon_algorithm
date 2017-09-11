num_of_num = int(input())

raw_data = input().split(" ")
raw_data = [int(i) for i in raw_data]

prime_number_counter = 0

for i in range(0, num_of_num):

    if raw_data[i] == 2:
        prime_number_counter += 1

    elif raw_data[i] > 2:
        for j in range(2, raw_data[i]):
            if raw_data[i] % j == 0:
                break
            if j == raw_data[i] - 1:
                prime_number_counter += 1


print(prime_number_counter)

