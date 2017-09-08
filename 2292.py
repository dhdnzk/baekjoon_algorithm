def calc_distance(n):
    cur_value = 1
    distance = 0
    while True:
        cur_value += 6 * distance
        if cur_value >= n:
            return distance + 1
        distance += 1

target_num = int(input())

print(calc_distance(target_num))
