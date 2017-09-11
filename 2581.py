def is_prime_num(n):
    if n == 2:
        return True

    elif n > 2:
        for j in range(2, n):
            if n % j == 0:
                return False
            if j == n - 1:
                return True

prime_list = list()

min_num = int(input())
max_num = int(input())

for i in range(min_num, max_num + 1):
    if is_prime_num(i):
        prime_list.append(i)

prime_list.sort()
sum_of_prime_num = 0
for i in prime_list:
    sum_of_prime_num += i


if prime_list.__len__() == 0:
    print(-1)
else:
    print(sum_of_prime_num)
    print(prime_list[0])

