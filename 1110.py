num = int(input())
cycle_counter = 0
prev_tmp = num
new_tmp = 0

if prev_tmp < 10:
    prev_tmp *= 10
    num *= 10

while True:

    added_num = int(prev_tmp % 10) + int(prev_tmp / 10)
    new_tmp = (prev_tmp % 10) * 10 + (added_num % 10)
    cycle_counter += 1
    if new_tmp == num:
        break

    prev_tmp = new_tmp

print(cycle_counter)


