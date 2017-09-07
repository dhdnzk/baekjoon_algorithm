def combination(a, b):
    cur_a = a
    cur_b = b
    upper = 1
    under = 1

    for i in range(0, b):
        upper *= cur_a
        cur_a -= 1

        under *= cur_b
        cur_b -= 1

    return int(upper / under)


def pinary_number(n):

    n = int(n)
    counter = 0

    if n % 2 == 0:
        max_num_of_1 = int(n / 2)
    else:
        max_num_of_1 = int(n / 2) + 1

    target_max_num_of_a = max_num_of_1 - 1

    for i in range(0, target_max_num_of_a + 1):
        result = combination(n - (i + 1), i)
        counter += result

    return counter


length_of_number = input()
print(pinary_number(length_of_number))
