a = int(input())
b = int(input())
c = int(input())
a_b_c = str(a * b * c)
counter_list = [0 for i in range(0, 10)]

for i in a_b_c:
    counter_list[int(i)] += 1

for i in counter_list:
    print(i)
