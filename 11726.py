def combination(i, j):

    numerator_start = i
    denominator_start = j
    numerator = 1
    denominator = 1

    for idx in range(0, j):
        numerator *= numerator_start
        numerator_start -= 1

    for idx in range(0, j):
        denominator *= denominator_start
        denominator_start -= 1

    return int(numerator / denominator) % 10007


def calculator(num):

    landscape_max = int(int(num) / 2)
    number_of_cases = 1
    for i in range(1, landscape_max + 1):
        cur_space = int(num) - int(i)
        number_of_cases += int(combination(cur_space, i))
        number_of_cases %= 10007

    return int(number_of_cases)

n = int(input(""))
print(calculator(n))

