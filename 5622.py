def calc_time(char):
    if 'A' <= char < 'D':
        return 3
    elif 'D' <= char < 'G':
        return 4
    elif 'G' <= char < 'J':
        return 5
    elif 'J' <= char < 'M':
        return 6
    elif 'M' <= char < 'P':
        return 7
    elif 'P' <= char < 'T':
        return 8
    elif 'T' <= char < 'W':
        return 9
    elif 'W' <= char <= 'Z':
        return 10


user_input = input()
time_counter = 0

for i in user_input:
    time_counter += calc_time(i)

print(time_counter)
